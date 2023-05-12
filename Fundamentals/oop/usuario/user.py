class Usuario:
    def __init__(self):
        self.name = "isidora"
        self.email = "isdora19@Renca.com"
        self.balance_cuenta = 0
    def hacer_depósito(self, amount):
    	self.balance_cuenta += amount
    def hacer_retiro(self, amount):
    	self.balance_cuenta -= amount
    def mostrar_balance_cuenta(self, amount):
        print(f"Este es el saldo de cuenta {self.balance_cuenta} para nuestro usuario {self.name}")

Usuario = Usuario()