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

You'll need [Python][] and [pip][]. On a modern OS (Python > 2.7.9), `pip`
_should_ already be installed and in your exectuable search path (`$PATH` on
Unix and `%PATH%` on Windows).

Do this in a terminal and cross your fingers:

```bash
# in the directory where you cloned / downloaded this project...
cd icsa-listserv
pip install --user .
```

On Windows, `sudo` isn't necessary. That's a Unix thing. However, there's
a good chance that you'll get a message like `'pip' is not recognized as an
internal or external command`, and in that case you'll want to add these
paths (separated by semicolons) to your `PATH` environment variable:

```
C:\Python<VER>
C:\Python<VER>\Scripts
C:\Users\<USER>\AppData\Roaming\Python\Scripts (for 'pip install --user')
```
([instructions][envvars])

Replace `<VER>` with your actual Python version, _e.g._, `Python27` or
`Python35` and `<USER>` with your actual Windows username. Some of these may
have been added for you by the Python installer, if you're lucky.

## Usage

You should end up with a script called `listmanager` in your `PATH`, which you
can execute from anywhere on the system. If you type this in and get some
variation on a "command not found" error, try one of the alternatives
mentioned in [the wiki][wiki]. In a pinch, you can invoke the script with
`python listmanager.py [options]` while you're inside the `icsa-listmanager`
directory.

The script has rudimentary built-in help, which you can reference with
`listmanager --help`. But here are the basics:

```
# All names & emails on all tabs (all graduating years)
listmanager germany.xlsx

# Or for only those students in the graduating class of 2020
listmanager germany.xlsx 2020

# Export list of names to a file suitable for LISTSERV bulk subscription:
listmanager germany.xlsx 2020 > germany_2020.txt
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
[Pandas]: http://pandas.pydata.org/pandas-docs/stable/index.html
[openpyxl]: http://openpyxl.readthedocs.io/en/latest/index.html
[envvars]: http://www.computerhope.com/issues/ch000549.htm
[wiki]: https://github.uc.edu/ernstki/icsa-listmanager/wiki
