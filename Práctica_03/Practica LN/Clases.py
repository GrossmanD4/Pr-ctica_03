class Estudiante:

    def __init__(self,nom="",apel="",dna="",carr="",cur="",can=0,tar="",contra=""):
        self.nombre=nom
        self.apellido=apel
        self.dni=dna
        self.carrera=carr
        self.curso=cur
        self.cantidad=can
        self.tarjeta=tar
        self.contraseña=contra
    
    def ingresoDatos(self):
        while len(self.nombre)<=0:
            self.nombre=str(input("Ingrese el nombre: "))

        while len(self.apellido)<=0:
            self.apellido=str(input("Ingrese el apellido: "))

        while len(self.dni)!=8:
            self.dni=str(input("Ingrese el DNI: "))

        while len(self.carrera)<=0:
            self.carrera=str(input("Ingrese su carrera: "))

    def impDatos(self):
        print("Nombre: ",self.nombre)
        print("Apellido: ",self.apellido)
        print("DNI: ",self.dni)
        print("Carrera: ",self.carrera)
    
    def matricula(self):
        rpta="si"
        matr=set()
        cursos=["Lenguaje","Cálculo","Fisica","Estructuras","Metodología","Lenguaje"]
        print("Los cursos que puede elegir son: ")
        for x in cursos:
            print("-",x)
        while rpta!="no":
            self.curso=""
            while self.curso not in cursos:
                self.curso=str(input("Ingrese el curso al cual se va matricular, considere las mayúsculas y minúsuclas: "))
            matr.add(self.curso)
            print("Se ha matriculado para: ",matr)
            rpta=str(input("Desea continuar elegiendo sus cursos?: "))
        self.cantidad=len(matr)

    def pago(self):
        print("La cantidad a pagar será de: ",self.cantidad*150)
        while len(self.tarjeta)!=16:
            self.tarjeta=str(input("Ingrese su número de cuenta (16 términos): "))
        while len(self.contraseña)!=6:
            self.contraseña=str(input("Ingrese su clave: "))
        print("Gracias por su confianza en nuestra universidad, lo esperamos.")

    def llamado():
        est=Estudiante()
        est.ingresoDatos()
        est.impDatos()
        est.matricula()
        est.pago()
