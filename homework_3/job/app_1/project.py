from flask import Flask, render_template, request, make_response, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from models import db, User
from logging import getLogger as Logger
from registration_form import RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
logger = Logger(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'
db.init_app(app)
csrf = CSRFProtect(app)

# hash = generate_password_hash("12345")
# check_password_hash(hash, "12345")

@app.cli.command("init-db")
def init_db():
  db.create_all()
  print('OK')


@app.get('/')
def home():
  context = {'users': User.query.all()}
  return render_template('home.html', **context)


@app.route('/register/', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()

  if request.method == 'POST' and form.validate():
    user = User(
      full_name=form.full_name.data,
      e_mail=form.e_mail.data,
      password=generate_password_hash(form.password.data)
    )
    db.session.add(user)
    db.session.commit()

    response = make_response(redirect(url_for('home')))
    flash('SignUp was successfully!', 'success')
    return response
  else:
    return render_template('register.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
  logger.warning(e)

  context = {
    'title': 'Page not found =(',
    'url': request.referrer,
  }
  return render_template('404.html', **context), 404
