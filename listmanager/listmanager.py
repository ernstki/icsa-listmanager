import click
from config import Config
from excelreader import ExcelReader

config = Config()

@click.command()
@click.argument('excelfile', type=click.Path(exists=True))
@click.argument('year', type=click.INT, required=False)
def read_workbook(excelfile, year=None):
    """Open .xlsx workbook and print names and emails in a format that LISTSERV
    understands"""
    xlr = ExcelReader(excelfile)
    xlr.print_members(year)

if __name__ == '__main__':
    read_workbook()
