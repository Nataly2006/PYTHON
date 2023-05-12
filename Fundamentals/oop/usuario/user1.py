class Usuario:
    def __init__(self):
        self.name = "isidora"
        self.email = "isdora19@Renca.com"
        self.balance_cuenta = 0
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
    	self.balance_cuenta += amount
    def mostrar_balance_usuario(self,):
        self.balance_cuenta == 100
        

Usuario()
guido = Usuario()
monty = Usuario()

guido.hacer_depósito(100)
guido.mostrar_balance_usuario()

#acediendo a los atributos de la instancia
print(f"ella es {guido.name},{guido.hacer_depósito}")   #salida :isidora
print(monty.email)   #salida :isidora

""""
como se podia hacer la asignacion
"""

