# MPred-IA Backend

## 📌 Descrição

API REST desenvolvida em Python com Flask para gerenciamento de equipamentos industriais e suas anomalias, com foco em manutenção preditiva.

Permite cadastrar, listar e remover equipamentos, além de registrar anomalias associadas.

---

## 🚀 Tecnologias utilizadas

* Python
* Flask
* Flask-OpenAPI3
* SQLAlchemy
* SQLite
* Flask-CORS

---

## ⚙️ Funcionalidades

* Cadastro de equipamentos
* Listagem de equipamentos
* Cadastro de anomalias
* Relacionamento entre equipamentos e anomalias
* Remoção de equipamentos
* Documentação automática com Swagger

---

## 📂 Estrutura do projeto

```
backend/
│── model/
│── schemas/
│── database/
│── app.py
│── requirements.txt
```

---

## 🔧 Instalação e execução

### 1. Clonar o repositório

```
git clone https://github.com/seu-usuario/mpred-ia-backend.git
cd mpred-ia-backend
```

### 2. Criar ambiente virtual

```
python -m venv venv
```

### 3. Ativar ambiente

**Windows:**

```
venv\Scripts\activate
```

### 4. Instalar dependências

```
pip install -r requirements.txt
```

### 5. Executar aplicação

```
flask run
```

---

## 📚 Documentação da API

Disponível em:

```
http://127.0.0.1:5000/openapi
```

---

## 🔗 Rotas principais

| Método | Rota              | Descrição            |
| ------ | ----------------- | -------------------- |
| GET    | /equipamentos     | Lista equipamentos   |
| POST   | /equipamento      | Cadastra equipamento |
| POST   | /anomalia         | Cadastra anomalia    |
| DELETE | /equipamento/{id} | Remove equipamento   |

---

## 📌 Observações

Projeto desenvolvido como MVP para a Pós-Graduação em Desenvolvimento Full Stack da PUC-Rio.
