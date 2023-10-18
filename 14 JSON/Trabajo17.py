import json

def guardarLibro(lstLibros, ruta):
    try:
        fd = open(ruta, 'w')
    except Exception as e:
        print("Error al abrir el archivo para guardar el libro: \n" + str(e))
        return None
    
    try:
        json.dump(lstLibros, fd)
    except Exception as e:
        print("Error al guardar la informacion del libro. \n" + str(e))
        return None
    
    fd.close()
    return True

def existeCodigo(codigo, lstLibros):
    for datos in lstLibros:
        k = int(list(datos.keys())[0])
        if k == codigo:
            return True
    return False

def consultarLibro(lstLibros, rutafile):
    
    codigo = int(input("Ingrese el codigo del libro del que desea informacion: "))
    if not existeCodigo(codigo, lstLibros):
        print("No existe un libro con ese codigo ")
        input()
        return
    
    for i in range(len(lstLibros)):
        datos = lstLibros[i]
        k = int(list(datos.keys())[0])
        if k == codigo:
            print("\n\n**************Informacion del libro***************")
            print("-" * 50)
            print(f"\t|Titulo: ", lstLibros[i][f"{codigo}"]["titulo"])
            print(f"\t|Autor:  ", lstLibros[i][f"{codigo}"]["autor"])
            print(f"\t|Precio: ", lstLibros[i][f"{codigo}"]["precio"])
            print("-" * 50)
            break


def borrarLibro(lstLibros, rutaFile):
    print("\n\nBorrar personal")

    codigo = int(input("Ingrese el codigo: "))
    if not existeCodigo(codigo, lstLibros):
        print("No existe un libro con ese codigo ")
        input()
        return
    
    for i in range(len(lstLibros)):
        datos = lstLibros[i]
        k = int(list(datos.keys())[0])
        if k == codigo:
            del lstLibros[i]
            break

    if guardarLibro(lstLibros, rutaFile) == True:
        print("El libro ha sido borrado con exito")
        input()
    else:
        print("Ocurrio un error al borrar el libro")




def agregarLibro(lstLibros, ruta):
    print("\n\n1. agregar Personal")

    codigo = int(input("Ingrese el codigo: "))
    while existeCodigo(codigo, lstLibros):
        print("---->Ya existe codigo: ")
        input()
        codigo = int(input("\nIngrese el codigo: "))
    
    titulo = input("titulo: ").lower()
    autor = input("autor: ").lower()
    precio = int(input("precio: "))


    dicInfoLibro = {}
    dicInfoLibro[codigo] = {"titulo": titulo, "autor":autor, "precio":precio}
    lstLibros.append(dicInfoLibro)
    guardarLibro(lstLibros, ruta)


    if guardarLibro(lstLibros, ruta) == True:
        print("El libro se ha guardado con exito")
    else:
        input("El libro se ha registrado con exito \nPresione cualquier tecla para continuar\n")

def menu(): 

    while True: 
        try: 
            print("****Libreria 'el arsenal'*****")
            print("=" * 30)
            print("\t1. Insertar") 
            print("\t2. Consultar") 
            print("\t3. Editar") 
            print("\t4. Borrar") 
            print("\t5. Salir") 
            print("=" * 30)
            op = int(input(">>>>>> Opcion (1-5): ")) 
            if op <1 or op > 5: 
                print("Opcion no valcodigoa. Escoja de 1 a 5. ")  
                input("Presione cualquier tecla para continuar: ")
                continue 
            return op #Devulve el valor op 
        except ValueError:  
            print("Opcion no valcodigoa. Escoja de (1-5 )") 
            input("Presione cualquier tecla para continuar: ") 

def cargarInfo(ruta):
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
            lstLibros = json.load(fd)
        else:
            lstLibros = []
    except Exception as e:
        print("Error al intentar cargar la informacion\n" , e)
        return None
    
    print(lstLibros)
    fd.close()
    return lstLibros


rutaFile = "14 JSON/listalibros.json"
lstLibros = []
lstLibros = cargarInfo(rutaFile)


#Programa principal 
while True: 

    opcion = menu() 
        

    if opcion == 1: 
        agregarLibro(lstLibros, rutaFile)

    elif opcion == 2:
        # lstLibros = cargarInfo(rutaFile)
        consultarLibro(lstLibros, rutaFile)

    elif opcion == 3: 
        borrarLibro(lstLibros, rutaFile)
        pass

    elif opcion == 4: 
        pass

    elif opcion == 5: 

        print("\n\nGracias por usar la calculadora") 
        print("Adios") 
        input("Presione cualquier tecla para salir ... ") 
        break 
    input("\nPresione cualquier tecla para volver al menu ...")
    
