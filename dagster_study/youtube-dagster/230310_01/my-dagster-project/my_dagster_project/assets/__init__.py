import yaml  # type: ignore
from yaml.loader import SafeLoader  # type: ignore
from dagster import asset
from github import Github
import pandas as pd
from datetime import timedelta
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pickle
import jupytext


with open("./my_dagster_project/assets/token.yaml") as f:
    data = yaml.load(f, Loader=SafeLoader)

ACCESS_TOKEN = data["ACCESS_TOKEN"]


@asset
def github_stargazer():
    return list(
        Github(ACCESS_TOKEN).get_repo("dagster-io/dagster").get_stargazers_with_dates()
    )


@asset
def github_stargazers_by_week(github_stargazer):
    df = pd.DataFrame(
        [
            {
                "users": stargazer.user.login,
                "week": startgazer.starred_at.date()
                + timedelta(days=6 - startgazer.starred_at.weekday()),
            }
            for startgazer in github_stargazer
        ]
    )

    return df.groupby("week").count().sort_values(by="week")


@asset
def github_stars_notebook(github_stargazers_by_week):
    markdown = f"""
# Github Stars

```python
import pickle
github_stargazers_by_week = pickle.loads({pickle.dumps(github_stargazers_by_week)!r})

## Github Stars by Week, last 52 weeks

github_stargazers_by_week.tail(52).reset_index().plot.bar(x="week", y="users")

    """
    nb = jupytext.reads(markdown, "md")
    ExecutePreprocessor().preprocess(nb)
    return nbformat.writes(nb)


from github import InputFileContent


@asset
def github_stars_notebook_gist(context, github_stars_notebook):
    gist = (
        Github(ACCESS_TOKEN)
        .get_user()
        .create_gist(
            public=False,
            files={
                "github_stars.ipynb": InputFileContent(github_stars_notebook),
            },
        )
    )
    context.log.info(f"Notebook created at {gist.html_url}")
    return gist.html_url
