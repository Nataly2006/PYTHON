# 1. TAREA: imprime "Hola, mundo"
print( "Hola, Mundo")

# 2. imprime "Hola, Nataly" con el nombre en una variable
name = "Nataly"
print( "Hola, " + name )  # con una coma y un +

# 3. imprimir "Hola 42!" con el número en una variable
name = 42
print("Hola " + str(42) + "!" )	# con una coma
print("Hola " + str(42) + --  "!" )  # con una +	-- este debería arrojar un error!

# 4. imprimir "Amo comer Lentejas y pizza" con las comidas en variables
fave_food1 = "lentejas"
fave_food2 = "pizza"
print("Amo comer y {} {} ".format( fave_food1, fave_food2))# con .format()
print(f"Amo comer y {fave_food1} {fave_food2}") # con una cadena f

