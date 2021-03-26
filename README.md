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

You'll need [Python][] and [pip][]. Python 2.7 might even work if you remove
the version "pins" from `requirements.txt`.

It's nice to install dependencies into their own virtual environment, so that
the versions of libraries like pandas and openpyxl required by this project
don't interfere with other Python programs.

Do that with either [virtualenv][] or [`python3 -m venv`][venv]:

    python -m venv venv
    
    # python 2.7 (install 'virtualenv' with pip)
    virtualenv venv

    source venv/bin/activate

    # then use 'pip' to install dependencies
    pip install -r requirements.txt

But if you don't have an opinion about that, you can skip all the virtualenv
stuff and just install the libraries to your home directory (the exact
destination varies by platform, but it's `~/.local` on Linux) with:

    pip install --user -r requirements.txt


## Usage

The script has rudimentary built-in help, which you can reference with `python
listmanager.py --help`. But here are the basics:

    # All names & emails on all tabs (all graduating years)
    python listmanager.py germany.xlsx
    
    # Or for only those students in the graduating class of 2020
    python listmanager.py germany.xlsx 2020
    
    # Export list of names to a file suitable for LISTSERV bulk subscription:
    python listmanager.py germany.xlsx 2020 > germany_2020.txt


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
[venv]: https://docs.python.org/3/library/venv.html
[Pandas]: http://pandas.pydata.org/pandas-docs/stable/index.html
[openpyxl]: http://openpyxl.readthedocs.io/en/latest/index.html
