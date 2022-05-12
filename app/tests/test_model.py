from app.models.fornecedor_model import FornecedorModel
from app.models.produto_model import ProdutoModel
from app.models.comprador_model import CompradorModel
from app.models.compra_model import CompraModel
from uuid import uuid4

class TesteModel():

    forncedor_uuid = uuid4()
    produto_uuid = uuid4()
    comprador_uuid = uuid4()

    def test_model_fornecedor(self):
        fornecedor_data = {
        'nome': "Bob's Pizza",
        "endereco":'987 Fake St'
        }

        fornecedor = FornecedorModel(**fornecedor_data)
        self.forncedor_uuid = fornecedor.id
        assert fornecedor.nome == "Bob's Pizza"
        assert fornecedor.endereco == '987 Fake St'
    
    def test_model_produto(self):
        produto_data = {
           'descricao': 'R$10 off R$20 of food',
           'preco_unidade':float('10.0'),
           'forncedor_id':self.forncedor_uuid
        }

        produto = ProdutoModel(**produto_data)
        self.produto_uuid = produto.id
        assert produto.descricao == 'R$10 off R$20 of food'
        assert produto.preco_unidade == float('10.0')
        assert produto.forncedor_id == self.forncedor_uuid


    def test_model_comprador(self):
        comprador_data = {
            'nome':'João Silva'
        }

        comprador = CompradorModel(**comprador_data)
        self.comprador_uuid=comprador.id
        assert comprador.nome == 'João Silva'
    
    def test_model_compra(self):
        compra_data={
            'quantidade': int('4'),
            'produto_id': self.produto_uuid,
            'comprador_id':self.comprador_uuid
        }

        compra=CompraModel(**compra_data)
        assert compra.quantidade == int('4')
        assert compra.produto_id == self.produto_uuid
        assert compra.comprador_id == self.comprador_uuid
