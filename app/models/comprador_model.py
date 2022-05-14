from dataclasses import dataclass
from uuid import uuid4

from app.configs.database import db
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID


@dataclass
class CompradorModel(db.Model):
    id:UUID
    nome:str

    __tablename__ = 'comprador'

    id=Column(UUID(as_uuid=True),primary_key=True,default=uuid4)
    nome=Column(String)
    