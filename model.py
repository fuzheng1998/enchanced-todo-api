from config import *


class User(Db.Model):
    id = Db.Column(Db.Integer, primary_key=True)
    username = Db.Column(Db.String(80), unique=True, nullable=False)
    email = Db.Column(Db.String(120), unique=True, nullable=False)
    password = Db.Column(Db.String(255),nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Todo(Db.Model):
    id = Db.Column(Db.Integer, primary_key=True)
    task = Db.Column(Db.String(120), nullable=False)
    user_id = Db.Column(Db.Integer, Db.ForeignKey("user.id"))
    user = Db.relationship('User',
                           backref=Db.backref('todos', lazy=True))

    def __repr__(self):
        return '<Todo %r>' % self.task
