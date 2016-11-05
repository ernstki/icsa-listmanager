#!/usr/bin/env python
##########################################################################
##                                                                      ##
##   listmanager.py                                                     ##
##                                                                      ##
##   Generate a list of names and emails from an Excel (OOXML .xlsx)    ##
##   workbook that's in a suitable format for LISTSERV's bulk           ##
##   subscription function.                                             ##
##                                                                      ##
##   Author:   Kevin Ernst <ernstki@mail.uc.edu>                        ##
##   Date:     05 November 2016                                         ##
##                                                                      ##
##   References:                                                        ##
##                                                                      ##
##     1. http://pandas.pydata.org/pandas-docs/stable/index.html        ##
##     2. http://openpyxl.readthedocs.io/en/latest/index.html           ##
##                                                                      ##
##   Sample Usage:                                                      ##
##                                                                      ##
##     python workbook.xlsx 2020                                        ##
##                                                                      ##
##########################################################################

import os
import sys
import click

from openpyxl import load_workbook
from pandas import DataFrame


def print_members(excelfile, year=None):
    """
    Print out the list of members from the 'Master List' tab in a format
    that's suitable for bulk import into LISTSERV
    """
    wb = load_workbook(excelfile)

    # Look for a sheet named "Master (something)" or bail out
    masterlist = [s for s in wb.get_sheet_names() if "Master" in s]
    if not masterlist:
        raise RuntimeError("'Master' tab not found in spreadsheet")

    ws = wb.get_sheet_by_name(masterlist[0])
    data = ws.values

    # Skip over any empty rows, then save off the column headers
    cols = next(data)
    while not cols[0]:
        cols = next(data)

    # Load data into a Pandas DataFrame for further manipulation
    df = DataFrame(data, columns=cols)

    if year:
        for p in df[df['Class Year'] == year][['Name', 'Email']].itertuples():
            # If, for some odd reason, the DataFrame has 'None's at the end
            if p.Name is None: break
            print "%s <%s>" % (p.Name.title(), p.Email)
    else:
        for p in df[['Name', 'Email']].itertuples():
            if p.Name is None: break
            print "%s <%s>" % (p.Name.title(), p.Email)


@click.command()
@click.argument('excelfile', type=click.Path(exists=True))
@click.argument('year', type=click.INT, required=False)
def read_workbook(excelfile, year=None):
    """Open .xlsx workbook and print names and emails"""
    print_members(excelfile, year)


if __name__ == '__main__':
    read_workbook()


