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
usage: cfparser.py [-h] [-t TEMPLATE_DIR] contest [root_dir]

Simple CLI tool for parsing Codeforces contest test samples

positional arguments:
  contest               ID of the contest
  root_dir              Optional argument root dir, where file structure will
                        be created. By default, this is current dir

optional arguments:
  -h, --help            show this help message and exit
  -t TEMPLATE_DIR, --template_dir TEMPLATE_DIR
                        Optional argument for templates. Expected path to
                        directory containing subdirectory `contest` whose
                        contents is copied to contest root dir, and
                        subdirectory `problem` with template files that are
                        copied to every problem subdirectory. If not provided,
                        no templates are copied.

```

### Example 1: Download contest data
Download data for contest with id 123 ([link](http://codeforces.com/contest/123))
##### Command
```
cfparser 123 ./
```
##### Files created on drive
```
.1
├── A
│   └── tests
│       ├── test.in.0
│       └── test.out.0
├── B
│   └── tests
│       ├── test.in.0
│       └── test.out.0
└── C
    └── tests
        ├── test.in.0
        └── test.out.0

```
### Example 2: Using templates
Templates dir can be provided with files that are copied to contest directory and problems subdirectories.

##### Template dir contents
Example of templates dir containing `CMakeLists.txt` intended to be copied
to contest root dir and `main.cpp`, `Makefile` and `test.sh` script that are copied to every problem.
```
templates
├── contest
│   └── CMakeLists.txt
└── problem
    ├── main.cpp
    ├── Makefile
    └── test.sh
```
##### Usage
```
cfparser 1 ./ --template ./templates
```


##### Files created on drive
```
1
├── A
│   ├── main.cpp
│   ├── Makefile
│   ├── tests
│   │   ├── test.in.0
│   │   └── test.out.0
│   └── test.sh
├── B
│   ├── main.cpp
│   ├── Makefile
│   ├── tests
│   │   ├── test.in.0
│   │   └── test.out.0
│   └── test.sh
├── C
│   ├── main.cpp
│   ├── Makefile
│   ├── tests
│   │   ├── test.in.0
│   │   └── test.out.0
│   └── test.sh
└── CMakeLists.txt

```

