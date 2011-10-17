#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='{{ PROJECT_MODULE }}',
      version='0.1',
      packages=find_packages(),
      package_data={'{{ PROJECT }}': ['templates/*.*']})
