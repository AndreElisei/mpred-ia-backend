from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from model import Base

class Equipamento(Base):
    __tablename__ = 'equipamento'

    id = Column(Integer, primary_key=True)
    nome = Column(String(140))
    tipo = Column(String(50))
    tag = Column(String(50))

    anomalias = relationship("Anomalia")

    def __init__(self, nome, tipo, tag):
        self.nome = nome
        self.tipo = tipo
        self.tag = tag