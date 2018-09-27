#!/usr/bin/env python
from setuptools import setup

with open("requirements.txt") as requirement_file:
    requirements = requirement_file.readlines()

setup(
    name='keras2tensorflow',
    version='1.0.0',
    description='General code to convert a trained keras model into an inference tensorflow model',
    # author='',
    # author_email='',
    # url='',
    packages=[''],
    entry_points={
        'console_scripts': [
            'keras2tensorflow = keras_to_tensorflow:main'
        ]
    },
    install_requires=requirements,
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
)
