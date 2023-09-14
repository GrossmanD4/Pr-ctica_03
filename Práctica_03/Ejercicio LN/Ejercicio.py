#Desarrolle una aplicación en lenguaje Python que contenga las clases Producto, Cliente y Venta.
#El programa debe poder registrar los datos de los objetos de todas las clases.
#Los datos de los objetos de la clase venta están vinculados al producto y al cliente.
#La aplicación debe poseer un menú de opciones.
class Cliente:

    def __init__(self, name="", añs=0, dni=""):
        self.nombreH=name
        self.añoH=añs
        self.dniH=dni

    def obtenerDT(self):

        while len(self.nombreH)<=0:
            self.nombreH=str(input("Ingrese el su nombre: "))

        while self.añoH<=0:
            self.añoH=int(input("Ingrese su edad: "))

        while len(self.dniH)!=8:
            self.dniH=str(input("Ingrese su DNI: "))

    def llamarnombre(self):
        print("Nombre: ",self.nombreH)
    def llamaraños(self):
        print("Edad: ",self.añoH)    
    def llamardni(self):
        print("DNI: ",self.dniH)    

class Producto:
    
    def __init__(self,nombre="",precio=-5,codigo="",acumulador=set(),precioT=0,fin=0):
        self.nombreP=nombre
        self.precioP=precio
        self.codigoP=codigo
        self.productos=acumulador
        self.precioTP=precioT
        self.precioFinal=fin

    def obtenerPF(self):
        continuar="sis"
        while continuar!="no":
            self.codigoP=""
            self.nombreP=""
            self.precioP=-5

            while len(self.nombreP)<=0:
                self.nombreP=str(input("Ingrese el nombre del producto: "))

            while self.precioP<=0:
                self.precioP=float(input("Ingrese su el precio del producto: "))

            while len(self.codigoP)!=4:
                self.codigoP=str(input("Ingrese el codigo de fácil acceso del producto: "))
            
            print("Se agregó el producto: ",self.nombreP," con el valor de: ",self.precioP)
            self.productos.add(self.nombreP)
            self.precioTP+=self.precioP
            print("Precio total del Carrito:")
            print("S/",self.precioTP)

            continuar=str(input("¿Desea continuar comprando? --> "))
            while continuar!="si" and continuar!="no":
                continuar=str(input("Ingrese una respuesta válida --> "))
                
            if continuar=="no":
                if self.precioTP!=0:
                    self.precioFinal=(self.precioTP*0.18)+self.precioTP
                    print("El precio final será de S/",self.precioFinal)
                else:
                    print("El precio final será de S/0")
    
    def llamarprod(self):
        print("Productos comprados: ")
        for x in self.productos:
            print("- ",x)
    def prefin(self):
        print("Precio a pagar + IGV: ",self.precioFinal)    

        

class Venta():
    class ven1(Cliente):
        pass
    class ven2(Producto):
        pass


venD3=Venta.ven1()
venD4=Venta.ven2()
print("CD.COM ")
venD3.obtenerDT()
venD4.obtenerPF()
rpta="si"
while rpta!="no":
    rpta=str(input(("¿Desea revisar los detalles de su compra antes de imprimir su boleta de compra?-->  ")))
    while rpta!="si" and rpta!="no":
        rpta=str(input(("Ingrese una respuesta válida -->  ")))   
    if rpta=="si":
        print("1: Productos comprados")
        print("2: Precio Final")
        rta=4
        while rta!=1 and rta!=2:
            rta=int(input("-->"))    
        if rta==1:
            venD4.llamarprod()
        else:
            venD4.prefin()
    else:
        print("Recuerde que ante cualquier reclamo puede acercarse al área de servicio para el cliente.")
        print("BOLETA AUTOMÁTICA")
        venD3.llamarnombre()
        venD3.llamaraños()
        venD3.llamardni()
        venD4.llamarprod()
        venD4.prefin()
        print("Acérquese al mostrador para cancelar sus productos.")


