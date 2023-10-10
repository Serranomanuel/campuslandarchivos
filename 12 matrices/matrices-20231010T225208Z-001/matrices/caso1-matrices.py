def leerTamaño(mensaje): 
    while True: 
        try:
            tamaño = int(input(mensaje))
            if tamaño < 0:
                print("Ingrese un numero mayor que cero")
                continue
            return tamaño 
        except ValueError : 
            print("Error. Numero invalido") 
            input("Presione cualquier tecla para continuar...")

def crearMatrices(fil, col):
    m = []
    for i in range(fil):
        fila = [0] * col
        m.append(fila)
    return m

def printMatrices(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print(mat[f][c], end='\t')
        print('')

def llenarMatrices(mat):
    contador = 0
    for f in range(len(mat)):
        #print("\nFila #",f+1)
        for c in range(len(mat[f])):
            contador += 1
            mat[f][c] = contador
            #mat[f][c] = int(input(f"\nmat[{f+1}][{c+1}]"))
            #print(mat[f][c], end=' ')
        print('')

def main():
    tamaño = leerTamaño("Ingrese el tamaño de la matriz: ")
    matriz = crearMatrices(tamaño, tamaño)
    llenarMatrices(matriz)
    printMatrices(matriz)
main()

#matriz = crearMatrices(4, 5)
#llenarMatrices(matriz)
#printMatrices(matriz)