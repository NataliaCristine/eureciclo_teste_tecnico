from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4
from sqlalchemy import Column, String,Float,ForeignKey
from sqlalchemy.orm import backref,relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.fornecedor_model import FornecedorModel

@dataclass
class ProdutoModel(db.Model):
    id:UUID
    descricao:str
    preco_unidade:float
    fornecedor:FornecedorModel

    __tablename__ = 'produto'

    id=Column(UUID(as_uuid=True),primary_key=True,default=uuid4)
    descricao=Column(String)
    preco_unidade=Column(Float)
    forncedor_id = Column(UUID(as_uuid=True),ForeignKey('fornecedor.id'))

    fornecedor= relationship("FornecedorModel",backref=backref('fornecedor',uselist=False))

    


    