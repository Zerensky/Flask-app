import os
import random

from flask import Flask, render_template
from task1.models import db, Student, Faculty

app = Flask(__name__)
app.secret_key = b"5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4"

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///mydatabase.db"
db.init_app(app)


@app.route("/")
def index():
    return "hello"


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.cli.command("test-data")
def add_test_data():
    count = 5
    for i in range(1, count + 1):
        faculty = Faculty(name=f"faculty{i}")
        db.session.add(faculty)
        for j in range(1, 3):
            student = Student(
                first_name=f"name{i}{j}",
                last_name=f"surname{i}{j}",
                age=random.randint(18, 25),
                group=2,
                gender=random.choice("муж", "жен"),
                faculty_id=i,
            )
            db.session.add(student)
    db.session.commit()
    print("данные добавлены")


@app.route("/students")
def all_students():
    students = Student.query.all()
    context = {"students": students}
    return render_template("books.html", **context)


if __name__ == "__main__":
    db.create_all()
    add_test_data()
    app.run(debug=True)
