from fastapi import FastAPI
from starlette.responses import Response
from v1.api import Validador
from fastapi.encoders import jsonable_encoder


app = FastAPI()

@app.get('/')
def main():
    return { 
        "msg" : "EJEMPLO" 
        }

@app.get("/curp/{curp}")
def ValidaCurp(curp: str):
    dataJson = jsonable_encoder(Validador.CURP(curp))    
    return Response(content=dataJson, media_type="application/json")
    
