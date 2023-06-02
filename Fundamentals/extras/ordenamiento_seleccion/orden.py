def ordenamiento_seleccion(lista):
    # Recorrer la lista de 0 a n-1
    for i in range(len(lista)):
        # Encontrar el índice del valor mínimo en el resto de la lista
        indice_minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        # Intercambiar el valor mínimo con el valor en la posición actual
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]


lista = [5, 3, 8, 2, 1, 7, 6, 4]
print("Lista original:", lista)

ordenamiento_seleccion(lista)
print("Lista ordenada:", lista)