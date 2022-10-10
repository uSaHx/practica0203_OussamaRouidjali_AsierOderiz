fecha = input("Introduzca su fecha de nacimiento con el formato (dd/mm/aaaa): \n")
fecha_separado = fecha.split("/")

print("Usted nacio el día", fecha_separado[0], "del mes", fecha_separado[1], "del año", fecha_separado[2])