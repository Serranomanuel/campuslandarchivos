fd = open('13 archivos/datos-empleado.dat', 'r')


lstEmpleados = []

for linea in fd:
    lstEmpleados.append(linea.split(","))
print(lstEmpleados)

fil = len(lstEmpleados)

for l in range(fil):
        if l != 0:
            print(f"id: {lstEmpleados[l][0]}\nNombre: {lstEmpleados[l][1]}\nEdad: {lstEmpleados[l][2]}\nSexo: {lstEmpleados[l][3]}\nTelefono: {lstEmpleados[l][4]}" )
            k = 0


fd.close()