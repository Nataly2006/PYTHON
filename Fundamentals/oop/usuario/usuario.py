class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def hacer_deposito(self, amount):
        self.amount += amount

    def hacer_retiro(self,amount):
        self.amount -= amount

    def mostrar_balance_usuario(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_dinero(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.mostrar_balance_usuario()
        user.mostrar_balance_usuario()


Haku = User("Haku")
isidora = User("isidora")
itachi = User("itachi")

Haku.hacer_deposito(100)
Haku.hacer_deposito(200)
Haku.hacer_deposito(50)
Haku.hacer_retiro(45)
Haku.mostrar_balance_usuario()

isidora.hacer_deposito(1000)
isidora.hacer_deposito(1000)
isidora.hacer_retiro(500)
isidora.hacer_retiro(300)
isidora.mostrar_balance_usuario()

itachi.hacer_deposito(1500)
itachi.hacer_retiro(1000)
itachi.hacer_retiro(5000)
itachi.hacer_retiro(3000)
itachi.mostrar_balance_usuario()


itachi.transfer_dinero(361, Haku)