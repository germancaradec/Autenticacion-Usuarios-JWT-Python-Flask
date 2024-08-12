# Flask JWT App

## Descripción

Esta aplicación Flask proporciona autenticación de usuarios mediante JSON Web Tokens (JWT). Incluye rutas para la autenticación de usuarios y la gestión de lenguajes, y utiliza MySQL para la gestión de datos.


## Instalación
1 Clona este repositorio en tu máquina local:

git clone https://github.com/germancaradec/Autenticacion-Usuarios-JWT-Python-Flask.git

2 Navega al directorio del proyecto:

3 Crea un entorno virtual e instálalo:

python -m venv venv

source venv/bin/activate   # En Windows usa `venv\Scripts\activate`

4 Instala las dependencias:

pip install -r requirements.txt

5 Configura las variables de entorno en un archivo .env:

SECRET_KEY=tu_clave_secreta

JWT_KEY=tu_clave_jwt

MYSQL_HOST=localhost

MYSQL_USER=tu_usuario

MYSQL_PASSWORD=tu_contraseña

MYSQL_DB=tu_base_de_datos

MYSQL_PORT=3306

## Ejecución

Ejecuta la aplicación:

python index.py

La aplicación estará disponible en http://localhost:5000.

## Endpoints

### Autenticación

POST /auth/

Descripción: Autentica a un usuario y devuelve un token JWT.

Cuerpo de la Solicitud:
{
  "username": "usuario",
  "password": "contraseña"
}

Respuesta Exitosa:

{
  "success": true,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}

Respuesta de Error:

{
  "message": "Unauthorized"
}

Código de Estado: 401 si la autenticación falla.

### Gestión de Lenguajes

GET /languages/

Descripción: Obtiene una lista de lenguajes si el token JWT es válido.

Encabezados de Solicitud:

Authorization: Bearer <tu_token_jwt>

Respuesta Exitosa:

{
  "languages": [
    {"id": 1, "name": "Español"},
    {"id": 2, "name": "Inglés"}
  ],
  "message": "SUCCESS",
  "success": true
}

Respuesta de Error:

{
  "message": "Unauthorized"
}

Código de Estado: 401 si el token es inválido o ha expirado.

## Conceptos

JWT (JSON Web Token): Utilizado para autenticar a los usuarios. El token se genera al iniciar sesión y debe ser incluido en los encabezados de las solicitudes para acceder a recursos protegidos.

Blueprints: Utilizados para organizar las rutas en la aplicación Flask en módulos separados para una mejor gestión.

CORS (Cross-Origin Resource Sharing): Configurado para permitir solicitudes desde diferentes orígenes.

Configuración de Entorno: Las configuraciones como las claves secretas y la conexión a la base de datos se gestionan mediante variables de entorno para mayor seguridad.