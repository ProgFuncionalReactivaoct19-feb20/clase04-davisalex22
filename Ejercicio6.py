"""
Ejercicio 5 : Clase 4 -  Manejo de colecciones y Tuplas
Autor = @davisalex22

# Encontrar la siguiente estructura
#

[(4.333333333333333, 13, 'Ángel'), (4.666666666666667, 14, 'Ana')]

Dadas las siguientes estructuras

"""

# Declaracion de Variables

paraleloA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]
nombres = ["Luis", "Ángel", "José", "Ana"]

# Union de cadenas

unionlist = list(zip(paraleloA, nombres))

# Uso de list map lambda para calcular suma y promedio

listaFinal = list(map(lambda x: (sum(x[0])/3, sum(x[0]), x[1]), unionlist))
# Muestra en Pantalla de resultados

print(list(filter(lambda x: x[0] <= 5, listaFinal)))
