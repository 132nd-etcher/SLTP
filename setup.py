# coding=utf-8

from setuptools import setup

# noinspection SpellCheckingInspection
setup(
    name='SLTP',
    version='0.0.2',
    author='132nd-etcher',
    url='https://github.com/132nd-etcher/sltp',
    packages=['sltp'],
    requires=['mpmath'],
    dependency_links=['https://github.com/132nd-etcher/utils.git#egg=utils']
)
