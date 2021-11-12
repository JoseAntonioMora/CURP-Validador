from fastapi import FastAPI
from starlette.responses import Response
from v1.api import Validador
from fastapi.encoders import jsonable_encoder

description = """
CURP Validador ayuda a validar la Clave Unica de Resgistro a la Poblacion de México. 🚀

## CURP

Regresa la información en formato JSON para su uso, el valor que recibe es una cadena de caracters de longuitud 18.

"""

tags_metadata = [
    {
        "name": "/",
        "description": "default",
    },
    {
        "name": "curp",
        "description": "Validación de CURP en sistema de RENAPO",
    },
]

app = FastAPI(
    title="CURP Validador",
    description=description,
    version="0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "J. Antonio Mora",
        "url": "https://jantoniomora.wordpress.com/",
    },
    openapi_tags=tags_metadata
)

@app.get('/', tags=["/"])
def main():
    return { 
        "msg" : "V1 Renapo Curp" 
        }

@app.get("/curp/{curp}", tags=["curp"])
def ValidaCurp(curp: str):
    dataJson = jsonable_encoder(Validador.CURP(curp))    
    return Response(content=dataJson, media_type="application/json")
    
