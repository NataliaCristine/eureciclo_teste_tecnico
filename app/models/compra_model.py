from dataclasses import dataclass
from uuid import uuid4

from app.configs.database import db
from app.models import CompradorModel, ProdutoModel
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref, relationship


@dataclass
class CompraModel(db.Model):
    id:UUID
    produto:ProdutoModel
    comprador:CompradorModel
    quantidade:int

    __tablename__ = 'compra'

    id=Column(UUID(as_uuid=True),primary_key=True,default=uuid4)
    quantidade=Column(Integer)
    produto_id = Column(UUID(as_uuid=True),ForeignKey('produto.id'))
    comprador_id = Column(UUID(as_uuid=True),ForeignKey('comprador.id'))
    
    produto= relationship("ProdutoModel", backref=backref('produto',uselist=False))
    comprador=relationship("CompradorModel", backref=backref('comprador',uselist=False))



