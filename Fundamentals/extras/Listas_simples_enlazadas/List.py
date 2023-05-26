class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self,):
        new_node = SLNode(0)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self



"""
class SList:
        def __init__(self):
            self.head = None
        def add_to_front(self, val):	
            # agregó esta línea, toma un valor


class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None
    def add_to_front(self, val):
        new_node = SLNode(val)	
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self	
        # crea una nueva instancia de nuestra clase Node usando el valor dado"""
