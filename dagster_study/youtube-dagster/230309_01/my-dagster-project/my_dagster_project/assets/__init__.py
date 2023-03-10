import yaml # type: ignore
from yaml.loader import SafeLoader # type: ignore
import pickle

from dagster import asset
from github import Github
import pandas as pd
from datetime import timedelta
import nbformat
import jupytext
from nbconvert.preprocessors import ExecutePreprocessor

with open("./my_dagster_project/assets/token.yaml") as f:
    data = yaml.load(f, Loader=SafeLoader)

ACCESS_TOKEN = data["ACCESS_TOKEN"]

@asset
def github_stargazer():
    return list(Github(ACCESS_TOKEN).get_repo("dagster-io/dagster").get_stargazers_with_dates())

@asset
def github_stargazer_by_weeek(github_stargazer):
    df = pd.DataFrame(
        [
        {
        "users": stargazer.user.login,
        "week": startgazer.starred_at.date() + timedelta(days=6-startgazer.starred_at.weekday()),
        }
        for startgazer in github_stargazer
        ]
    )

    return df.groupby("week").count().sort_values(by="week")


@asset
def github_stars_notebook(github_stargazer_by_weeek):
    markdown = f"""
# Github Stars

```python
import pickle
github_stargazer_by_weeek = \
    pickle.loads({pickle.dumps(github_stargazer_by_weeek)!r})

## Github Stars by Week, last 52 weeks

github_stargazer_by_weeek.tail(52).reset_index().plot.bar(x="week", y="users")

    """
    nb = jupytext.reads(markdown, "md")
    ExecutePreprocessor().preprocess(nb)
    return nbformat.writes(nb)

