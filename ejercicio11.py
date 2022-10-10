nombre_producto = input("Introduzca el nombre del producto: \n")
precio = float(input("Introduzca el valor del producto: \n"))
cantidad = int(input("Introduzca cuantos productos desea: \n"))
total = precio * cantidad

print("El producto es {nombre_producto}, a un precio de {precio:6.2f} euros, y una cantidad de {cantidad:3d} unidades, por un precio total de {total:8.2f} euros"
      .format(nombre_producto = nombre_producto, precio = precio, cantidad = cantidad, total = total))