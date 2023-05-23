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




cuenta1 = CuentaBancaria(.8,1000)
cuenta2=CuentaBancaria(1,5000)
cuenta3=CuentaBancaria(.25,1000000)

cuenta1.mostrar_todas_las_cuentas()