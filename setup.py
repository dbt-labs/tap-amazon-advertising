#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-amazon-advertising',
      version='0.0.1',
      description='Singer.io tap for extracting data from the Amazon Advertising API',
      author='Fishtown Analytics',
      url='http://fishtownanalytics.com',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_amazon_advertising'],
      install_requires=[
          'tap-framework==0.0.4',
      ],
      entry_points='''
          [console_scripts]
          tap-amazon-advertising=tap_amazon_advertising:main
      ''',
      packages=find_packages(),
      package_data={
          'tap_amazon_advertising': [
              'schemas/*.json'
          ]
      })
