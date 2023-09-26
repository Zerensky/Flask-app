from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Forma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False,  unique=True)
    password = db.Column(db.String(50) , nullable=False)
    date_birthday = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'Name - ({self.name}), email - ({self.email})'
