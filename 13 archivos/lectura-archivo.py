archivo = open("13 archivos/nombres.txt", "r")


texto = archivo.read()
print(texto) # Imprime el archivo y me deja el lector en la ultima linea    

archivo.seek(0) # posiciona el lector de linea en la primera linea

texto2 = archivo.readline() # lee solo un alinea del archivo
print(texto2)

# archivo.seek(0)
texto3 = archivo.readlines() #  agrega en una lista cada uno de los elementos del archivo
print(texto3)



archivo.close()
