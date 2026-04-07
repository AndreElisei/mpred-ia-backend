from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS

from model import Session
from model.equipamento import Equipamento

from schemas import EquipamentoSchema

info = Info(title="MPred-IA API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


@app.get('/')
def home():
    return {"message": "API funcionando"}


@app.post('/equipamento')
def add_equipamento(form: EquipamentoSchema):
    session = Session()

    equipamento = Equipamento(
        nome=form.nome,
        tipo=form.tipo,
        tag=form.tag
    )

    session.add(equipamento)
    session.commit()

    return {"message": "Equipamento cadastrado"}


@app.get('/equipamentos')
def get_equipamentos():
    session = Session()
    equipamentos = session.query(Equipamento).all()

    lista = []
    for e in equipamentos:
        lista.append({
            "id": e.id,
            "nome": e.nome,
            "tipo": e.tipo,
            "tag": e.tag
        })

    return {"equipamentos": lista}