import os

# grab the folder where the script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktasker.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'A967382E524649E2DD9DD227D4582'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

DEBUG = True