from flask import Flask
from environs import Env
from app import views

def create_app():
    
    env=Env()
    env.read_env()

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI']=env('SQLALCHEMY_DATABASE_URI')
    app.config['SQLACHEMY_TRACK_MODIFICATIONS']=False
    app.config['JSON_SORT_KEYS'] = False

    views.init_app(app)

    return app