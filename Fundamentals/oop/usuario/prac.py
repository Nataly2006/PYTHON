class CuentaBancaria:
    # atributo de clase
    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []
    def __init__(self, int_rate,balance):
        self.tasa_int = tasa_int
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)
    
    # método de clase para cambiar el nombre del banco
    @classmethod
    def cambiar_nombre_banco(cls,name):
        cls.nombre_banco = name
    # método de clase para obtener balance de todas las cuentas
    @classmethod
    def todos_los_balances(cls):
        sum = 0
        # utilizamos cls para referirnos a la clase 
        for account in cls.todas_las_cuentas:
        balance.cuenta += sum 
        return sum
