create database turismo;
use turismo;

CREATE TABLE contactos (
    id_contacto serial primary key,
    nombre varchar(50),
    telefono varchar(50),
    email varchar(50),
    fecha_actuliz timestamp,
    sitio_web text,
    informacion text,
    guia_turistico varchar(50),
    telefono_guia varchar(10));
