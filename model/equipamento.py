from sqlalchemy import Column, String, Integer
from model import Base

class Equipamento(Base):
    __tablename__ = 'equipamento'

    id = Column(Integer, primary_key=True)
    nome = Column(String(140))
    tipo = Column(String(50))
    tag = Column(String(50))

    def __init__(self, nome, tipo, tag):
        self.nome = nome
        self.tipo = tipo
        self.tag = tag