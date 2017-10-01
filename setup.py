from setuptools import setup, find_packages

setup(name='cfparser',
      version='0.1',
      description='Codeforces test sample parser',
      long_description='CLI tool for parsing sample tests for Codeforces contests',
      keywords='codeforces contests tests parsing',
      url='https://github.com/mratkovic/codeforces-parser',
      author='Marko Ratkovic',
      author_email='marko.ratkovic0@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
            'beautifulsoup4==4.6.0',
            'certifi==2017.7.27.1',
            'chardet==3.0.4',
            'idna==2.6',
            'requests==2.18.4',
            'urllib3==1.22'
      ],
      include_package_data=True,
      zip_safe=False)