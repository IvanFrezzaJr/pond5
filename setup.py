
from setuptools import setup, find_packages


def read(filename):
    return [
        reg.strip() 
        for reg 
        in open(filename).readlines()
    ]


extras = {
    'develop': read('requirements-dev.txt')
}


setup(
    name='pond5',
    version="0.1.0",
    description='Pond5 project',
    packages=find_packages(exclude=".venv"),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={
        'dev': read("requirements-dev.txt")
    },
)
    