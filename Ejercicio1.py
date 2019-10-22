"""
Ejercicio 1 : Clase 4
Autor = @davisalex22
"""
# Declaracion de Listas

listaA = [10, 2, 3, 4]
listaB = ["a", "b", "c", "d"]

# Uso de list, zip y sorted

listaFinal = list(zip((sorted(listaA)), (sorted(listaB, reverse=True))))

# Muestra en pantalla de resultados

print(listaFinal)
print(max(listaFinal))
