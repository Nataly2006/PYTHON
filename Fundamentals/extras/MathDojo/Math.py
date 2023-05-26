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

# crear una instancia:
md = MathDojo()

x = md.sumar(2).sumar(2, 5, 1).restar(3, 2).result
print(x)  # Output: 5

# ejecuta cada uno de los métodos unas cuantas veces más y verifica el resultado

