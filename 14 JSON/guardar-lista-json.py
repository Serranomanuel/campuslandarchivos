# metodos de json

import json
fd = open("14 JSON/lista.json", "w")

lst = [{"nombre": "paola", "edad": 25}, 
        {"nombre": "Carlos", "edad": 28}, 
        {"nombre": "Juan", "edad": 18}, 
        {"nombre": "Mateo", "edad": 19}, 
        {"nombre": "Patricia", "edad": 21}]

json.dump(lst, fd)

fd.close()