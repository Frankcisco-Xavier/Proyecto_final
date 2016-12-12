import web, datetime

db = web.database(dbn='postgres', host='ec2-54-163-254-48.compute-1.amazonaws.com', port='5432', db='d5udq2a6eihpmb',pw='61de49a2f52ead35a8bd8ca6d865eba6f202c101f8325b756e3dbab54e7f28e7', user='nadzfbbvljbjrd')

def get_posts():
    return db.select('contactos', order='id_contacto DESC')

def get_post(id):
    try:
        return db.select( 'contactos', where="id_contacto=$id",vars=locals())[0]
    except IndexError:
        return None

def new_post(nombre, telefono, email, sitio_web, informacion, guia_turistico, telefono_guia):
    db.insert('contactos', nombre=nombre, telefono=telefono, email=email, fecha_actuliz=datetime.datetime.utcnow(), sitio_web=sitio_web, informacion=informacion, guia_turistico=guia_turistico, telefono_guia=telefono_guia)

def del_post(id):
    db.delete('contactos', where="id_contacto=$id", vars=locals())

def update_post(id, nombre, telefono, email, sitio_web, informacion, guia_turistico, telefono_guia):
    db.update('contactos', where="id_contacto=$id", vars=locals(),
        nombre=nombre, telefono=telefono, email=email, fecha_actuliz=datetime.datetime.utcnow(), sitio_web=sitio_web, informacion=informacion, guia_turistico=guia_turistico, telefono_guia=telefono_guia)
