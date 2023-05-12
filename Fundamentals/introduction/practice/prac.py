
class Usuario:
    # los atributos de clase se definen en la clase
    nombre_banco = "Primer Dojo Nacional"
    # ¡ahora nuestro método tiene 2 parámetros!
    def __init__(self , name, email_address):
    	# los asignamos en consecuencia
        self.name = name
        self.email = email_address
    	# el balance de la cuenta se establece en $0
        self.balance_cuenta = 0
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
    	self.balance_cuenta += amount

guido = Usuario("Guido van Rossum", "  guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")

rasput = Usuario("Rasputin  ", "guido@python.com")
urs = Usuario("Rusia urs", "monty@python.com")

cobra = Usuario("Orochimaru  ", "guido@python.com")
loca = Usuario("Python", "monty@python.com")

emo = Usuario("Sasuke  ", "guido@python.com")
vengador = Usuario("uchiha", "monty@python.com")

princesa= Usuario("Hinata  ", "guido@python.com")
luna = Usuario("hyuga", "monty@python.com")

mensaje = "   soy un ninja y mi correo es  "
texto = "  soy un renegado"

guido.hacer_depósito(100)

print(f"hola {mensaje} guido@python.com" )	# salida: Guido van Rossum
print(monty.name + mensaje)	# salida: Monty Python
print(rasput.name + urs.name +texto)
print(cobra.name + loca.name + texto)
print(emo.name + vengador.name + texto)
print(princesa.name + luna.name +mensaje)





