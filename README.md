# API V0.1 RENAPO

#### Desarrollo no oficial para validar que una CURP sea válida desde el sistema de RENAPO

La API esta basada en la pagina web de [RENAPO](http://www.renapo.sep.gob.mx/wsrenapo/), la cuál utiliza una llamada __POST__ a su servicio enviando el valor de la CURP. El desarrollo se realizó utilizando [FASTAPI](https://fastapi.tiangolo.com/) y para la ejecución local se utilizó [Uvicorn](https://www.uvicorn.org/).

## Secciones
- [¿Cómo utilizar localmente la API?](#cómo-utilizar-localmente-la-API)


## ¿Cómo utilizar localmente la API?
Para utilizar el proyecto de forma local se hay que verificar los siguientes requisitos:

### Requisitos:
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

Una vez que se tienen los requisitos, hay que ejecutar el proyecto como lo indica la documentación de *FAST API*, desde la terminal ejecutamos los siguiente:
```
uvicorn main:app --reload
```

Por default la API estará ejecutandose en [http://127.0.0.1:8000](http://127.0.0.1:8000), en caso que no sea esa dirección, puedes consultarlo en la consola. Si el API esta ejecutandose correctamente el mensaje de inicio podrás verlo en pantalla.

## Utilizar API
Por el momento la _API_ únicamente incluye el _endpoint_ "curp", el cual permite comprobar si una __CURP__ existe en el sistema. Los resultados serán proporcionados por la pagina, por lo cuál el API no almacenará ninguna información.


