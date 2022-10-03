from email.mime import base
from fastapi import FastAPI
from pydantic import BaseModel #facilita e estiliza a passagem de parâmetros

app = FastAPI()   #realiza a inicialização da API
# Rota Raiz
@app.get("/")
def raiz():
    return{"Olá": "Mundo"}

# Modelo
class Usuario(BaseModel):
    id: int
    email: str
    senha: str
# Base de dados

base_de_dados = [
    Usuario(id=1, email="fernandoccfelipe@gmail.com", senha="fernando123"),
    Usuario(id=2, email="fulano@gmail.com", senha="fulano123")
]

# Rota Get ALL
@app.get("/usuarios") #endpoint usuários
def get_todos_os_usuarios():
    return base_de_dados

# Rota GET ID

@app.get("/usuarios/{id_usuario}")
def get_by_id(id_usuario: int):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return usuario
    
    return{"Erro": 404, "Mensagem": "Usuário não encontrado"}   ##else não é necessário

# Rota para inserir novo usuário

@app.post("/usuarios")
def insere_usuario(usuario: Usuario):
    base_de_dados.append(usuario) #append >> insere um novo objeto
    return usuario