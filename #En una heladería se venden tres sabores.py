
kg=0
cantidad1=0
cantidad2=0
cantidad3=0
maxvainilla=0
total=0
chocolate=1254
vainilla=1125
frutilla=1236
cant_dia=1
dia=0
cantidad=0
print("BUENOS DIAS USUARIO ")
dia=int(input("ingrese dia de la venta "))
while dia > 0 :
    
    sabor=int(input("ingrese sabor de la venta "))
    if sabor == 1 :
    
        cantidad=int(input("ingrese cantidad de kg de la venta "))
        kg=kg+cantidad
        cantidad1=chocolate*cantidad
        
    elif sabor == 2 :
        
        cantidad=int(input("ingrese cantidad de kg de la venta "))
        cantidad2=vainilla*cantidad
        kg=kg+cantidad
   
    elif sabor == 3 :
            
        cantidad=int(input("ingrese cantidad de kg de la venta "))
        cantidad3=frutilla*cantidad
        kg=kg+cantidad
       
    dia =int(input("ingrese dia de la venta "))
        a

if cantidad1 > cantidad2 and cantidad1 > cantidad3 :
    print("el sabor mas vendido fue el chocolate")
elif cantidad2 > cantidad1 and cantidad2 > cantidad3 :
    print("el sabor mas vendido fue la vainilla")
elif cantidad3 > cantidad1 and cantidad3 > cantidad2 :
    print("el sabor mas vendido fue la frutilla")

print("la ganancia total de la heladeria fue ",cantidad1+cantidad2+cantidad3)
print("el dia que mas kg de vainilla se vendieron fue el ")
print("el promedio de pesos es ",total)


    