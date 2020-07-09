from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my_code", # the name that you will install via pip
    version="1.0",
    author="Charlie May",
    author_email="camiv95@gmail.com",
    description="A function that extracts year, month, and day from a date column and add each to a new column",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/charlie-may86/lambdata-charlie-may-86.git",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)