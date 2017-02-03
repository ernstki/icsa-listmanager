from setuptools import setup

setup(
    name='listmanager',
    version='0.1',
    py_modules=['xlreader'],
    install_requires=[
        'Click',
        'openpyxl',
        'pandas',
    ],
    entry_points='''
        [console_scripts]
        listmanager=xlreader.xlreader:read_workbook
    ''',
)
