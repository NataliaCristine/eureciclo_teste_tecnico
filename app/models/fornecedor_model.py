from dataclasses import dataclass
from uuid import uuid4

from app.configs.database import db
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID


@dataclass
class FornecedorModel(db.Model):
    id:UUID
    nome:str
    endereco:str

    __tablename__= 'fornecedor'

    id= Column(UUID(as_uuid=True),primary_key=True, default=uuid4)
    nome= Column(String)
    endereco=Column(String)

    