def ordenamiento_insercion(lista):
    # Recorrer la lista desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion = i

        # Desplazar los elementos mayores a la derecha
        while posicion > 0 and lista[posicion - 1] > valor_actual:
            lista[posicion] = lista[posicion - 1]
            posicion -= 1

        # Insertar el valor actual en la posición correcta
        lista[posicion] = valor_actual


lista = [5, 3, 8, 2, 1, 7, 6, 4]
print("Lista original:", lista)

ordenamiento_insercion(lista)
print("Lista ordenada:", lista)