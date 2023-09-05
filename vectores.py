edades = [22,18,44,55,66]
i=0
maximo=0
suma = 0
minimo = edades[0]
promedio = 0
cantidad = len(edades)
while i < cantidad:
    print(edades[i])
    if(edades[i]>maximo):
        max = edades[i]
    if(edades[i]<minimo):
        minimo=edades[i]
    suma += edades[i]
    i=i+1
print(i)
promedio = sum(edades)/len(edades)
print("La suma es: ", suma)
print("El promedio de edades es de: ", promedio)
print(max)
print(minimo)

