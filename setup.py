from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="preamchand228",
    description="A small package for flowers prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/premchand228/Flowerspred_CNN",
    author_email="pream.chand228@gmail.com",
    packages=["src"],
    python_requires=">=3.6",
    install_requires=[
        "dvc",
        "tensorflow",
        "matplotlib",
        "numpy",
        "pandas",
        "tqdm",
        "PyYAML",
        "boto3" ,
    ]
)
