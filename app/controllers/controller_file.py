
import csv
from uuid import uuid4

from app.repositories import Repository


def open_file(path):
       
    with open(path) as data:
        data_reader = csv.DictReader(data,delimiter='\t')
        for line in data_reader:
            comprador ={'nome':line['Comprador']}
            new_comprador = Repository.comprador_save(comprador)
            fornecedor ={
                'nome': line['Fornecedor'],
                'endereco':line['Endereço']
            }
            new_fornecedor = Repository.fornecedor_save(fornecedor)
            produto = {
                'descricao':line['Descrição'],
                'preco_unidade':line['Preço Unitário'],
                'forncedor_id':new_fornecedor['id']
            }
            new_produto = Repository.produto_save(produto)
            compra = {
                'quantidade':line['Quantidade'],
                'produto_id':new_produto['id'],
                'comprador_id':new_comprador['id']
            }
            new_compra = Repository.compra_save(compra)
    output = Repository.get_all()

    return output


def file_upload_save(data):
    try:
        for key,item in data.items():
            extension = item.filename.split('.')[1]
            if not extension == 'txt':
                    return {"Erro":"Extensão não suportada"},415
            paths= f'app/file/ar{uuid4()}.{extension}'
            item.save(paths)
            output = open_file(paths)
    except IndexError:
        return {"Erro":"Arquivo não enviado"},400

    return output
    

def list_all():
    output = Repository.get_all()

    return output
