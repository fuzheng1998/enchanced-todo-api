from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

App = Flask(__name__)
Api = Api(App)
# path at /tmp/test.db
App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
Db = SQLAlchemy(App)