"""
This is a crazy idea, but fun.
Create a list of programming languages

https://leetcode.com/problemset/all/

and a list between 1 and 2081 which are the quantity of leetcode chanllenges that exist
some of them are not available for non premium users, but that is ok

https://www.reddit.com/r/dailyprogrammer/
for the reddit page create a number between 1 and 399

The objective here is to create some random challenges to take a look at the languages
that I'm interested in and also do some interesting challenges.

To run the program just write:
$ python3 leet_code_challenge_lottery.py

"""

from random import sample


list_languages = [
    "Python",
    "C",
    "Go",
    "Java",
    "C++",
    "R",
    "Julia",
    "Haskell",
    "Clojure",
    "Common Lisp",
    "Scala",
    "bash",
    "awk",
    "Rust",
    "Nim",
    "JavaScript",
    "PHP",
    "Kotlin",
    "Fortran",
    "Ruby"
]


dict_challenges = {
    "leet_code": list(range(1, 2081)),
    "reddit_dailyprogrammer": list(range(1, 399)),
}


print("Chosen programming language: ",sample(list_languages, 1)[0])
chosen_platform = sample(list(dict_challenges.keys()), 1)[0]
print("Chosen challenge platform: ", chosen_platform)
chosen_id = sample(dict_challenges.get(chosen_platform),1)[0]
print("Chosen challenge id: ", chosen_id)


