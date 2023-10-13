import json

fd = open("14 JSON/lista.json" , "r")

lst = []

lst = json.load(fd)

for e in lst:
    print(f"Nombre: {e['nombre']}")
    print(f"Edad: {e['edad']}")
    print("=" * 30)