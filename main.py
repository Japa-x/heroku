from email.mime import base
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

#rota raiz
@app.get("/")
def raiz():
    return {"Olá": "Mundo"}

# Criar model
class Usuario(BaseModel):
    id: int 
    email: str
    senha: str

#criar base de dados

base_de_dados = [
    Usuario(id=1, email="matheus@hotmail.com", senha= "matheus123"),
    Usuario(id=2, email="evelin@hotmail.com", senha= "evelin123")
]

# rota get all
@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados

# rota get id
@app.get("/usuarios/{id_usuarios}")
def get_usuario_usando_id(id_usuario: int):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return usuario

    return {"Status": 404, "Mensage": "Não encontrou usuário"}

# criar usuario
@app.post("/usuarios")
def intere_usuario(usuario: Usuario):
    base_de_dados.append(usuario)
    return usuario