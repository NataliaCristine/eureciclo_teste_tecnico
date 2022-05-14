from flask import current_app
from app.models import CompradorModel,FornecedorModel,ProdutoModel,CompraModel


class Repository():
    
    @staticmethod
    def comprador_save(dados):
        new_comprador = CompradorModel(**dados)
        current_app.db.session.add(new_comprador)
        current_app.db.session.commit()
        id = new_comprador.id
        comprador = CompradorModel.query.get(id)

        return comprador.__dict__

    def fornecedor_save(dados):

        fornecedor = FornecedorModel.query.filter_by(nome=dados['nome']).first()
        if not fornecedor:
            new_fornecedor = FornecedorModel(**dados)
            current_app.db.session.add(new_fornecedor)
            current_app.db.session.commit()
            fornecedor = FornecedorModel.query.filter_by(nome=dados['nome']).first()

    
        return fornecedor.__dict__

    def produto_save(dados):
        new_produto = ProdutoModel(**dados)
        current_app.db.session.add(new_produto)
        current_app.db.session.commit()
        id = new_produto.id
        produto = ProdutoModel.query.get(id)

        return produto.__dict__

    def compra_save(dados):
        new_compra = CompraModel(**dados)
        current_app.db.session.add(new_compra)
        current_app.db.session.commit()

        return new_compra

    def get_all():
        compra = CompraModel.query.all()
        output =[]
        total = 0
        cont = 0

        while cont < len(compra):
            total= total+(compra[cont].produto.preco_unidade * compra[cont].quantidade)
            
            output.append({"Comprador":compra[cont].comprador.nome,"Descrição":compra[cont].produto.descricao,"Preço Unitário":compra[cont].produto.preco_unidade,"Quantidade":compra[cont].quantidade,"Endereço":compra[cont].produto.fornecedor.endereco,"Fornecedor":compra[cont].produto.fornecedor.nome})
            cont += 1

        return (output,total)