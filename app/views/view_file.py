from app.controllers import file_upload_save, list_all
from flask import render_template, request


def file_save(app):
    @app.route('/')
    def form_upload():
        return render_template('upload.html')

    @app.route('/register',methods = ['GET', 'POST'])
    def file_save():
        if request.method == 'POST':
            data = request.files
            output=file_upload_save(data)
            if type(output[0]) == dict:
                return render_template('erro.html', output=output)
            return render_template('tabela.html', output=output)
        
        output = list_all()
        return render_template('tabela.html', output=output)
