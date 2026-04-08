from sqlalchemy import Column, String, Integer, ForeignKey
from pydantic import BaseModel
from model import Base

class Anomalia(Base):
    __tablename__ = 'anomalia'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(400))
    status = Column(String(50))

    equipamento_id = Column(Integer, ForeignKey("equipamento.id"))

    def __init__(self, descricao, status, equipamento_id):
        self.descricao = descricao
        self.status = status
        self.equipamento_id = equipamento_id

class AnomaliaSchema(BaseModel):
    descricao: str
    status: str
    equipamento_id: int