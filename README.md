# LISTSERV list management with Python

The `listmanager.py` script included in this repository will extract names and
emails from an Excel (OOXML `.xlsx` format) spreadsheet and print them in the
format expected by LISTSERV for bulk import, _i.e._:

    First Last <email@domain.com>

This script is intended to be used to make updates to the ICSA / ICP LISTSERV
lists when students get added to or deleted from the "master" spreadsheet(s).

As of the present version, only workbook tabs with names matching `.*20\d\d$`
(_i.e._, `20xx` at the _end_ of the tab name) will be read and examined. The
individual sheets are expected to have this format:

_(possibly preceded by empty rows)_

| Name      | Major | Class Year | Email             |
|-----------|-------|------------|-------------------|
| Human One | CS    | 2017       | onehj@mail.uc.edu |
| Human Two | EE    | 2017       | twohk@mail.uc.edu |
| ⋮         | ⋮     | ⋮          | ⋮                 |

_(possibly followed by empty rows)_

The column labels are hard-coded at the moment, and the "Class Year" column is
currently ignored. Rather, the year matched from the name of the worksheet
(tab) is what's used to create the script's internal data structures, and to
retrieve list members by graduating year.

## Installation

### Install Python, `pip`, and `virtualenv`

You'll need [Python][] and [pip][]. On a modern OS (Python > 2.7.9), `pip`
should already be installed and in your `$PATH`.

Next you'll want to install [virtualenv][] globally, with `pip`, like this:

    sudo pip install virtualenv

or install the `virtualenv` package through your OS's package manager (_e.g._,
`apt-get` or `yum` for Linux, MacPorts or Homebrew on Mac).

On Windows, `sudo` isn't necessary. That's a Unix thing. If you have trouble,
refer to the `virtualenv` [installation documentation][virtualenv]

### Install Pandas and openpyxl

```
# First, create and activate the virtual environment
cd /path/where/you/cloned/this/repo
virtualenv venv
source venv/bin/activate

# Then use 'pip' to install dependencies
pip install -r requirements.txt
```

## Usage

The script has rudimentary built-in help, which you can reference with `python
listmanager.py --help`. But here are the basics:

```
# All names & emails on all tabs (all graduating years)
python listmanager.py germany.xlsx

# Or for only those students in the graduating class of 2020
python listmanager.py germany.xlsx 2020

# Export list of names to a file suitable for LISTSERV bulk subscription:
python listmanager.py germany.xlsx 2020 > germany_2020.txt
```

## To do

* Allow sorting of output by last name. Names are currently stored as
  one single string, "Firstname Lastname", just as they come out of the
  spreadsheet.

## References

* [Pandas][]
* [openpyxl][]


[python]: https://www.python.org/downloads/
[pip]: https://pip.pypa.io/en/stable/installing/
[virtualenv]: https://virtualenv.pypa.io/en/stable/installation/
[Pandas]: http://pandas.pydata.org/pandas-docs/stable/index.html
[openpyxl]: http://openpyxl.readthedocs.io/en/latest/index.html
