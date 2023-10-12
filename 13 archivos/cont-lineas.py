fd = open('13 archivos/mbox-short.txt' , 'r')

cl = 0
cp = 0

for line in fd:
    line = line.strip()
    cp += len(line.split(' '))

    # for lin in line.split(' '):
    #     if lin.isalnum():
    #         cp += 1

    cl += 1


fd.close()

print("Cantidad de lineas:", cl)
print("Cantidad de palabras:", cp)
