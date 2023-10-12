fd = open('13 archivos/nombres.txt', 'r')

fd2 = open('13 archivos/nombres-bak.txt', 'w')

for line in fd:
    fd2.write(line)


fd.close()
fd2.close()
print('process finished')