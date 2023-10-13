import json

def guardarEmpleado(lstPersonal, ruta):
    try:
        fd = open(ruta, 'w')
    except Exception as e:
        print("Error al abrir el archivo para guardar al empleado: \n" + str(e))
        return None
    
    try:
        json.dump(lstPersonal, fd)
    except Exception as e:
        print("Error al guardar la informacion del empleado. \n" + str(e))
        return None
    
    fd.close()
    return True

def existeID(id, lstPersonal):
    for datos in lstPersonal:
        k = int(list(datos.keys())[0])
        if k == id:
            return True
    return False

def borrarPersonal(lstPersonal, rutaFile):
    print("\n\nBorrar personal")

    id = int(input("Ingrese el ID: "))
    if not existeID(id, lstPersonal):
        print("No existe un empleado con ese ID ")
        input()
        return
    
    for i in range(len(lstPersonal)):
        datos = lstPersonal[i]
        k = int(list(datos.keys())[0])
        if k == id:
            del lstPersonal[i]
            break

    if guardarEmpleado(lstPersonal, rutaFile) == True:
        print("El empleado ha sido borrado con exito")
        input()
    else:
        print("Ocurrio un error al borrar el empleado")

def agregarPersonal(lstPersonal, ruta):
    print("\n\n1. agregar Personal")

    id = int(input("Ingrese el ID: "))
    while existeID(id, lstPersonal):
        print("---->Ya existe ID: ")
        input()
        id = int(input("\nIngrese el ID: "))
    
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    sexo = input("SEXO (M/F): ")
    telefono = input("Telefono: ")


    dicEmpleado = {}
    dicEmpleado[id] = {"nombre": nombre, "edad":edad, "sexo":sexo, "telefono":telefono}
    lstPersonal.append(dicEmpleado)


    if guardarEmpleado(lstPersonal, ruta) == True:
        print("El empleado ha sido guardado con exito")
    else:
        input("El empleado ha sido registrado con exito \nPresione cualquier tecla para continuar")

def menu(): 

    while True: 
        try: 
            print("****registro del personal*****") 
            print("1. agregar") 
            print("2. eliminar") 
            print("3. modificar") 
            print("4. ver") 
            print("5. Salir") 
            op = int(input(">>>>>> Opcion (1-5): ")) 
            if op <1 or op > 5: 
                print("Opcion no valida. Escoja de 1 a 5. ")  
                input("Presione cualquier tecla para continuar: ")
                continue 
            return op #Devulve el valor op 
        except ValueError:  
            print("Opcion no valida. Escoja de (1-5 )") 
            input("Presione cualquier tecla para continuar: ") 

def cargarInfo(lstPersonal, ruta):
    try:
        fd = open(ruta, "r")
    except Exception as e:
        try:
            fd = open(ruta, "w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n " + e)
            return None
    try:
        linea = fd.readline()
        if linea.strip() != "" :
            fd.seek(0)
            lstPersonal = json.load(fd)
        else:
            lstPersonal = []
    except Exception as e:
        print("Error al intentar cargar la informacion\n" , e)
        return None
    
    print(lstPersonal)
    fd.close()
    return lstPersonal


rutaFile = "14 JSON/datPersonal.json"
lstPersonal = []
lstPersonal = cargarInfo(lstPersonal, rutaFile)


#Programa principal 
while True: 

    opcion = menu() 
        

    if opcion == 1: 
        agregarPersonal(lstPersonal, rutaFile)

    elif opcion == 2:
        pass

    elif opcion == 3: 
        borrarPersonal(lstPersonal, rutaFile)

    elif opcion == 4: 
        pass

    elif opcion == 5: 

        print("\n\nGracias por usar la calculadora") 
        print("Adios") 
        input("Presione cualquier tecla para salir ... ") 
        break 
    input("Presione cualquier tecla para volver al menu ...")
    
