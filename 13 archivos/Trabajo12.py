# un programa que cuente los correos de origen distintos que hay en mbox.txt

def miFuncion(email):
    return len(email)


fd = open('13 archivos/mbox-short.txt', 'r')

fdNuevo = open('13 archivos/correosEnviados.txt', 'w')

cl = 0
setEmail = set()
for linea in fd:
    if linea.startswith('From:'):
        # cl += 1
        # email = linea.split()[1]
        # print(email)
        setEmail.add(linea.split()[1])


# cl = len(setEmail)
# print("Cantidad de correos de origen distinto: " , cl)
# for email in sorted(setEmail, reverse = False, key = lambda x: x.len(x)):
#     print(email)

cl = len(setEmail)
# print("Cantidad de correos de origen distinto: " , cl)
for email in sorted(setEmail, reverse = True, key = miFuncion):
    print(f"{email} \tenviado [ok]")
    fdNuevo.write(f"{email} \tenviado [ok] \n")

fd.close()
fdNuevo.close()