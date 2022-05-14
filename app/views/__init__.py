from .view_file import file_save
def init_app(app):
    file_save(app)
    return app