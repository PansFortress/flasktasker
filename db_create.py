from views import db
from models import Task
from datetime import date


# Create the database and tables
db.create_all()

# Insert data
db.session.add(Task("Finish this tutorial", date(2016, 3, 13), 1, 1))
db.session.add(Task("Grab bike", date(2016, 3, 19), 2, 1))

# Commit the changes
db.session.commit()
