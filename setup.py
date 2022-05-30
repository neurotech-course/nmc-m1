#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fp:
    install_requires = fp.read().splitlines()
install_requires = [i for i in install_requires if 'http' not in i]
    
    
setup(
    name="nmc-m1", 
    version="0.0",
    author="Microcredentials Team",
    author_email="",
    description="Neurotech Microcredentials Thing",
    keywords="some keywords",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = install_requires,
    url='https://github.com/neurotech-course/nmc-m1',
    license="BSD (3-clause)",
    entry_points={},#{"console_scripts": ["eegnb=eegnb.cli.__main__:main"]},
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)

