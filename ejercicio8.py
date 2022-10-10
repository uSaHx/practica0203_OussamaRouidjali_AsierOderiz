precio = input("Introduzca el precio del producto con dos decimales: \n")
precio_separado = precio.split(".")

print(precio_separado[0], "euros", precio_separado[1], "centimos")
