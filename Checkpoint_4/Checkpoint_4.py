from decimal import *

# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
flotante = 1.1
integro = 2
decimall = Decimal(1) / Decimal(7)
diccionario = {"Nombre": "Jokin", "Apellido": "Gorrotxategi"}

print(lista, tupla, flotante, integro, decimall, diccionario)
print(lista.__class__, tupla.__class__, flotante.__class__, integro.__class__, decimall.__class__, diccionario.__class__)

# Exercise 2: Round your float up.

import math
arriba = math.ceil(flotante)
print(arriba)

# Exercise 3: Get the square root of your float.

raiz_cuadrada = math.sqrt(flotante)
print("raiz cuadrada", raiz_cuadrada)

# Exercise 4: Select the first element from your dictionary.

primer_elemento = list(diccionario.keys())[0]
print("Primer elemento del diccionario", diccionario[primer_elemento])

# Exercise 5: Select the second element from your tuple.

segundo_elemento = tupla[1]
print("Segundo elemento de la tupla", segundo_elemento)

# Exercise 6: Add an element to the end of your list.
lista.append("Nuevo elemento")
print("Lista con nuevo elemento",lista)

print("Dos formas de agregar un elemento a la lista", lista + ["Otro más"])

# Exercise 7: Replace the first element in your list.

lista[0] = "Pero capachao?"
print("Lista con el primer elemento reemplazado", lista)

# Exercise 8: Sort your list alphabetically.
nueva_lista_para_odenar = ["hiru", "bi", "bat"]
nueva_lista_para_odenar.sort()
print("Lista ordenada alfabeticamente", nueva_lista_para_odenar)

# Exercise 9: Get the number of elements in your list.

tupla += (26890,)
print("Tupla con un elemento más", tupla)