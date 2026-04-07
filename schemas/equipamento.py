from pydantic import BaseModel

class EquipamentoSchema(BaseModel):
    nome: str
    tipo: str
    tag: str