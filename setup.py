import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'Nextbook'
DESCRIPTION = 'Get random book suggestions from your library and add books. '
URL = 'https://github.com/Mandelliant/nextbook
EMAIL = 'mandelliant@gmail.com'
AUTHOR = 'Anthony Mandelli'

# What packages are required for this module to be executed?
REQUIRED = [
    'os', 'sys', 'csv', 'random'
]


here = os.path.abspath(os.path.dirname(/Users/anthonymandelli/Repos/nextbook/Nextbook))

setup(
    name=NAME,
    #version=about['__version__'],
    description=DESCRIPTION,
    # long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),

    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],

)
