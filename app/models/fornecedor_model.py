from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, String
from uuid import uuid4
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

    