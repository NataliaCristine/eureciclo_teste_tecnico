from flask import Flask, request, render_template
from app.controllers.controller_file import file_upload_save

def file_save(app):
    @app.route('/upload')
    def form_upload():
        render_template()

    @app.route('/register',methods = ['GET', 'POST'])
    def file_save():
        if request.method == 'POST':
            data = request.files
            output=file_upload_save(data)
