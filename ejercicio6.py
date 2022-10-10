frase = input("Introduzca una frase: \n")
vocal = input("Introduzca la vocal que quiere resaltar: \n")
vocal_mayus = vocal.upper()
frase_remplazada = frase.replace(vocal, vocal_mayus)
print(frase_remplazada)

