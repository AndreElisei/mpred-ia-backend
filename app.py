from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS
from flask import jsonify

from model import Session
from model.equipamento import Equipamento

from model.anomalia import Anomalia
from schemas import AnomaliaSchema
from schemas.delete import EquipamentoIdPath
from schemas import EquipamentoSchema

info = Info(title="MPred-IA API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response

@app.get('/')
def home():
    return {"message": "API funcionando"}, 200


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

    return {
    "id": equipamento.id,
    "nome": equipamento.nome,
    "tipo": equipamento.tipo,
    "tag": equipamento.tag
    }, 201

@app.get('/equipamentos')
def get_equipamentos():
    session = Session()
    equipamentos = session.query(Equipamento).order_by(Equipamento.id).all()

    lista = []
    for e in equipamentos:
        lista.append({
            "id": e.id,
            "nome": e.nome,
            "tipo": e.tipo,
            "tag": e.tag,
            "anomalias":[
                {
                    "id": a.id,
                    "descricao": a.descricao,
                    "status": a.status
                } for a in e.anomalias
            ]
        })
    return {"equipamentos": lista}, 200


@app.post('/anomalia')
def add_anomalia(form: AnomaliaSchema):
    session = Session()

    equipamento = session.query(Equipamento).filter(Equipamento.id == form.equipamento_id).first()

    if not equipamento:
        return {"message": "Equipamento não encontrado"}, 404

    anomalia = Anomalia(
        descricao=form.descricao,
        status=form.status,
        equipamento_id=form.equipamento_id
    )

    session.add(anomalia)
    session.commit()

    return {
        "id": anomalia.id,
        "descricao": anomalia.descricao,
        "status": anomalia.status,
        "equipamento_id": anomalia.equipamento_id
    }, 201

@app.delete('/equipamento/<int:id>')
def delete_equipamento(path: EquipamentoIdPath):
    session = Session()

    equipamento = session.query(Equipamento).filter(Equipamento.id == path.id).first()

    if not equipamento:
        return {"message": "Equipamento não encontrado"}, 404

    session.delete(equipamento)
    session.commit()

    return {"message": "Equipamento removido"}, 200
