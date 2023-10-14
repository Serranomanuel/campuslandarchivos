import json

def guardarEmpleado(lstPersonal, ruta):
    
    try:
        fd = open(ruta, "w")
    except Exception as e:
        print("Error al abrir el archivo para guardar al empleado.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        json.dump(lstPersonal, fd)
    except Exception as e:
        print("Error al guardar la información del empleado.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.")
        input("Presione cualquier tecla para continuar\n")
        return False
    
    return True

def existeId(id, lstPersonal):
    for datos in lstPersonal:
        k = int(list(datos.keys())[0])
        if k == id:
            return True
    return False

def leerID(msj):
    while True:
        try:
            id = int(input(msj))
            if id < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return id
        except ValueError:
            print("Error al ingresar el ID.")

def leerEdad(msj): 
    while True: 
        try:
            edad = float(input(msj))
            if len(edad) > 3 or edad < 0:
                print("Error. la edad no esta dentro del rango valido") 
                continue
            return edad 
        except ValueError : 
            print("Error. Numero invalido") 
            input("Presione cualquier tecla para continuar...")

def leerTelefono(msj): 
    while True: 
        try:
            num = int(input(msj))
            return num 
        except ValueError : 
            print("Error. Numero invalido") 
            input("Presione cualquier tecla para continuar...")

def leerNombre(msj): 
    while True:
        try:
            nom = input(msj)
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def leerSexo(msj):
    while True:
        try:
            sex = input(msj).upper
            sex = sex.strip()
            if not sex == "M" or not sex == "F":
                print("Nombre inválido")
                continue
            return sex
        except Exception as e:
            print("Error al ingresar el sexo.", e)

def ModificarEmpleado(lstEmpleado, rutafile):
    id = leerID("Digite id empleado a modificar")
    if existeId(id,lstEmpleado) == True:
        while True:
            try:
                print("\nOPCIONES A MODIFICAR")
                print("1. Nombre")
                print("2. Edad")
                print("3. Sexo\n")
                print("4. Telefono\n")


                select = int(input("\nDigite la opcion del empleado que quiere modificar: "))
                if(select<1 or select>4):
                    print("Error numero fuera de rango")
                    continue
                break
            except Exception as e:
                print("Error", e)
        if(select == 1):
            Nombre = leerNombre("\nDigite nuevo nombre; ")
            for i in len(lstEmpleado):
                for k, v in lstEmpleado:
                    i[k]["nombre"] = Nombre
        elif(select ==2):
            Edad = leerEdad("\nDigite nueva edad: ")
        elif(select == 3):
            Sexo = leerSexo("\nDigite nuevo Sexo: ")
        elif(select == 3):
            Sexo = leerTelefono("\nDigite nuevo Telefono: ")
            print(lstEmpleado)
            if guardarEmpleado(lstEmpleado,rutafile) == True:
                print("EMpleado guardado con exito")
            else:
                print("Ocurrio un error al guardar el empleado")
                return
    else:
        print("Usuario no encontrado")
        return

def borrarPersonal(lstPersonal, rutaFile):
    print("\n\n3. Borrar Personal")
    
    id = int(input("Ingrese el ID: "))
    if existeId(id, lstPersonal) == -1:
        # si existeId es -1 entonces no existe ese id en lstPersonal
        print("No existe un empleado con ese ID")
        input("Presione cualquier tecla para continuar\n")
        return None
    
    for i in range(len(lstPersonal)):
        datos = lstPersonal[i]
        k = int(list(datos.keys())[0])
        if k == id:
            del lstPersonal[i]
            break
    
    if guardarEmpleado(lstPersonal, rutaFile) == True:
        print("El empleado ha sido borrado con exito")
        input("Presione cualquier tecla para continuar\n")
    else:
        print("Ocurrio un error al borrar el empleado")
        input("Presione cualquier tecla para continuar\n")
        return None

def agregarPersonal(lstPersonal, ruta):
    print("\n\n1. Agregar Personal")
    
    id = leerID("Ingrese el id del empleado")
    while existeId(id, lstPersonal) != -1:
        # si existeId es -1 entonces no existe ese id en lstPersonal
        # si es diferente a -1, entonces el id y existe.
        print("--> Ya existe un empleado con ese ID")
        input("Presione cualquier tecla para continuar\n")
        id = leerID("Ingrese el id del empleado")
        
    nombre = leerNombre("Ingrese el nombre del empleado: ")
    edad = leerEdad("Ingrese la edad")
    sexo = leerSexo("Sexo (M/F)")
    telefono = leerTelefono("Ingrese el numero telefonico ")
    
    dicEmpleado = {}
    dicEmpleado[id] = {"nombre":nombre, "edad":edad, "sexo":sexo, "telefono":telefono}
    lstPersonal.append(dicEmpleado)
    
    if guardarEmpleado(lstPersonal, ruta) == True:
        input("El empleado ha sido registrado con éxito.\nPresione cualquier tecla para continuar...")
    else:
        input("Ocurrio algún error al guardar el empleado.")

def menu():
    while True:
        try:
            print("\n" * 30)
            print("*** REGISTRO DEL PERSONAL ***".center(40))
            print("MENU".center(40))
            print("1. Agregar")
            print("2. Modificar")
            print("3. Eliminar")
            print("4. Ver")
            print("5. Salir")
            op = int(input(">>> Opción (1-5)? "))
            if op < 1 or op > 5:
                print("Opción no válida. Escoja de 1 a 5.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 5.")
            input("Presione cualquier tecla para continuar...")

def cargarInfo(lstPersonal, ruta):
    try:
        fd = open(ruta, "r")
    except Exception as e:
        try:
            fd = open(ruta, "w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            input("Presione cualquier tecla para continuar\n")
            return None
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstPersonal = json.load(fd)
        else:
            lstPersonal = []
    except Exception as e:
        print("Error al cargar la información\n", e)
        input("Presione cualquier tecla para continuar\n")
        return None
    
    # print(lstPersonal)
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.\n", e, "\n")
        input("Presione cualquier tecla para continuar\n")
        return None
    return lstPersonal
    
# *** PROGRAMA PRINCIPAL ***
rutaFile = "Campus Lands\\Ciclo 1\\Grupo-C4-Sep\\Código\\11 archivos\\datpersonal.json"
lstPersonal = []
lstPersonal =cargarInfo(lstPersonal, rutaFile)
while True:
    op = menu()
    if op == 1:
        agregarPersonal(lstPersonal, rutaFile)
    elif op == 2:
        # Modificar
        pass
    elif op == 3:
        borrarPersonal(lstPersonal, rutaFile)
    elif op == 4:
        # Ver
        pass
    else:
        # Salir
        print("\nGracias por usar el programa")
        break