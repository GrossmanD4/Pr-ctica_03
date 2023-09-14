from Clases import Estudiante
rpta=""
while rpta!="no":
    est=Estudiante()
    print("Menú interactivo: ")
    print("1: Ingreso de datos")
    print("2: Imprimir los datos")
    print("3: Registrar matrícula")
    print("4: Pagar")
    rt=int(input("--> "))
    while rt>=5 or rt<1:
        rt=int(input("--> "))
    if rt==1:
        est.ingresoDatos()
    elif rt==2:
        est.impDatos()
    elif rt==3:
        est.matricula()
    else:
        est.pago()