from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from models.produto_model import Produto
from repositories import produto_repo
from util import obter_conexão
import uvicorn

#Criação do objeto FastAPI
app = FastAPI()

#Configuração do objeto templates, mapeando para a pasta "templates"
templates = Jinja2Templates(directory="templates") 

#Configuração da pasta de arquivos estáticos, mapeando para a pasta "static"
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
 uvicorn.run("main:app", port=8000, reload=True)

@app.route('/cadastro')
def cadastro():
    return templates.TemplateResponse('cadastro.html', titulo='Cadastro de Produto')

app.route('/post_cadastro', methods=['POST'])
def post_cadastro(request: Request,
                  nome: str = Form(...),
                  descricao: str = Form(...),
                  estoque: str = Form(...),
                  preco: str = Form(...),
                  categoria: str = Form(...)):
                  
                  produto = Produto(nome=nome, descricao=descricao, estoque=estoque, preco=preco, categoria=categoria)

                  conexao = obter_conexão()

                  try:
                     #Inserindo o Produto no banco
                     produto_repo.inserir(conexao, produto)
                     return RedirectResponse(url="/cadastro_recebido", status_code=303)
                  except Exception as i:
                        print(f'Erro ao inserir produto: {i}')
                  return RedirectResponse(url="/cadastro", status_code=303)

@app.get("/cadastro_recebido")
def cadastro_recebifo(request: Request):
      return templates.TemplateResponse("cadastro_recebido.html", {"request": request})