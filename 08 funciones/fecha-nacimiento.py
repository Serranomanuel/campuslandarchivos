"Fecha de nacimiento" 

fecha = input("Digite la fecha de nacimiento con el siguiente formato dd/mm/aaaa: ") 
partes = fecha.split("/") 

if partes[0].isdigit() and len(partes[0]) == 2 or len(partes[0]) == 1 and \
    partes[1].isdigit() and len(partes[1]) == 2 or len(partes[1]) == 1  and \
     partes[2].isdigit() and len(partes[2]) == 4 : 

    print(f"El dia es: {partes[0]} , el mes es: {partes[1]} y el año es: {partes[2]}") 
else: 
    print("El formato es incorrecto") 





