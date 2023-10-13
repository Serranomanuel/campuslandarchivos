fd = open("13 archivos/mbox-short.txt", "r")

fd2 = open("13 archivos/envio-emails.txt", "w")

lstEmails = []

for linea in fd:
    if linea.startswith("From: "):
        email  = linea.split()[1]
        if email not in lstEmails:
            lstEmails.append(email)

for i in range(len(lstEmails)-1, -1, -1):
    msj = (f"{lstEmails[i]} \tEnviado [OK]")
    print(msj)
    fd2.write(msj + "\n" )

fd.close()
fd2.close()