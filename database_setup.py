from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students_database.db'
db = SQLAlchemy(app)

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    amount_due = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

    # Check if the database is empty before adding initial data
    if Student.query.count() == 0:
        initial_students = [
            Student(first_name='Paul', last_name='Rogers', dob=datetime.strptime('2000-02-25', '%Y-%m-%d'), amount_due=1000.0),
            Student(first_name='Chris', last_name='Evans', dob=datetime.strptime('1998-06-15', '%Y-%m-%d'), amount_due=1500.0),
            Student(first_name='Tony', last_name='Stark', dob=datetime.strptime('2001-04-10', '%Y-%m-%d'), amount_due=2000.0)
        ]

        # Add and commit the initial data
        db.session.bulk_save_objects(initial_students)
        db.session.commit()
