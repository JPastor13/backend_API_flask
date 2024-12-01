# Plaza Santader

## Tablas

- Usuarios (users)

| columna   | tipo         | opciones      |
| --------- | ------------ | ------------- |
| id        | SERIAL       | PRIMARY KEY   |
| name      | VARCHAR(120) | NOT NULL      |
| last_name | VARCHAR(150) | NOT NULL      |
| username  | VARCHAR(80)  | UNIQUE        |
| password  | VARCHAR(255) | NOT NULL      |
| email     | VARCHAR(160) | UNIQUE        |
| rol_id    | INT          | FOREIGN KEY   |
| status    | BOOLEAN      | DEFAULT(true) |

- Roles (roles)

| columna | tipo        | opciones      |
| ------- | ----------- | ------------- |
| id      | SERIAL      | PRIMARY KEY   |
| name    | VARCHAR(30) | NOT NULL      |
| status  | BOOLEAN     | DEFAULT(true) |



- stores (tiendas)


| columna      | tipo        | opciones      |
| -------      | ----------- | ------------- |
| id           | SERIAL      | PRIMARY KEY   |
| stand        | VARCHAR(30) | NOT NULL      |
| name         | BOOLEAN     | DEFAULT(true) |
| logo         | VARCHAR(255)| DEFAULT(true) |
| phone        | VARCHAR(20) | DEFAULT(true) |
|days_open     | VARCHAR(50) | DEFAULT(true) |
|schedule      | VARCHAR(50) | DEFAULT(true) |
|level         | VARCHAR(100)| DEFAULT(true) |
|title         | VARCHAR(150)| DEFAUL(true)  |
|description   | VARCHAR(255)! DEFAULT(true) |
|photo_menu_1  | VARCHAR(255)| DEFAULT(true) !
|photo_menu_2  | VARCHAR(255)| DEFAULT(true) !
|photo_menu_3  | VARCHAR(255)| DEFAULT(true) !
|photo_promary | VARCHAR(255)| DEFAULT(true) !
|status        | VARCHAR(255)| DEFAULT(true) !

- events (eventos)


| columna      | tipo        | opciones      |
| -------      | ----------- | ------------- |
| title        | VARCHAR     | PRIMARY KEY   |
| photo        | VARCHAR(30) | NOT NULL      |
| fecha        | VARCHAR     | DEFAULT(true) |
| hora         | VARCHAR(255)| DEFAULT(true) |

- promotions (promociones)


| columna      | tipo        | opciones      |
| -------      | ----------- | ------------- |
| store_id     | VARCHAR     | PRIMARY KEY   |
| title        | VARCHAR(30) | NOT NULL      |
| photo        | VARCHAR     | DEFAULT(true) |



## Caracteristicas

1. Login
   - [X] Integrar JWT
   - [X] Validar el hash de las contraseñas
2. Reseteo Contraseña
   - [X] Enviar un correo con la contraseña nueva, en un template (HTML)
3. CRUD para cada Tabla
   - [X] Listado con paginación
   - [X] Obtener un registro por ID
   - [X] Creación de un registro
   - [X] Actualzación de un registro por ID
   - [X] Eliminar un registro por ID (Soft Delete)

4. Documentación
   - [X] Swagger OpenAPI
5. Despliegue
   - [] Render (PAAS)

## .env

```py
FLASK_APP='main.py'
FLASK_RUN_HOST=127.0.0.1
FLASK_RUN_PORT=5000
FLASK_DEBUG=True



DATABASE_URI= 'postgresql://plazasantander_pgsql_user:qI6U5hggFl9Cp2NjlpdlDgkbJgRJwibI@dpg-ct5qtvt6l47c73fr2v70-a.virginia-postgres.render.com/plazasantander_pgsql'
SECRET_KEY='pastor'
```
## SWAGGER
```ssh
https://plazasantander-api.onrender.com/swagger-ui

```
## Migraciones

- Iniciar alembic (se ejecuta una sola vez, solo si no existe una carpeta **migrations**)

```ssh
flask db init
```

- Generar una migración (cuando se crea o se modifica un modelo, se debe ejecutar el comando)

```ssh
flask db migrate -m "comentario"
```

- Ejecutar migraciones

```ssh
flask db upgrade
```