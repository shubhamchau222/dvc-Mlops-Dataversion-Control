from setuptools import find_packages, setup , find_packages 

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="shubhamchau222",
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shubhamchau222/dvc-MLusecase-mlops",
    author_email="shubhamchau78@gmail.com",
    packages=["src"],
    python_requires=">=3.6",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)
