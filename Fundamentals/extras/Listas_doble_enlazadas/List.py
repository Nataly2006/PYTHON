class Nodo:


def __init__(self, valor):
self.valor = valor
self.siguiente = 
self.valor = valor



None


class ListaEnlazada:


def __init__(self):
self.cabeza = 

None




def agregar_final(self, valor):
nuevo_nodo = Nodo(valor)

nuevo_nodo = Nodo(valor)


nuevo_nodo = Nodo(valor)


if not self.cabeza:
self.cabeza = nuevo_nodo

self.cabeza = nuevo_nodo

else:
actual = self.cabeza

actual = self.cabeza



while actual.siguiente:
actual = actual.siguiente
actual.siguiente = nuevo_nodo


actual = actual.siguiente


actual = actual.siguiente


def eliminar(self, valor):
if not self.cabeza:
return






if self.cabeza.valor == valor:
self.cabeza = self.cabeza.siguiente

self


return

actual = self.cabeza
previo = 

actual = self.cabeza






None


while actual and actual.valor != valor:
previo = actual
actual = actual.siguiente


previo = actual


previo = actual


if actual:
previo.siguiente = actual.siguiente


previo.siguiente = actual.siguiente



previo.siguiente = actual.siguiente

def insertar(self, valor, nuevo_valor):
nuevo_nodo = Nodo(nuevo_valor)


nuevo_nodo = Nodo(nuevo_valor)



if not self.cabeza:
self.cabeza = nuevo_nodo

self.cabeza =
return






if self.cabeza.valor == valor:
nuevo_nodo.siguiente = self.cabeza
self.cabeza = nuevo_nodo

nuevo_nodo.siguiente = self.cabeza
self.cabeza = nuevo_nodo


nuevo_nodo.siguiente = self.cabeza
self.cabeza = nuevo_nodo

nuevo_nodo.siguiente = self.cabeza


nuevo_nodo.siguiente = self.cabeza


return

actual = self.cabeza


actual = self.cabeza






while actual:


if actual.valor == valor:
nuevo_nodo.siguiente = actual.siguiente
actual.siguiente = nuevo_nodo

nuevo_nodo.siguiente = actual.siguiente
actual.siguiente = nuevo_nodo


nuevo_nodo.siguiente = actual.siguiente


nuevo_nodo.siguiente =

nuevo


return
actual = actual.siguiente


actual = actual.siguiente



actual = actual.siguiente

actual = actual.s


def imprimir(self):
actual = self.cabeza

actual = self.cabeza

actual = self.cabe


while actual:


print(actual.valor, end=" -> ")
actual = actual.siguiente

actual = actual.siguiente


actual = actual.siguiente


print("None")


# Ejemplo de uso
lista = ListaEnlazada()


lista
# Agregar nodos al final de la lista
lista.agregar_final(
lista
5)
lista.agregar_final(
lista
10)
lista.agregar_final(
lista
15)
lista.imprimir() 
lista.imprimir()

lista
# Resultado: 5 -> 10 -> 15 -> None

# Eliminar un nodo existente
lista.eliminar(10)
lista.imprimir() 
lista.imprimir() 

lista.imprimir

lista
# Resultado: 5 -> 15 -> None

# Insertar un nodo entre nodos existentes
lista.insertar(
lista
5, 7)
lista.imprimir() 
lista.imprimir()

lista.imprimir

lista
# Resultado: 5 -> 7 ->