from setuptools import find_packages, setup
from typing import List



"""
This function will return list of requirements
"""

def get_requirements()->List[str]:
    requirement_list:List[str] = []
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="abdul-jaweed",
    author_email="jdgaming7320@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)


