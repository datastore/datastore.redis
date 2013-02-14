#!/usr/bin/env python

import re
from setuptools import setup, find_packages

pkgname = 'datastore.redis'

# gather the package information
main_py = open('datastore/redis/__init__.py').read()
metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", main_py))
packages = filter(lambda p: p.startswith(pkgname), find_packages())

# convert the readme to pypi compatible rst
try:
  try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
  except ImportError:
    readme = open('README.md').read()
except:
  print 'something went wrong reading the README.md file.'
  readme = ''

setup(
  name=pkgname,
  version=metadata['version'],
  description='redis datastore implementation',
  long_description=readme,
  author=metadata['author'],
  author_email=metadata['email'],
  url='http://github.com/datastore/datastore.redis',
  keywords=[
    'datastore',
    'redis',
  ],
  packages=packages,
  namespace_packages=['datastore'],
  install_requires=['datastore>=0.3.3', 'redis>=2.7.2'],
  test_suite='datastore.redis.test',
  license='MIT License',
  classifiers=[
    'Topic :: Database',
    'Topic :: Database :: Front-Ends',
  ]
)
