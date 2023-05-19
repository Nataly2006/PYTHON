""" 1 Actualizar valores en diccionarios y listas """
# Codigo 1
x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)
# imprimira [[5, 2, 3], [15, 8, 9]]

# Codigo 2
estudiantes = [{'first_name': 'Michael', 'last_name': 'Jordan'}, {'first_name': 'John', 'last_name': 'Rosales'}]
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)
# imprimira [{'first_name': 'Michael', 'last_name': 'Bryant'}, {'first_name': 'John', 'last_name': 'Rosales'}]

# Codigo 3
directorio_deportes = {'basketball': ['Kobe', 'Jordan', 'James', 'Curry'], 'fútbol': ['Messi', 'Ronaldo', 'Rooney']}
directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)
# imprimira  {'basketball': ['Kobe', 'Jordan', 'James', 'Curry'], 'fútbol': ['Andrés', 'Ronaldo', 'Rooney']}

# Codigo 4
z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30
print(z)
# imprimira [{'x': 10, 'y': 30}]

""" 2 Iterar a través de una lista de diccionarios """

def iterateDictionary(some_list):
    for item in some_list:
        output = ""
        for key, value in item.items():
            output += f"{key} - {value}, "
        output = output.rstrip(", ")  # Elimina la coma al final
        print(output)

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(estudiantes)

""" 3 Obtener valores de una lista de diccionarios """

def iterateDictionary2(key_name, some_list):
    for item in some_list:
        if key_name in item:
            print(item[key_name])

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary2('first_name', estudiantes)
# Output:
# Michael
# John
# Mark
# KB

iterateDictionary2('last_name', estudiantes)
# Output:
# Jordan
# Rosales
# Guillen
# Tonel

""" 4 Iterar a través de un diccionarios con valores de lista """

def printInfo(some_dict):
    for key, values in some_dict.items():
        print(f"{len(values)} {key.upper()}")
        for value in values:
            print(value)
        print()

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
# salida:

"""
7 UBICACIONES
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORES
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""
