class Usuario:
    # declarando un atributo de clase
    nombre_banco = "Primer Dojo Nacional"		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 0

guido = Usuario()
monty = Usuario()
guido.nombre_banco = "Dojo Credit Union"
print(guido.nombre_banco) # salida: Dojo Credit Union 
print(monty.nombre_banco) # salida: Primer Dojo Nacional

Usuario.nombre_banco = "Banco del Dojo"
print(guido.nombre_banco) # salida: Banco del Dojo
print(monty.nombre_banco) # salida: Banco del Dojo



