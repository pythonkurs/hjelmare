from setuptools import setup, find_packages
import sys, os

version = '0.1dev'

setup(name='hjelmare',
      version=version,
      description="Testing Python",
      long_description="""\
Testing Python""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='testing python',
      author='MartinHjelmare',
      author_email='marhje52@kth.se',
      url='https://github.com/MartinHjelmare/hjelmare/',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
