from app.configs.database import db
from dataclasses import dataclass 
from uuid import uuid4
from sqlalchemy import Column,Integer,ForeignKey
from sqlalchemy.orm import backref,relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.produto_model import ProdutoModel
from app.models.comprador_model import CompradorModel

@dataclass
class CompraModel(db.Model):
    id:UUID
    produto:ProdutoModel
    comprador:CompradorModel
    quantidade:int

    __tablename__ = 'compra'

    id=Column(UUID(as_uuid=True),primary_key=True,default=True)
    quantidade=Column(Integer)
    produto_id = Column(UUID(as_uuid=True),ForeignKey('produto.id'))
    comprador_id = Column(UUID(as_uuid=True),ForeignKey('comprador.id'))
    
    produto= relationship("ProdutoModel", backref=backref('produto',uselist=False))
    comprador=relationship("CompradorModel", backref=backref('comprador',uselist=False))



