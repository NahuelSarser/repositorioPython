edades = [22,18,44,55,66]
i=0
maximo=0
suma = 0
minimo = edades[0]

promedio = 0
cantidad = len(edades)
#while i < cantidad:
 #   print(edades[i])
  #  if(edades[i]>maximo):
   #     max = edades[i]
    #if(edades[i]<minimo):
     #   minimo=edades[i]
    #suma += edades[i]
    #i=i+1
#print(i)
promedio = sum(edades)/len(edades)
#print("La suma es: ", suma)
print("El promedio de edades es de: ", promedio)
#print(max)
#print(minimo)

for edad in edades:
    print(edad)
    if(edad>maximo):
        max = edad
    if(edad<minimo):
        minimo=edad
    suma += edad
print(max)
print(minimo)

edades.append(0) #suma un nuevo numero al array al ultimo puesto
edades.insert(2,100) #asigno un valor al puesto 3 de 100
edades.remove(100) #borra el item de valor 100 ( si hay 3 personas con el valor de 100 solo borra el primero)
edades.pop(3) #borra el valor de una posicion puntual, todos se corren un lugar mas
edades.clear() #elimina el vector, entre parentesis va vacio porque borra todo. tambien sirve para inicializar un vector vacio, luego se le asignan valores.



    
