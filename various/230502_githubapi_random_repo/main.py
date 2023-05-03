import requests
import random

# set up the base URL for the GitHub API
base_url = "https://api.github.com/"

# set up the endpoint to search for repositories that use Rust
endpoint = "search/repositories"

# set up the parameters for the search query
params = {
    "q": "stars:<2",  ## <== change the number of stars here
}

# send a GET request to the search endpoint with the parameters
response = requests.get(base_url + endpoint, params=params)

# get the response as JSON data
repos = response.json()

# get a random repository from the list of repositories that use Rust
random_repo = random.choice(repos["items"])

# print the name and URL of the random repository
print("Random repository: ", random_repo["name"])
print("Repository URL: ", random_repo["html_url"])
