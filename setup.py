from setuptools import setup, find_packages
from typing import List


def get_requirements(filepath: str) -> List:

    Minus_E_Dot = "-e ."
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if Minus_E_Dot in requirements:
            requirements.remove(Minus_E_Dot)

    return requirements


setup(
    name='ML Project',
    version='2.0.6',
    author='Hamza',
    author_email='hi437587@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
