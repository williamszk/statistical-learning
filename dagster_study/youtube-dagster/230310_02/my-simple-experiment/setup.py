from setuptools import find_packages, setup

setup(
    name="my_simple_experiment",
    packages=find_packages(exclude=["my_simple_experiment_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
