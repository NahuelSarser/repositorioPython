libros=[0,1,3,10,50,-20]
maximo = libros[0]
minimo = libros[0]

for i in range(0, len(libros), 1):
    if libros[i] > maximo:
        maximo = libros[i]
    if libros[i] < minimo:
        minimo = libros[i]
    
print("El número máximo es: ", maximo)
print ("El número mínimo es: ", minimo)