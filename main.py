from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
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
