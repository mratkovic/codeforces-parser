from setuptools import setup, find_packages

setup(name='cfparser',
      version='0.1',
      description='Codeforces test sample parser',
      long_description='CLI tool for parsing sample tests for Codeforces contests',
      keywords='codeforces contests tests parsing',
      url='https://github.com/mratkovic/codeforces-parser',
      author='Marko Ratkovic',
      author_email='marko.ratkovic@yahoo.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'beautifulsoup4==4.6.0',
          'requests==2.18.4',
      ],
      py_modules=['cfparser'],
      entry_points={
          'console_scripts': [
              'cfparse=cfparser:main',
          ],
      },
      zip_safe=False
      )
