from flask import Flask
import os
from uuid import uuid4

def file_upload_save(data):
    
    paths = ''
    
    for key,item in data.items():
        extension = item.filename.split('.')[1]
        paths= f'app/file/ar{uuid4()}.{extension}'
        item.save(paths)
