class Underscore:
    def map(self, iterable, callback):
        result = []
        for item in iterable:
            result.append(callback(item))
        return result

    def find(self, iterable, callback):
        for item in iterable:
            if callback(item):
                return item
        return None

    def filter(self, iterable, callback):
        result = []
        for item in iterable:
            if callback(item):
                result.append(item)
        return result

    def reject(self, iterable, callback):
        result = []
        for item in iterable:
            if not callback(item):
                result.append(item)
        return result


# Ejemplo de uso de los métodos de la clase Underscore
_ = Underscore()

# Ejemplo de uso de map
numbers = [3, 3, 3]
mapped_numbers = _.map(numbers, lambda x: x * 2)
print(mapped_numbers)  # imprime [6, 6, 6]

# Ejemplo de uso de find
numbers = [1, 2, 3, 4, 5, 6]
found_number = _.find(numbers, lambda x: x > 5)
print(found_number)  # nos imprimira 6

# Ejemplo de uso de filter
numbers = [1, 2, 3, 4, 5, 6]
filtered_numbers = _.filter(numbers, lambda x: x % 2 == 0)
print(filtered_numbers)  # imprime: [2, 4, 6]

# Ejemplo de uso de reject
numbers = [1, 2, 3, 4, 5, 6]
rejected_numbers = _.reject(numbers, lambda x: x % 2 == 0)
print(rejected_numbers)  # imprime: [1, 3, 5]
