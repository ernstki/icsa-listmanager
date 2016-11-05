## List management with Python

The `listmanager.py` script included in this repository will extract names and
emails from an Excel (OOXML `.xlsx` format) spreadsheet and print them in the
format expected by LISTSERV for bulk import, _i.e._:

    First Last <email@domain.com>

This script is intended to be used to make updates easier

# Installation

## Install Python, `pip`, and `virtualenv`

You'll need [Python][] and [pip][]. On a modern OS (Python > 2.7.9), `pip`
will already be installed.

You'll then want to install [virtualenv][] globally, with `pip`, like this:

    sudo pip install virtualenv

or install the `virtualenv` package through your OS's package manager (_e.g._,
`apt-get` or `yum` for Linux, MacPorts or Homebrew on Mac).

On Windows, `sudo` isn't necessary. That's a Unix thing. If you have trouble,
refer to the `virtualenv` [installation documentation][venv]

## Install Pandas and openpyxl

# Usage

The script has rudimentary built-in help, which you can reference with `python
listmanager.py --help`. But here are the basics:

```
# For all names
python listmanager.py germany 2020

# Or for *all* names in the "German Master List" sheet:
python listmanager.py germany

# Redirect into a file for uploading to LISTSERV
python listmanager.py germany 2020 > germany_2020.txt
```

# References

* [Pandas][]
* [openpyxl][]


[python]: https://www.python.org/downloads/
[pip]: https://pip.pypa.io/en/stable/installing/
[venv]: https://virtualenv.pypa.io/en/stable/installation/
[Pandas]: http://pandas.pydata.org/pandas-docs/stable/index.html
[openpyxl]: http://openpyxl.readthedocs.io/en/latest/index.html
