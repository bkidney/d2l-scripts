# d2l-scripts

This repository is a collection of Python scripts to make D2L easier to work with. To install the requirements (currently only for `d2l_test_redact.py`), run

```shell
pip3 -r requirements.txt
```
## d2l_test_redact.py

This script can be used to remove the name and student number from a PDF of a test attempt preview printed from d2l.

### Usage

```
d2l_test_redact.py FILENAME 
d2l_test_redact.py (-d|--dir) DIR
d2l_test_redact.py (-h|--help)

Options: 
    -d --dir    Process all files in a driectory 
    -h --help   Show this screen.
```
