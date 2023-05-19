class CuentaBancaria:
    tasa_interes = 0.05

    def __init__(self, balance=0):
        self.balance = balance

    def deposito(self, cantidad):
        self.balance += cantidad
        return self

    def retiro(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print("Fondos insuficientes")
        return self

    def mostrar_info_cuenta(self):
        print("Balance:", self.balance)
        return self

    def generar_interes(self):
        interes_generado = self.balance * self.tasa_interes
        self.balance += interes_generado
        return self

    @classmethod
    def mostrar_todas_las_cuentas(cls):
        for instance in cls.__subclasses__():
            instance.mostrar_info_cuenta(instance)


cuenta1 = CuentaBancaria()
cuenta1.deposito(100).deposito(200).deposito(300).retiro(150).generar_interes().mostrar_info_cuenta()

cuenta2 = CuentaBancaria()
cuenta2.deposito(500).deposito(1000).retiro(200).retiro(300).retiro(400).retiro(500).generar_interes().mostrar_info_cuenta()

cuenta3 = CuentaBancaria()
cuenta3.deposito(700).deposito(1000).retiro(100).retiro(101).retiro(408).retiro(519).generar_interes().mostrar_info_cuenta()

CuentaBancaria.mostrar_todas_las_cuentas()