class CuentaBancaria:
    cuentas =[]

    def __init__(self,interes,balance):
        self.balance = balance
        self.interes = interes
        CuentaBancaria.cuentas.append(self)

    def deposito(self, cantidad):
        self.balance += cantidad
        return self

    def retiro(self, cantidad):
        if(self.balance - cantidad) >= 0:
            self.balance -= cantidad
        else:
            print(f"Fondos insuficientes su monto es ${self.balance}")
        return self

    def mostrar_info_cuenta(self):
        print(f"Su saldo de cuenta es: ${self.balance}")
        return self
    
    def generar_interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interes)
        return self

    @classmethod
    def mostrar_todas_las_cuentas(cls):
        for cuentas in cls.cuentas:
            cuentas.mostrar_info_cuenta()

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

    def transferir_dinero(self,amount,user):
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

itachi.transferir_dinero(361, Haku)


cuenta1 = CuentaBancaria(.8,1000)
cuenta2=CuentaBancaria(1,5000)
cuenta3=CuentaBancaria(.25,1000000)

cuenta1.mostrar_todas_las_cuentas()