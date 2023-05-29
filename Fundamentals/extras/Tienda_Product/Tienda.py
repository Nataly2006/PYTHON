class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)

    def vender_producto(self, id):
        if id >= 0 and id < len(self.productos):
            producto_vendido = self.productos.pop(id)
            producto_vendido.print_info()
        else:
            print("¡El producto no existe!")

    def inflacion(self, porcentaje_aumento):
        for producto in self.productos:
            producto.actualizar_precio(porcentaje_aumento, True)

    def hacer_liquidacion(self, categoria, porcentaje_descuento):
        for producto in self.productos:
            if producto.categoria == categoria:
                producto.actualizar_precio(porcentaje_descuento, False)


class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado:
            self.precio += self.precio * cambio_porcentaje / 100
        else:
            self.precio -= self.precio * cambio_porcentaje / 100

    def print_info(self):
        print(f"Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: ${self.precio:.2f}")


# Prueba de las clases
tienda = Tienda("Mi Tienda")

producto1 = Producto("Camiseta", 25.99, "Ropa")
producto2 = Producto("Zapatos", 79.99, "Calzado")
producto3 = Producto("Bolso", 49.99, "Accesorios")

tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

print("Antes de la venta:")
for producto in tienda.productos:
    producto.print_info()

print("\nRealizando una venta:")
tienda.vender_producto(1)

print("\nDespués de la venta:")
for producto in tienda.productos:
    producto.print_info()

print("\nAplicando inflación del 10%:")
tienda.inflacion(10)

for producto in tienda.productos:
    producto.print_info()

print("\nHaciendo liquidación de la categoría 'Ropa' con descuento del 20%:")
tienda.hacer_liquidacion("Ropa", 20)

for producto in tienda.productos:
    producto.print_info()