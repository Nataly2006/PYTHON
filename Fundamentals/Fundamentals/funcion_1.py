#Codigo 1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# este codigo nos imprimira 5

#Codigo 2
def number_of_military_branches ():
    return 5

#Codigo 3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold ())

#Codigo 4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

#Codigo 5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# !este codigo imprime 5,None

#Codigo 6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#! >>> 3,5, Error can't add NoneTypes
""" Este hermoso codigo da error por que """

#Codigo 7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#imprimira "25"

#Codigo 8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#imprimira 100, 10

#Codigo 9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# imprime 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# imprime 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) +
number_of_days_in_a_week_silicon_or_triangle_sides(5,3)  )
# imprime 21

#Codigo 10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# este codigo imprimira 8

#Codigo eleven
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# imprime  500,500, 300, 500

#Codigo 12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
""" imprime  500,500, 300, 500 """

#Codigo Thirteen
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b =foobar()
print(b)
"""imprime  500,500, 300, 300 """

#Codigo 14
def foo():
    print (1)
    bar()
    print(2)
def bar():
    print(3)
foo()
""" este codigo  imprimira 1, 3,2 """

#Codigo 15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

""" imprimira 1,3,5,10 """
