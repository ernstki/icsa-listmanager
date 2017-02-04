from setuptools import setup

setup(
    name='listmanager',
    version='0.2',
    py_modules=[
        'listmanager.config',
        'listmanager.excelreader',
        'listmanager.mailhandler',
    ],
    install_requires=[
        'Click',
        'openpyxl',
        'pandas',
        'pytest',
    ],
    entry_points='''
        [console_scripts]
        listmanager=listmanager.listmanager:read_workbook
    ''',
)
