from sqlalchemy import Column, String, Integer, ForeignKey
from model import Base

class Anomalia(Base):
    __tablename__ = 'anomalia'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(400))
    status = Column(String(50))

    equipamento_id = Column(Integer, ForeignKey("equipamento.id"))