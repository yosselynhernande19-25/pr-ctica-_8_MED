nombres = []
while True:
    nombre = input("Ingresa un nombre (o presiona Enter para terminar): ")
    if nombre:
        nombres.append(nombre)
    else:
        break

with open("nombres.txt", "w") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")

print("Los nombres se han guardado en el archivo 'nombres.txt'.")
