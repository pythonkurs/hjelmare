from setuptools import setup, find_packages
import sys, os

version = '0.2dev'

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
      scripts = ['scripts/getting_data.py', 'scripts/check_repo.py'],
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          # Project uses XML parsing, so ensure that the untangle get installed or upgraded on the target machine
          # Project uses GET to access a webservice
          'untangle>=1.1.0',
          'requests>=1.1.0',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
