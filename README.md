# API V0.1 RENAPO

#### Desarrollo no oficial para validar que una CURP sea válida desde el sistema de RENAPO

La API esta basada en la pagina web de [RENAPO](http://www.renapo.sep.gob.mx/wsrenapo/), la cuál utiliza una llamada _POST_ a su servicio enviando el valor de la CURP. El desarrollo se realizó utilizando [FASTAPI](https://fastapi.tiangolo.com/) y para la ejecución local se utilizó [Uvicorn](https://www.uvicorn.org/).

## Secciones
- [¿Cómo utilizar localmente la API?](#¿Cómo-utilizar-localmente-la-API?)


## ¿Cómo utilizar localmente la API?
Para utilizar el proyecto de forma local se hay que verificar los siguientes requisitos:

### Requisitos:
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

Una vez que se tienen los requisitos, hay que ejecutar el proyecto como lo indica la documentación de *FAST API*.
```
uvicorn main:app --reload
```
