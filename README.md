# UT5_TFU - API con FastAPI, MySQL y Docker

Este proyecto corresponde a una API desarrollada en Python utilizando FastAPI, conectada a una base de datos MySQL y levantada mediante Docker.

La API sigue una organización inspirada en el patrón MVC, separando responsabilidades entre modelos, controladores y la capa de respuesta de la API.

---

## Estructura del proyecto

```txt
UT5_TFU/
│
├── Backend/
│   ├── Controllers/
│   ├── Models/
│   ├── Views/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── database/
│   └── init.sql
│
├── postman/
│   └── endpoints.postman_collection.json
│
├── docker-compose.yml
└── README.md
```

---

## Inicialización del proyecto

Para levantar el proyecto es necesario tener instalado Docker Desktop.

El archivo principal para iniciar el proyecto es:

```txt
docker-compose.yml
```

Desde una terminal ubicada en la carpeta raíz del proyecto, ejecutar:

```bash
docker compose up --build
```

Este comando construye la imagen del backend y levanta los servicios definidos en Docker Compose.

Los servicios principales son:

- `api`: servicio correspondiente a la API desarrollada con FastAPI.
- `mysql`: servicio correspondiente a la base de datos MySQL.

Una vez levantado el proyecto, la API queda disponible en:

```txt
http://localhost:8000
```

La documentación automática de FastAPI se puede consultar en:

```txt
http://localhost:8000/docs
```

Si se modifica el archivo `database/init.sql` y se quiere recrear la base de datos desde cero, se puede ejecutar:

```bash
docker compose down -v
docker compose up --build
```

El comando `docker compose down -v` elimina los volúmenes, por lo que también borra los datos guardados anteriormente en MySQL.

---

## Patrón MVC

El proyecto sigue una organización basada en el patrón MVC.

MVC significa:

- `Model`
- `View`
- `Controller`

En este proyecto se aplica de forma adaptada a una API REST hecha con FastAPI.

- `Model`: contiene la representación de los datos del sistema, las entidades, las clases relacionadas con la base de datos y la lógica de acceso a los datos.

- `View`: en una API REST no representa una pantalla visual, sino la respuesta que devuelve la API al cliente. En este caso, la vista corresponde principalmente a las respuestas en formato JSON.

- `Controller`: contiene los endpoints de la API. Recibe las solicitudes HTTP, procesa los datos necesarios, se comunica con la lógica correspondiente y devuelve una respuesta.

onnection.py
```

## Archivo de pruebas

El proyecto incluye un archivo de Postman para probar los endpoints de la API.

El archivo se encuentra en:

```txt
postman/endpoints.postman_collection.json
```

Este archivo puede importarse en Postman para probar los endpoints sin tener que escribir manualmente cada ruta.

Para utilizarlo:

1. Abrir Postman.
2. Seleccionar la opción `Import`.
3. Elegir el archivo `endpoints.postman_collection.json`.
4. Ejecutar los endpoints disponibles.