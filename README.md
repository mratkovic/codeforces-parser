# codeforces-parser

This is a python script that parses the sample tests from the [Codeforces](http://codeforces.com/) contest problem pages and generates the sample input/output files.

## Requirements:
This tool uses `requests` for loading contest site and `beautifulsoup4` for parsing *HTML*.

## Installation:
[Note] Installation is not necessary, the tool can be run as a script.

CLI tool can be installed by running following command:
```
python setup.py install
```

## Usage
``` cfparser --help``` prints detailed instructions
```
    usage: cfparser [-h] contest [root_dir]

    Simple CLI tool for parsing Codeforces contest test samples

    positional arguments:
      contest     ID of the contest
      root_dir    Optional argument root dir, where file structure will be
                  created. By default, this is current dir

    optional arguments:
      -h, --help  show this help message and exit
```

### Example
Download data for contest with id 123 ([link](http://codeforces.com/contest/123))
##### Command
```
cfparse 123
```
##### Files created on drive
```
./
└── 123
    ├── A
    │   └── tests
    │       ├── test.in.0
    │       ├── test.in.1
    │       ├── test.in.2
    │       ├── test.out.0
    │       ├── test.out.1
    │       └── test.out.2
    ├── B
    │   └── tests
    │       ├── test.in.0
    │       ├── test.in.1
    │       ├── test.in.2
    │       ├── test.out.0
    │       ├── test.out.1
    │       └── test.out.2
    ├── C
    │   └── tests
    │       ├── test.in.0
    │       ├── test.in.1
    │       ├── test.in.2
    │       ├── test.out.0
    │       ├── test.out.1
    │       └── test.out.2
    ├── D
    │   └── tests
    │       ├── test.in.0
    │       ├── test.in.1
    │       ├── test.in.2
    │       ├── test.out.0
    │       ├── test.out.1
    │       └── test.out.2
    └── E
        └── tests
            ├── test.in.0
            ├── test.in.1
            ├── test.in.2
            ├── test.out.0
            ├── test.out.1
            └── test.out.2
```

## Tests
Unit tests are placed in `tests` directory and can be executed by running
```
python tests/run_tests.py
```