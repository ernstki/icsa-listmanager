"""
Generate a list of names and emails from an Excel (OOXML .xlsx) workbook that's
in a suitable format for LISTSERV's bulk subscription function.

References:

  1. http://pandas.pydata.org/pandas-docs/stable/index.html
  2. http://openpyxl.readthedocs.io/en/latest/index.html
"""
import os
import sys
import re
import warnings

from openpyxl import load_workbook
from pandas import DataFrame


class ExcelReader:
    """
    Excel spreadsheet reader class. Loads .xlsx file given as the first
    argument to the constructor and creates a Pandas dataframe with which to
    access the class roster data.
    """
    roster = {}

    def __init__(self, excelfile):
        """
        Open workbook given as argument, look for sheets that end in "20xx"
        and store their contents on a dictionary of DataFrames, with the
        graduating years as (string) keys
        """
        p = re.compile('.*(20\d\d)$')

        # reference:
        # https://docs.python.org/2/library/warnings.html#temporarily-suppressing-warnings
        with warnings.catch_warnings() as w:
            warnings.filterwarnings('ignore', 'Unknown extension')
            wb = load_workbook(excelfile)

        for sheet in wb.get_sheet_names():
            m = p.match(sheet)
            if not m: continue
            data = wb.get_sheet_by_name(sheet).values
            # Skip over any empty rows, then save off the column headers
            cols = next(data)
            while not cols[0]:
                cols = next(data)
            # Store data in dictionary as a Pandas DataFrame
            self.roster[m.group(1)] = DataFrame(data, columns=cols)

        if not self.roster.keys():
            raise RuntimeError("No tabs matching '20xx' found in spreadsheet")

    def print_members(self, year=None):
        """
        Print out the list of members from the all worksheet tabs with a name
        matching "<Something> 20xx" in a format that's suitable for bulk
        import into LISTSERV

        TODO: Allow printing in sorted order
        """
        if year:
            years = [str(year)]
        else:
            years = self.roster.keys()

        for year in years:
            df = self.roster[year]
            for p in df[['Name', 'Email']].itertuples():
                if p.Name is None: break
                print("{} <{}>".format(p.Name.title(), p.Email))
