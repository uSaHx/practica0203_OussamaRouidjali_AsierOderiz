correo_introducido = input("Introduzca su correo electronico: \n")
correo_separado = correo_introducido.split("@")
nombre_correo = correo_separado[0]
dominio = "@ceu.es"

print("Su nuevo correo es:")
print(nombre_correo + dominio)
