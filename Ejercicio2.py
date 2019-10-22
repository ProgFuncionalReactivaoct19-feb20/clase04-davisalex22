"""
Ejercicio 2 : Clase 4 Manejo de colecciones y Tuplas
Autor = @davisalex22

Encontrar : [("a",(30,1)),("b",(100,2)),("c",(20,4))]
"""
# Declaracion de Listas

lista = [(100, 2), (20, 4), (30, 1)]
lista2 = ["b", "a", "c"]

# Muestra en pantalla de resultados y Uso de list, zip y sorted

print(list(zip(sorted(lista2), sorted(lista, key=lambda x: x[1]))))
