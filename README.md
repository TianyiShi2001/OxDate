# OxDate
Tools for Oxford Term Dates

## Dependency

Make sure you have Python 3 installed. Run `python --version` in your terminal to check.

```bash
$ python --version
3.x.x
```

Here is a guide on how to install Python 3: https://realpython.com/installing-python

## Install

```bash
pip install OxDate --user
```

## Usage

To instantiate an `OxDate()` object, a single argument, `date`, is required. It can be a `datetime` object provided by the built-in `datetime` module, or a date-like string, such as '1 Dec' and 'Mar 5 2020'. It defaults to the current date.

```python
from OxDate import OxDate
OxDate()
#           Monday 07 October 2019, week 0 of Michaelmas term.
#           Term starts: Sunday 13 October 2019
#           Term ends: Saturday 07 December 2019
#           Next vac: Christmas vac in 60 days
OxDate('Dec 1')
#           Sunday 01 December 2019, week 7 of Michaelmas term.
#           Term starts: Sunday 13 October 2019
#           Term ends: Saturday 07 December 2019
#           Next vac: Christmas vac in 6 days
```