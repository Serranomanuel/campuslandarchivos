""" 
num = int(input("Ingrese un numero : "))
cPares = 0 
cImpares = 0

while num != -1 : 
    if num % 2 == 0: 
        print("EL numero es par")  
        cPares += 1

    else : 
        print("El numero es impar") 
        cImpares += 1 

    num = int(input("Ingrese un numero: "))

print("\n" , "="  *30) 
print("La cantidad de numeros pares: " , cPares) 
print("La cantidad de numeros impares es: " , cImpares) 

 """ 


"""  
eleccion = "S" 
tarifaBasica = 0

while eleccion == "S" or eleccion == "s":  

    nombre = input("Digite el nombre del usuario: ") 
    estrato = int(input("Digite el estrato [1-5]: ")) 

    if estrato == 1:  
        tarifaBasica = 10000

    if estrato == 2:  
        tarifaBasica = 15000

    if estrato == 3:  
        tarifaBasica = 30000

    if estrato == 4:  
        tarifaBasica = 50000

    if estrato == 5:  
        tarifaBasica = 65000
    
    print("\n" , "=" * 30)

    print(f"Nombre del usuario : {nombre}\nTarifa basica $ {tarifaBasica:,.0f}") 

    print("\n" , "=" * 30)

    eleccion = input("Desea seguir facturando? [S-s] sino digite cualquier otra cosa: ") 

    print("\n" , "=" * 30)
    
print("Muchas gracias")
 """ 

matriculasTotales = 0


eleccion = "S" 

while eleccion == "S" or eleccion == "s":  



    nombre = input("Digite el nombre de usuario: ") 
    codigo = int(input("Digite el codigo: ")) 


    programaAcademico = ""
    becaAcademica = "" 
    indicadorDescuento = 0
    valorPrograma = 0 



    print("\n 1.Tecnico en sistemas \n 2. Tecnico en desarrollo de videojuegos \n 3. Tecnico en animacion digital\n") 


    entradaPrograma = int(input("Seleccione  el numero del programa academico: ")) 



    if entradaPrograma == 1: 
        programaAcademico = "Tecnico en sistemas" 
        valorPrograma = 800000 

    elif entradaPrograma == 2: 
        programaAcademico = "Tecnico en desarrollo de videojuegos" 
        valorPrograma = 1000000 


    elif entradaPrograma == 3: 
        programaAcademico = "Tecnico en animacion digital"  
        valorPrograma = 1200000 

    print("\n" , "=" *40) 

    print("\n 1.Beca por rendimiento \ 2. Beca cultural \n") 

    entradaBeca = int(input("Digite el numero de la beca que posee: "))

    if entradaBeca == 1 :  
        becaAcademica = "Beca por rendimiento" 
        indicadorDescuento = 0.5 
    elif entradaBeca == 2 : 
        becaAcademica = "Beca cultural" 
        indicadorDescuento = 0.4 
    else: 
        becaAcademica = "Ninguna" 
        
    valorNetoPrograma = valorPrograma * indicadorDescuento 

    matriculasTotales += valorNetoPrograma

    print("\n" , "=" *40) 

    print(f"Programa academico: {programaAcademico}") 
    print(f"Tipo de descuento: {indicadorDescuento} %") 
    print(f"Valor final de descuento {valorNetoPrograma:,.0f}") 
    print(f"Valor de matriculas totales {matriculasTotales:,.0f}")

    print("\n" , "=" *40) 

    eleccion = input("Desea continuar [S-s]? , sino digite cualquier otra cosa")
