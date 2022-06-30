# <img src="https://user-images.githubusercontent.com/92172040/168483567-d59c8404-fe28-4a1d-80e1-c1e7eaafd230.png" alt="logoSACPU" width="35"/> UTEC COMPUTERS - PC Build Simulator

### Integrantes

* Anderson Cárcamo
* Susana Chang

### Descripción del proyecto

Nuestro proyecto es una aplicación web que permite el simulado de compra de una computadora teniendo en cuenta como pieza base la tarjeta madre y la compatibilidad de esta con los diferentes componentes. La información de la base de datos está basada en direntes páginas web de compra de tecnología especializada en computadoras como LoginStore, y marcas propias como MSI, AMD, Intel, entre otros. Está realizada con el micro Framework Flask para el backend y el Framework Vue para el frontend.

### Objetivos principales
* **Misión**

    Simular el armado de una PC para ayudar a nuestros usuarios que no tengan un conocimiento base de como comprar una computadora por piezas.

* **Visión**

    Cumplir con la demanda de nuestros usuarios, siendo útil y de fácil manejo.

### Información de librerías/frameworks/plugins

* **Backend**

| Librería           | Versión |
| :--                | :--     |
| bcrypt             | 3.2.2   |
| cffi               | 1.15.0  |
| click              | 8.1.3   |
| colorama           | 0.4.4   |
| configparser       | 5.2.0   |
| Flask              | 2.1.2   |
| Flask-Cors         | 3.0.10  |
| Flask-SQLAlchemy   | 2.5.1   |
| greenlet           | 1.1.2   |
| importlib-metadata | 4.11.4  |
| itsdangerous       | 2.1.2   |
| Jinja2             | 3.1.2   |
| MarkupSafe         | 2.1.1   |
| psycopg2-binary    | 2.9.3   |
| pycparser          | 2.21    |
| six                | 1.16.0  |
| SQLAlchemy         | 1.4.37  |
| Werkzeug           | 2.1.2   |
| zipp               | 3.8.0   |

* **Frontend**

| Librería   | Versión |
| :--        | :--     |
| core-js    | ^3.8.3  |
| vue        | ^3.2.13 |
| vue-router | ^4.0.3  |

* **Frontend Dependencias de Desarrollador**

| Librería               | Versión  |
| :--                    | :--      |
| @babel/core            | ^7.12.16 |
| @babel/eslint-parser   | ^7.12.16 |
| @vue/cli-plugin-babel  | ~5.0.0   |
| @vue/cli-plugin-eslint | ~5.0.0   |
| @vue/cli-plugin-router | ~5.0.0   |
| @vue/cli-service       | ~5.0.0   |
| eslint                 | ^7.32.0  |
| eslint-plugin-vue      | ^8.0.3   |

### Script a ejecutar la base de datos

Para ejecutar la base de datos con datos, lo primero que se tiene que realizar es crear en postgresql una base de datos. Ejemplo:

```sql
CREATE DATABASE ejemplo;
```

Crear un archivo config.txt dentro de la carpeta /backend para la configuración de la base de datos. Ejemplo:

```
[config]
username=postgres
password=admin
host=localhost:5432
database_name=ejemplo
secret_key=clavesecreta
```

Crear el ambiente virtualizado, instalar las dependencias para el backend, entrar a la carpeta del backend y ejecutar el script dump_data.py que contiene datos para probar la página web.
```bash
python3 -m venv venv
pip install -r requirements.txt
cd backend
python3 dump_data.py
```

### Información de endpoints

* **Endpoints en el backend**

| Endpoint          | POST | GET  | PATCH | DELETE |
| :--               | :--: | :--: | :--:  | :--:   |
| /compatibles      | ✅   | ✅  |       |        |
| /compatibles/:id  |      | ✅   | ✅   | ✅    |
| /components       | ✅   | ✅  |       |        |
| /components/:id   |      | ✅   | ✅   | ✅    |
| /motherboards     | ✅   | ✅  |       |        |
| /motherboards/:id |      | ✅   | ✅   | ✅    |
| /simulations      | ✅   | ✅  |       |        |
| /simulations/:id  |      | ✅   |      | ✅     |
| /users            | ✅   | ✅  |       |        |
| /users/:id        |      | ✅   | ✅   | ✅    |

* **Endpoints en el frontend**

| Endpoint          | Nombre      | Componente      |
| :--               | :--         | :--             |
| /                 | home        | HomeView        |
| /login            | login       | LoginView       |
| /register         | register    | RegisterView    |
| /simulator        | simulator   | SimulatorView   |
| /simulation/:id   | simulation  | SimulationView  |
| /profile          | profile     | ProfileView     |
| /admin            | admin       | AdminHomeView   |
| /admin/create     | adminCreate | AdminCreateView |
| /admin/delete     | adminDelete | AdminDeleteView |
| /admin/update     | adminUpdate | AdminUpdateView |
| /:pathMatch(.*) * | errorPage   | ErrorView       |

### Hosts

|          | Host                  | Puerto |
| :--      | :--                   | :--    |
| postgres | localhost (127.0.0.1) | 5432   |
| backend  | localhost (127.0.0.1) | 5000   |
| frontend | localhost (127.0.0.1) | 8080   |

### Forma de autenticación

Para la autenticación en la página web en el backend tenemos un modelo llamado User que guarda el nombre de usuario y la clave encriptada (usando la librería bcrypt). En el endpoint del frontend /register, se utilizan expresiones regulares para validar la dificultad requerida de la contraseña. Al realizar el envío, se realiza un POST al endpoint del backend /users para crear un usuario, si el nombre de usuario ya se encuentra registrado, nos mandará una respuesta 422; si todo sale correcto se creará el usuario con una respuesta 200 y la página nos redirecciona al endpoint de frontend /login.

En el endpoint del frontend /login se ingresa el nombre de usuario y contraseña. Al realizar el envío se realiza un POST al endpoint /users, pero a diferencia del registro, dentro del body del request se envía un campo extra llamado login. Si el nombre de usuario no es encontrado en la base de datos, el backend nos mandará una respuesta 404, si el usuario existe, pero la clave es incorrecta, nos mandará una respuesta 422; y si se realiza el login correctamente nos manda una respuesta 200 y un token.

Una vez autenticado, hay un endpoint en el frontend /profile en el que se puede realizar el cambio de contraseña, se pide ingresar la contraseña anterior y una nueva, asimismo revisa como el el registro de usuario, a través de expresiones regulares que la nueva contraseña sea fuerte. Al realizar el envío se realiza un PATCH al endpoint del backend a /users/:id, si la contraseña actual no coincide con la existente en la base de datos, el servidor nos respondera con un error 422; y si el cambio de contraseña es exitoso, nos responderá con un 200.

### Manejo de errores HTTP
**500: Errores en el servidor**

* **500: Internal Server Error**<br>
Si se genera un error en el backend, este mandará una respuesta 500 y el frontend mostrará el la página que ha ocurrido un error.

**400: Errores en el cliente**

* **404: Resource Not Found**<br>
Si un recurso no es encontrado en el backend, este mandará una respuesta 404 y el frontend dependiendo de si el recurso pedido es importante o no para la navegación en la página, o no lo pintará y seguirá o informará que no se encuentra el recurso.

* **422: Unprocessable**<br>
Si el body de la petición no cumple con los datos necesarios y/o correctos para procesar la petición, el backend mandará una respuesta 422 y el frontend mostrará que la petición fue incorrecta.

**300: Redirección**

* En el desarrollo de la aplicación web, no se visto necesario implementar visualmente las respuestas de redirección.

**200: Exitoso**

* En el desarrollo de la aplicación web, no se visto necesario implementar visualmente las respuestas exitosas.

**100: Informacional**

* En el desarrollo de la aplicación web, no se visto necesario implementar visualmente las respuestas informacionales.

### Deployment scripts

Para la ejecución del backend (antes se debe crear e ingresar el ambiente virtualizado e instalar las dependencias):

```bash
cd backend
$env:FLASK_APP = 'server'
$env:FLASK_ENV = 'development'
flask run
```

Para la ejecución del frontend:

```bash
cd frontend
npm install
npm run serve
```
