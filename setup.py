from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "ML Based Books Recommender System Collaborative-Filtering"
AUTHOR_USER_NAME = "Rahul Verma "
SRC_REPO = "books_recommender Collaborative-Filtering"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Rahul Verma",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RahulVermaAnirvity/End-to-End-Books-Recommender-System-Implementation-using-Collaborative-Filtering-",
    author_email="rahulvermaanirvity@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)