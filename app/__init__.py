from environs import Env
from flask import Flask

from app import views
from app.configs import database, migrations


def create_app():
    
    env=Env()
    env.read_env()

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI']=env('SQLALCHEMY_DATABASE_URI')
    app.config['SQLACHEMY_TRACK_MODIFICATIONS']=False
    app.config['JSON_SORT_KEYS'] = False

    views.init_app(app)
    database.init_app(app)
    migrations.init_app(app)

    return app
