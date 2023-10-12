def miFuncion(email):
    return len(email)


fd = open('13 archivos/mbox-short.txt', 'r')

cl = 0
setEmail = set()
for linea in fd:
    if linea.startswith('To:'):
        setEmail.add(linea.split()[1])


fd.close()

cl = len(setEmail)
print("Cantidad de correos de origen distinto: " , cl)
for email in sorted(setEmail, reverse = True, key = miFuncion):
    print(email ," enviado [OK]")
    