# un programa que cuente los correos de origen distintos que hay en mbox.txt

def miFuncion(email):
    return len(email)


fd = open('13 archivos/mbox-short.txt', 'r')

cl = 0
setEmail = set()
for linea in fd:
    if linea.startswith('From:'):
        # cl += 1
        # email = linea.split()[1]
        # print(email)
        setEmail.add(linea.split()[1])


fd.close()

# cl = len(setEmail)
# print("Cantidad de correos de origen distinto: " , cl)
# for email in sorted(setEmail, reverse = False, key = lambda x: x.len(x)):
#     print(email)

cl = len(setEmail)
print("Cantidad de correos de origen distinto: " , cl)
for email in sorted(setEmail, reverse = False, key = miFuncion):
    print(email)