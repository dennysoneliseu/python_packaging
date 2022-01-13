# Import required functions 
from setuptools import setup, find_packages

# Call setup function

setup(
    author="Dennyson Eliseu - copied from James Fulton",
    description="A package for converting imperial lengths and weights.",
    name="impyrial",
    version="0.1.0",
    packages=find_packages(include=["impyrial", "impyrial.*"]),
    install_requires=["numpy>=1.10", "pandas"],
)

