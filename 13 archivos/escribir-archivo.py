archivo = open("13 archivos/salas.txt", "w")

archivo.write("sputnik\n")
archivo.write("apolo\n")
archivo.writelines(["houston\n", "artemis\n"])


archivo.close()
print("Arch2")