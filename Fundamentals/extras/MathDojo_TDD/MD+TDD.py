class MathDojo:
    def __init__(self):
        self.result = 0

    def sumar(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def restar(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self


def reverse_list_func(lst):
    return lst[::-1]


def is_palindrome(word):
    return word == word[::-1]


def coins(cents):
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    return [quarters, dimes, nickels, cents]


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Ejecutar pruebas para MathDojo
md = MathDojo()
x = md.sumar(2).sumar(2, 5, 1).restar(3, 2).result
print(x)  # Output: 5

# Ejecutar pruebas para las demás funciones
assert reverse_list_func([1, 3, 5]) == [5, 3, 1]
assert reverse_list_func([2, 4, 6, 8]) == [8, 6, 4, 2]
assert reverse_list_func(['a', 'b', 'c', 'd']) == ['d', 'c', 'b', 'a']

assert is_palindrome("racecar") == True
assert is_palindrome("level") == True
assert is_palindrome("hello") == False
assert is_palindrome("madam") == True
assert is_palindrome("python") == False

assert coins(87) == [3, 1, 0, 2]
assert coins(50) == [2, 0, 0, 0]
assert coins(99) == [3, 2, 0, 4]
assert coins(75) == [3, 0, 0, 0]
assert coins(32) == [1, 0, 1, 2]

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(6) == 720