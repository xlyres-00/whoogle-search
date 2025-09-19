import os

optional_dev_tag = ''
if os.getenv('DEV_BUILD'):
    optional_dev_tag = '.dev' + os.getenv('DEV_BUILD')

<<<<<<< HEAD
__version__ = '0.9.3' + optional_dev_tag
=======
__version__ = '0.9.4' + optional_dev_tag
>>>>>>> 2c5adbc (Initial upload: Whoogle app (excluding connection-api))
