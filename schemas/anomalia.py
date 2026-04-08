from pydantic import BaseModel

class AnomaliaSchema(BaseModel):
    descricao: str
    status: str
    equipamento_id: int