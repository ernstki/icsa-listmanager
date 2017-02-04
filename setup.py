from setuptools import setup

setup(
    name='listmanager',
    version='0.1',
    py_modules=[
        'config',
        'excelreader',
        'mailhandler',
    ],
    install_requires=[
        'Click',
        'openpyxl',
        'pandas',
    ],
    entry_points='''
        [console_scripts]
        listmanager=excelreader.excelreader:read_workbook
    ''',
)
