def leernombre(msg):
    while True:
        try:
            n = input(msg)
            n.strip()
            if(n==0 or not n.isalnum()):
                print("Nombre no valido")
            return n
        except Exception as e:
            print("Error al ingresar el nombre", e)

def leerint(msg):
    while True:
        try:
            n = int(input(msg))
            if(n<1):
                print("Valor invalido, debe ser mayor a cero")
            return n
        except Exception as e:
            print("Error al ingresar el numero", e)

def llenarMatriz(mat,dicCiudades):

    for f in range(1):
        for c in range(len(mat[f])):
            nomCiudad = leernombre(f"Escriba el nombre de la ciudad en la red ferrovial{c+1}: ")
            mat[f][c] =  nomCiudad
            numCiudades = leerint("Digite numero de ciudades enlazadas: ")
            ciudadesenlazadas = []
            for i in range(numCiudades):
                ciudadesenlazadas.append(leernombre(f"Ciudadenlazada {i+1} "))
                dicCiudades[nomCiudad] = ciudadesenlazadas
    return

def compararCiudad():
    ciud1 = leernombre("Ingrese la ciudad a comparar")
    ciud2 = leernombre("Ingrese la segunda ciudad a comparar")

    for key, value in dicConexiones.items():
        if ciud1 in value and ciud2 in value:
            print("Estan enlazadas")
        else:
            print("no estan enlazadas")


dicConexiones = {}

def main():
    matCiudades = []
    numCiudades = leerint("Digite numero de ciudades: ")
    fil = [""] * numCiudades

    matCiudades.append(fil)
    llenarMatriz(matCiudades,dicConexiones)
    print(dicConexiones)


main()
compararCiudad()