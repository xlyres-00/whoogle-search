import os

optional_dev_tag = ''
if os.getenv('DEV_BUILD'):
    optional_dev_tag = '.dev' + os.getenv('DEV_BUILD')

__version__ = '0.9.4' + optional_dev_tag
