import pickle
import json
import pandas as pd
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pickle
from dagster import asset


@asset
def dataset_00():
    return [1, 2, 3, 4]


@asset
def dataset_01():
    with open("./datasets/github_stargazer.json", "r") as f:
        data = json.load(f)

    return data


@asset
def dataset_02(dataset_01):
    df = pd.DataFrame(dataset_01)
    return df


@asset
def dataset_03(dataset_02):
    df = dataset_02.groupby("week").count().sort_values(by="week")
    return df


@asset
def github_stars_notebook(dataset_03):
    markdown = f"""
# Github Stars

```python
import pickle
dataset_03 = pickle.loads({pickle.dumps(dataset_03)!r})

## Github Stars by Week, last 52 weeks

dataset_03.tail(52).reset_index().plot.bar(x="week", y="users")

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
