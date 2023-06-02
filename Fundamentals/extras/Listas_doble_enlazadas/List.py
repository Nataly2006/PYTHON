class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, valor):
        nuevo_nodo = Nodo(valor)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def eliminar_nodo(self, valor):
        if self.cabeza is None:
            return

        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return

        nodo_actual = self.cabeza
        while nodo_actual.siguiente is not None:
            if nodo_actual.siguiente.valor == valor:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return
            nodo_actual = nodo_actual.siguiente

    def insertar_nodo(self, valor, valor_anterior):
        nuevo_nodo = Nodo(valor)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.valor == valor_anterior:
                nuevo_nodo.siguiente = nodo_actual.siguiente
                nodo_actual.siguiente = nuevo_nodo
                return
            nodo_actual = nodo_actual.siguiente

    def imprimir_lista(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

# Ejemplo de uso
lista = ListaEnlazada()

lista.agregar_nodo(1)
lista.agregar_nodo(2)
lista.agregar_nodo(3)

print("Lista original:")
lista.imprimir_lista()

lista.eliminar_nodo(2)

print("Lista después de eliminar el nodo 2:")
lista.imprimir_lista()

lista.insertar_nodo(4, 1)

print("Lista después de insertar el nodo 4 después del nodo 1:")
lista.imprimir_lista()