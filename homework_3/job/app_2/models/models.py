from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False,  unique=True)
    
    students = db.relationship('Grades', backref='student', lazy=True)

    def __repr__(self):
        return f'student ({self.username} {self.name}), group - {self.group}'


class Grades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    lesson_name = db.Column(db.String(120), nullable=False)
    grade = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.lesson_name} - {self.grade}'