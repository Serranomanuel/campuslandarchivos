# programa para calcular el producto con mas ingresos
def calcProdMasIngSem(matVentas, matPrecios):
    fil = len(matVentas)
    lstTotalVentas = [0] * fil
    for f in range(fil):
        lstTotalVentas[f] = sum(matVentas[f] * matPrecios[f])
    maxventas = max(lstTotalVentas)
    prodMaxVentas = lstTotalVentas.index(maxventas)  + 1
    return prodMaxVentas


def calcDiaMasIngSem(matVentas, matPrecios):
    lstTotalVentas = [0] * 7
    for f in range(len(matVentas)):
        for c in range(len(matVentas[f])):
            lstTotalVentas[c] = lstTotalVentas[c] + (matVentas[f][c] * matPrecios[f])



    maxVentas = max(lstTotalVentas)
    diaMaxVentas = lstTotalVentas.index(maxVentas) + 1
    return diaMaxVentas


matPrecios = [1500,5000,6500,2500,22500]
matVentas = [[100,88,92,94,85,110,118],
                [30,42,31,32,38,40,37],
                [23,35,39,45,55,60,61],
                [45,50,56,65,47,57,68],
                [18,25,33,21,22,28,32]]


prodMasIngSem = calcProdMasIngSem(matVentas, matPrecios)
print(f"El producto de mas ingreso es el: {prodMasIngSem}")

diaMasIngSem = calcDiaMasIngSem(matVentas, matPrecios)
if diaMasIngSem == 7:
    print(f"El dia de mas ingreso es el:{diaMasIngSem} o domingo...")