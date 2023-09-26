


# При отправке формы данные должны валидироваться на следующие условия:
# Все поля обязательны для заполнения.

# - Поле email должно быть валидным email адресом.
# - Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и одну цифру.
# - Поле подтверждения пароля должно совпадать с полем пароля.
# - Если данные формы не прошли валидацию, на странице должна быть выведена соответствующая ошибка.
# - Если данные формы прошли валидацию, на странице должно быть выведено сообщение об успешной регистрации

from flask import (Flask, render_template, url_for, request, redirect)
from models.models import db, Forma
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


# все методы "cli" запускаются из cmd по средствам flask
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        form = Forma(name=request.form.get('name'),
                     email=request.form.get('email'),
                     password=request.form.get('password'),
                     date_birthday=datetime.strptime(request.form.get('date'), '%Y-%m-%d'))
        db.session.add(form)
        db.session.commit()
        return redirect(url_for('form_completed'))
    return render_template('form.html')


@app.route('/form_completed/')
def form_completed():
    return render_template('form_completed.html')


if __name__ == '__main__':
    app.run(debug=True)