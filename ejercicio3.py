try:
    archivo = open("archivo_inexistente.txt", "r")
    contenido = archivo.read()
    archivo.close()

    print("Contenido del archivo:")
    print(contenido)

except FileNotFoundError:
    print("El archivo 'archivo_inexistente.txt' no se encontró.")
except Exception as e:
    print("Se produjo un error:", str(e))
