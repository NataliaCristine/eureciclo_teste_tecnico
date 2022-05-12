from flask import Flask
from environs import Env
from app import views

def create_app():
    
    env=Env()
    env.read_env()

    app = Flask(__name__)
    views.init_app(app)

    return app