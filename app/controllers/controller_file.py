from flask import Flask
import os
from uuid import uuid4
import csv

def file_upload_save(data):

    paths = ''
    dados_list=[]
    
    for key,item in data.items():
        extension = item.filename.split('.')[1]
        paths= f'app/file/ar{uuid4()}.{extension}'
        item.save(paths)

        with open(paths) as file_data:
            data_reade = csv.DictReader(file_data,delimiter='\t')
            for line in data_reade:
                dados_list.append(dict(line))
    

