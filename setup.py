import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cateye",
    version = "0.0.2",

    author = "Dirk Gütlin",
    author_email = "dirk.guetlin@gmail.com",
    description = ("Uniform Categorization of Eyetracking in Python."),
    license = "BSD",
    keywords = "Eyetracking classification",
    url = "https://github.com/DiGyt/CatEye",
    packages=['cateye'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
        "numpy>=1.14"
        "remodnav",
        "-e git+https://github.com/pupil-labs/nslr.git",
        "-e https://github.com/pupil-labs/nslr-hmm.git"
    ],
)