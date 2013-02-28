#!/usr/bin/env python


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = []

requires = []

setup(
    name='http_remote',
    version='0.0.1',
    description='Apple remote functionality over HTTP.',
    long_description=open('README.rst').read(),
    author='Chris Schomaker',
    author_email='schomaker.c@gmail.com',
    packages=packages,
    package_dir={'http_remote': 'http_remote'},
    include_package_data=True,
    install_requires=requires,
    license='',
    zip_safe=False,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        #'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.0',
        #'Programming Language :: Python :: 3.1',
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
    ),
)
