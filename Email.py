class Email:
    __idCuenta = ""
    __dominio = ""
    __tipodominio = ""
    __contrasenia = "1234"
    __listaEmails = []

    def __init__ (self, idCuenta, dominio, tipodominio, contrasenia=''):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipodominio = tipodominio
        self.__contrasenia = contrasenia
        self.__listaEmails = []

    def retornaEmail(self):
        return "{}@{}.{}".format(self.__idCuenta,self.__dominio,self.__tipodominio)

    def getIdCuenta (self):
        return self.__idCuenta
        
    def getDominio (self):
        return self.__dominio
        
    def getTipoDominio (self):
        return self.__tipodominio

    def crearCuenta(self, id, dominio, tipo):
        cuenta = Email(id, dominio, tipo)
        return self.retornaEmail
    
    def cambiarContrasenia(self, contrasenia):
        self.__contrasenia = contrasenia
        return self.__contrasenia
    
    def testListaCuenta (self):
        archivo = open('librosPOO.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:

    def agregarCuenta (self):
    
    def buscarCuenta (self):
    
    