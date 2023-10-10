

num1 = int(input("Digite el primer numero: "))  
num2 = int(input("Digite el segundo numero: "))

for i in range (1 , num1 + 1):  
    sumDiv = 0 

    if num1 % i == 0 :  
        sumDiv += i  

        if sumDiv != num2: 
            print("No son amigos") 
            
            for i in range (1 , num2 + 1): 

                if sumDiv == num2: 
                    print("El num1 es amigo")





for i in range (1 , num2 + 1):  
    sumDiv = 0 
    if num1 % i == 0 :  
        sumDiv += i  

        if sumDiv == num1: 
            print("El num2 es amigo")

       



