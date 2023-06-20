from Tienda import Tienda
from producto import Producto

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
tienda.vender_producto(2)

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
    