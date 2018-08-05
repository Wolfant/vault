# Vault Manager

## Creador de Baul Para JBoss EAP

Sistema Web desarrollado con Bootstrap Flask y WTForms.

Permite crear un Key Store y un Baul directamente en el Servidor.

Entrega la configuracion del Baul, para que los administradores
de JBoss no sepan las claves o textos secretos usados para conexion
a Base de datos u otros aplicativos.

## Instalación

Para el correcto funcionameinto se usa Python 3.

Se recomineda el uso de virtualenv.

`virtualenv virtualenv venv`

`source venv/bin/activate`

`pip3 install -r requirements.txt`