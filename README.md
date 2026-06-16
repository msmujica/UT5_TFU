# UT5_TFU - API con FastAPI, MySQL y Docker

Este proyecto corresponde a una API desarrollada en Python utilizando FastAPI, conectada a una base de datos MySQL y levantada mediante Docker.

La API sigue una organización inspirada en el patrón MVC, adaptada al desarrollo de una API REST. Además, se incorporan capas adicionales como `Services` y `Repositories` para lograr una mejor separación de responsabilidades, mantener el código más ordenado y facilitar su mantenimiento.

---

## Estructura del proyecto

```txt
UT5_TFU/
│
├── Backend/
│   ├── Controllers/
│   ├── Models/
│   ├── Views/
│   ├── Services/
│   ├── Repositories/
│   ├── Database/
│   │   └── connection.py
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── database/
│   └── init.sql
│
├── postman/
│   └── UT5_TFU.postman_collection.json
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

- `Backend`: servicio correspondiente a la API desarrollada con FastAPI.
- `Database`: servicio correspondiente a la base de datos MySQL.

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


MVC significa:

- `Model`
- `View`
- `Controller`

En este proyecto se aplica una arquitectura inspirada en el patrón MVC, adaptada a una API REST desarrollada con FastAPI. Además, se incorporan las capas `Services` y `Repositories` para separar mejor las responsabilidades del sistema.

- `Model`: contiene las clases que representan las entidades principales del sistema, como pedidos, productos o usuarios. Su función es modelar la estructura de los datos utilizados por la aplicación.

- `View`: en una API REST no representa una pantalla visual, sino la forma en que se construye la respuesta que devuelve la API al cliente. En este proyecto, la vista se encarga de armar las respuestas en formato JSON.

- `Controller`: contiene los endpoints de la API. Recibe las solicitudes HTTP, obtiene los datos enviados por el cliente, llama al servicio correspondiente y devuelve la respuesta generada por la vista.

- `Service`: contiene la lógica de negocio del sistema. Se encarga de procesar la información, aplicar reglas, coordinar operaciones y comunicarse con los repositorios cuando se necesita acceder a los datos.

- `Repository`: contiene la lógica de acceso a la base de datos. Se encarga de realizar las consultas SQL, insertar, modificar, eliminar y obtener información desde MySQL.

De esta manera, el flujo principal queda organizado de la siguiente forma:

```txt
Controller → Service → Repository → Database
```

## Archivo de pruebas

El proyecto incluye un archivo de Postman (Json) para probar los endpoints de la API.

El archivo se encuentra en:

postman/UT5_TFU.postman_collection
```

Este archivo puede importarse en Postman para probar los endpoints sin tener que escribir manualmente cada ruta.

Para utilizarlo:

1. Abrir Postman.
2. Seleccionar la opción `Import`.
3. Elegir el archivo `UT5_TFU.postman_collection.json`.
4. Ejecutar los endpoints disponibles.
