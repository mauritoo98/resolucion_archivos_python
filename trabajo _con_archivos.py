def cantidadPalabras():
    archivo = open("alfabeto.txt", "r")
    linea=archivo.readline()
    linea= linea.split(" ")
    count=0
    for i in linea:
        count=count+1
    print(f"Tiene {count} palabras")

cantidadPalabras()