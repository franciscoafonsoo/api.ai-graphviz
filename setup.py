# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='api_ai_graph',
    version='0.1.0',
    description='Render graphs based on API.AI intents.',
    long_description=readme,
    author='Francisco Pires',
    author_email='afonso.fcul@gmail.com',
    url='https://github.com/franciscoafonsoo/api_ai_graph',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)