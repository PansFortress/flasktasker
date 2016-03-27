import os

# grab the folder where the script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktasker.db'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'A967382E524649E2DD9DD227D4582'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+DATABASE_PATH
DEBUG = True