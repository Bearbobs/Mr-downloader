from setuptools import setup
import py2exe
from glob import glob

SETUP_DICT = {
    'windows': [{
        'script': 'dm.py',
    }],

    'zipfile': 'lib/library.zip',

    'data_files': (
        ('', glob(r'C:\Windows\SYSTEM32\msvcp100.dll')),
        ('', glob(r'C:\Windows\SYSTEM32\msvcr100.dll')),
    ),

    'options': {
        'py2exe': {
            'bundle_files': 3,
            'includes': ['sip', 'PyQt4.QtGui','PyQt4.QtCore','sys','urllib'],
        },
    }
}

setup(**SETUP_DICT)