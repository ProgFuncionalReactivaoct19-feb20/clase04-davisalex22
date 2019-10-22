"""
Ejercicio 4 : Clase 4 -  Manejo de colecciones y Tuplas
Autor = @davisalex22

Encontrar la siguiente estructura

[(16.333333333333332, 'Ángel'), (16.666666666666668, 'José'), (13.0, 'Ana')]

Dadas las siguientes estructuras:
"""

# Declaracion de Variables

paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]

# Calculo de los promedios con funcion lambda

prom = map(lambda x: (x[0] + x[1] + x[2])/3, paraleloA)

# Muestra en pantalla de resultado

print(list(zip(prom, nombres)))
