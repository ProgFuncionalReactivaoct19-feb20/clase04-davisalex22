"""
Ejercicio 3 : Clase 4 Manejo de colecciones y Tuplas
Autor = @davisalex22

Encontrar : [("a",(30,1)),("b",(100,2)),("c",(20,4))]
"""
# Declaracion de Listas

lista = [(100, 2), (20, 4), (30, 1)]
lista2 = ["b", "a", "c"]

# Muestra en pantalla de resultados y Uso de list, zip y sorted

listaC = reversed(sorted(map(lambda x: x.upper(), lista2)))

# Muestra en Pantalla de resultados

print(list(zip(sorted(lista, key=lambda x: x[0]), listaC)))
