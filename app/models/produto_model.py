from dataclasses import dataclass
from uuid import uuid4

from app.configs.database import db
from app.models import FornecedorModel
from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref, relationship


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

    


    