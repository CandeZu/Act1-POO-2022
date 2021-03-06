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
    cuenta = Email(id, dominio, tipo)
    print("Estimado {}, te enviaremos tus mensajes a la dirección de correo {}@{}.{}".format(nombre, cuenta.getIdCuenta(), cuenta.getDominio(), cuenta.getTipoDominio()))

    print("Ingrese una nueva contraseña: ")
    contrasenia = input()
    print("Contraseña cambiada con éxito.")
    
    e1 = Email("Juan", "gmail", "com")
    print("Correo: {}@{}.{}".format (e1.getIdCuenta(), e1.getDominio(), e1.getTipoDominio()))

    archivo = open("Emails.csv")
    reader = csv.reader(archivo, delimiter=";")
    IDPrueba= input(" Ingrese ID que desea verificar\n")
    mailItem4= Email()

    cont=0
    for comp in reader:
            for i in range(10): 
                mailItem4.CrearCuenta(comp[i])
                ident = mailItem4.getIdCuenta()
                if IDPrueba == ident:
                    cont += 1
    print("Hay {} mail con el ID {}\n".format(cont,IDPrueba))
    
    archivo.close()
