class Node:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_nodo(self, valor):
        nuevo_nodo = Node(valor)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar_nodo(self, valor):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.valor == valor:
                if nodo_actual.anterior is not None:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                else:
                    self.cabeza = nodo_actual.siguiente
                if nodo_actual.siguiente is not None:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                else:
                    self.cola = nodo_actual.anterior
                return
            nodo_actual = nodo_actual.siguiente

    def insertar_nodo(self, valor, valor_anterior):
        nuevo_nodo = Node(valor)
        
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.valor == valor_anterior:
                nuevo_nodo.siguiente = nodo_actual
                nuevo_nodo.anterior = nodo_actual.anterior
                if nodo_actual.anterior is not None:
                    nodo_actual.anterior.siguiente = nuevo_nodo
                else:
                    self.cabeza = nuevo_nodo
                nodo_actual.anterior = nuevo_nodo
                return
            nodo_actual = nodo_actual.siguiente

    def imprimir_lista(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

    def es_lista_enlazada_circular(self):
        if self.cabeza is None:
            return False
        
        nodo_rapido = self.cabeza
        nodo_lento = self.cabeza

        while nodo_rapido is not None and nodo_rapido.siguiente is not None:
            nodo_rapido = nodo_rapido.siguiente.siguiente
            nodo_lento = nodo_lento.siguiente

            if nodo_rapido == nodo_lento:
                return True

        return False

    def obtener_mitad_lista(self):
        if self.cabeza is None:
            return None
        
        nodo_rapido = self.cabeza
        nodo_lento = self.cabeza

        while nodo_rapido is not None and nodo_rapido.siguiente is not None:
            nodo_rapido = nodo_rapido.siguiente.siguiente
            nodo_lento = nodo_lento.siguiente

        return nodo_lento.valor

    def eliminar_duplicados(self):
        if self.cabeza is None:
            return

        valores = set()
        nodo_actual = self.cabeza
        nodo_anterior = None

        while nodo_actual is not None:
            if nodo_actual.valor in valores:
                nodo_anterior.siguiente = nodo_actual.siguiente
                if nodo_actual.siguiente is not None: