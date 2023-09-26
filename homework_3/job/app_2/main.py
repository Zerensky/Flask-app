# 📌 Доработаем задача про студентов<br>
# 📌 Создать базу данных для хранения информации о студентах и их оценках в
# учебном заведении.<br>
# 📌 База данных должна содержать две таблицы: "Студенты" и "Оценки".
# 📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
# и email.<br>
# 📌 В таблице "Оценки" должны быть следующие поля: id, id студента, название
# предмета и оценка.<br>
# 📌 Необходимо создать связь между таблицами "Студенты" и "Оценки".<br>
# 📌 Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их оценок.

from flask import Flask, render_template
from models.models import db, Student, Grades
from random import randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


# все методы "cli" запускаются из cmd по средствам flask
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_tables():
    list_lesson = ['mathematic', 'phisical', 'history']
    count = 10
    # Добавляем Студента
    for student in range(1, count + 1):
        group_rnd = randint(1, 4)

        db.session.add(
            Student(name=f'name_{student}',
                    surname=f'surname_{student}',
                    group=f'group - {group_rnd}',
                    email=f'name{student}@mail.ru'))
        db.session.commit()

        # Добавляем оценки
    for grades in range(1, count + 1):
        db.session.add(
            Grades(
                student_id=f'{grades}',
                lesson_name=f'lesson_{list_lesson[randint(0, 2)]}',
                grade=f'{randint(2, 5)}',
            ))
        db.session.commit()
    print('OK')


@app.route('/')
def hello():
    context = {'grades': Grades.query.all()}
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run(debug=True)