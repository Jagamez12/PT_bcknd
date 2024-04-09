Documentación del Backend - Aplicación de Gestión de Empleados
Esta documentación describe el funcionamiento del backend de la aplicación de gestión de empleados, desarrollada con Django REST Framework.

Tecnologías Utilizadas
 - Django REST Framework: Framework para el desarrollo rápido de APIs web.
 - PostgreSQL: Sistema de gestión de bases de datos relacional utilizado para almacenar los datos de los empleados.
 - Python 3: Lenguaje de programación utilizado para desarrollar el backend.

Configuracion del Entorno de Desarrollo 

1. Clonar el repositorios:
    - git clone https://github.com/Jagamez12/PT_bcknd.git
    - cd /backend
2. Usar PIPENV para el entorno virtual de desarrollo
    -pipenv install
    -pipenv shell
3. Instalar las siguientes librerias:
    django = "*"
    djangorestframework = "*"
    psycopg2 = "*"
    django-sendgrid-v5 = "*"
    python-decouple = "*"

4. Configurar la base de datos.
    debe crear una variable de entorno .env y rellenar los campos que les deje en .env.example en el respositorio
5. Ejecutar las migraciones
    - Pipenv run makemigrations
    - pipenv run migrate
6. Iniciar el Servidor de Desarrollo

ENDPOINS DE LA API REST
Tener en cuenta que los procesos estan protegidos y debes estar autenticado para poder hacer las peticiones, en la cabecera de la request debe haber un campo "authorization" con el token retornado por el endpoint /users/token

Empleados
 1. GET /api/empleados/: Obtiene la lista de todos los empleados.
 2. POST /api/empleados/: Crea un nuevo empleado.
 3. GET /api/empleados/{id}/: Obtiene los detalles de un empleado específico.
 4. PUT /api/empleados/{id}/: Actualiza los detalles de un empleado específico.
 5. DELETE /api/empleados/{id}/: Elimina un empleado específico.

 