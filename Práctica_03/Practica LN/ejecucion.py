class Estudiante:
    def __new__(cls,*args):
        print("Se está creando una instancia de la clase")
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nombre,apellido,dni,carrera,a=53,b=432):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._carrera = carrera
        self.asa=a
        self.bab=b
    #def __del__(nombre):
    #    print("Elimina nombre")

    def ob_nombre(self):
        return self._nombre
    def est_nombre(self,nuevo):
        self._nombre=nuevo

    def ob_apellido(self):
        return self._apellido
    def est_apelldo(self,novo):
        self._apellido=novo

    def ob_dni(self):
        return self._dni
    def est_dni(self,navo):
        self._dni=navo

    def ob_carrera(self):
        return self._carrera
    def est_carrera(self,nova):
        self._carrera=nova

    nombre=property(ob_nombre,est_nombre)
    apellido=property(ob_apellido,est_apelldo)
    dni=property(ob_dni,est_dni)
    carrera=property(ob_carrera,est_carrera)

    def suma(self):
        return self.bab+self.asa
    
    def resta(self):
        return self.bab-self.asa

    def sum(c,d):
        return c+d
    
    def rest(c,d):
        return c-d
        
    
persona=Estudiante("Julian","Vargas","12345678","Medicina")
print("Nombre: ",persona.nombre)
persona.nombre="Grossman"
print("Nuevo nombre: ",persona.nombre)

print("Apellido: ",persona.apellido)
persona.apellido="Chura"
print("Nuevo apellido: ",persona.apellido)

print("DNI: ",persona.dni)
persona.dni="72949694"
print("Nuevo DNI: ",persona.dni)

print("Carrera: ",persona.carrera)
persona.carrera="Ingenieria"
print("Nueva Carrera: ",persona.carrera)

print("Qué función desea llamar?")
print("1: Suma; 2: Resta")
res=3
while res<=0 or res>=3:
    res=int(input("--> "))
if res==1:
    Estudiante.suma
elif res==2:
    Estudiante.resta

print("Qué función desea llamar?")
print("1: Suma; 2: Resta")
res=3
while res<=0 or res>=3:
    res=int(input("--> "))
if res==1:
    print(Estudiante.sum(5,4))
elif res==2:
    print(Estudiante.rest(154,5))