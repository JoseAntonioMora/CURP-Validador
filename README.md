# API V0.1 RENAPO

#### Desarrollo no oficial para validar que una CURP sea válida desde el sistema de RENAPO

La API esta basada en la pagina web de [RENAPO](http://www.renapo.sep.gob.mx/wsrenapo/), la cuál utiliza una llamada __POST__ a su servicio enviando el valor de la CURP. El desarrollo se realizó utilizando [FASTAPI](https://fastapi.tiangolo.com/) y para la ejecución local se utilizó [Uvicorn](https://www.uvicorn.org/).

## Secciones
- [¿Cómo utilizar localmente la API?](#cómo-utilizar-localmente-la-API)
  - [Requisitos para ejecutar Localmente](#requisitos)
- [Utilizar la API](#utilizar-api)
- [Respuesta de API](#respuesta-de-api)
- [Documentacion API](#documentacion-api)
- [Contacto](#contacto)

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

Para utilizar el servicio hay que ingresar a la ruta [http://127.0.0.1:8000/curp/](http://127.0.0.1:8000/curp/) en donde se tiene que enviar el parámetro de la CURP [referencia del formato CURP](https://es.wikipedia.org/wiki/Clave_%C3%9Anica_de_Registro_de_Poblaci%C3%B3n).

Endpoint: __http://127.0.0.1:8000/curp/{curp}__

Ejemplo: http://127.0.0.1:8000/curp/ABCD123456XXXXXX78


## Respuesta de API
La _API_ regresará como resultado un objeto JSON que incluye la información extraída de la pagina para su fácil consulta, a continuación un ejemplo de como se ve el resultado válido:

```
{
  "AnioReg": "1994",
  "Apellido1": "XXXX",
  "Apellido2": "XXXX",
  "CRIP": "",
  "CURP": "XXXXXXXXXXXXXXXXXX",
  "CveEntidadEmisora": "",
  "CveEntidadNac": "MC",
  "CveMunicipioReg": "081",
  "DocProbatorio": "1",
  "FechNac": "01/01/1900",
  "Foja": "",
  "FolioCarta": "",
  "Libro": "",
  "Nacionalidad": "MEX",
  "Nombres": "ANTONIO",
  "NumActa": "00055",
  "NumEntidadReg": "15",
  "NumRegExtranjeros": "",
  "Sexo": "",
  "StatusCurp": "RCN",
  "Tomo": ""
}
```

En caso que el valor de la CURP sea incorrecto o que la cadena de texto sea erronea, el _API_ mostrará el siguiente mensaje:
```
{
  "Error": "El formato de CURP o datos generales son incorrectos.",
  "msg": "curp"
}
```

El tiempo de respuesta de la API utilizando _Postman_ es de **~400ms** aprox. *Investigando como bajar tiempos en respuesta.

## Documentacion API
El _API_ al ser creada con _FAST API_ incluye una sección de documentacion la cuál puedes revisar ingresando a la direccion [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) cuando la _API_ esté en ejecución.

## Contacto
La _API_ fue desarrollada sin fines de lucro, puedes utilizarla, modificarla o compartirla, solo haz referencia a este proyecto 🤓. #HappyCoding

- Desarrollador por __Jose Antonio Mora__
- [WEB](https://jantoniomora.wordpress.com/)