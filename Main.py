from xml.dom.pulldom import SAX2DOM
from Email import Email
import csv

if __name__=='__main__':
    print("Ingrese su nombre: ")
    nombre = input()
    print("Ingrese identificador de cuenta: ")
    id = input()
    print("Ingrese dominio: ")
    dominio = input()
    print("Ingrese tipo de dominio: ")
    tipo = input()
    print("Ingrese una nueva contraseña: ")
    contrasenia = input()

    cuenta = Email(id, dominio, tipo)
    
    print("Estimado {}, te enviaremos tus mensajes a la dirección de correo {}@{}.{}".format(nombre, cuenta.getIdCuenta(), cuenta.getDominio(), cuenta.getTipoDominio()))
    print("Contraseña cambiada con éxito.")

    e1 = Email("Juan", "gmail", "com")
    print("Correo: {}@{}.{}".format (e1.getIdCuenta(), e1.getDominio(), e1.getTipoDominio()))

    