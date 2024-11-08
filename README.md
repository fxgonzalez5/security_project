# Sistema con Controles de Seguridad

Este sistema cuenta con varios controles de seguridad para proteger los datos y la integridad de los usuarios. A
continuación se detallan las características principales y los pasos de configuración.

## Características de Seguridad

- **Doble Factor de Autenticación**: Requiere que el usuario verifique su identidad mediante un código de verificación
  enviado a su correo electrónico.
- **Protección de Rutas**: Solo usuarios autenticados pueden navegar a la ruta del panel o dashboard, garantizando así
  la seguridad de las secciones sensibles.
- **Encriptación de Contraseña**: Las contraseñas de los usuarios se almacenan de manera segura utilizando algoritmos de
  encriptación.
- **Control de Sesiones Activas**: Gestión y monitoreo de las sesiones activas para evitar más de un inicio de sesión.

## Requisitos

- **Python**: Versión 3.12
- **Django Admin**
    - Usuario: `admin`
    - Contraseña: `adminutpl`

## Configuración del Correo Electrónico para el Doble Factor de Autenticación

Para configurar el correo desde el cual se enviará el código de verificación, debes configurar el archivo `settings.py`.
Si utilizas una cuenta de Gmail con doble factor de autenticación, sigue estos pasos:

1. Ingresa a tu cuenta de Google y accede a la sección
   de [contraseñas de aplicaciones](https://myaccount.google.com/apppasswords).
2. Genera una nueva clave de seguridad para la aplicación.
3. Coloca esta clave como contraseña en la configuración del correo en `settings.py`.

## Modificación de Roles y Funciones de Usuarios

Para modificar los roles y funciones de los usuarios registrados, accede al panel de administración de Django. En caso
de que las credenciales proporcionadas anteriormente no funcionen, puedes crear un nuevo superusuario ejecutando el
siguiente comando:

```bash
python manage.py createsuperuser
