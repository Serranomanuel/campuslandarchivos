frase = input ("Digite un frase con caracteres alphabeticos:")

for i in frase:   

    primera = i 
    

    for e in frase[1::]:  
        segunda = e  
        
        if primera != segunda: 
            break

        if primera == segunda:
            frase = frase.replace(i,"") 
            frase = frase.replace(e,"") 
            print(frase)
            break

