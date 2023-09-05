productos=[]


productos.append("manteca") #ingresa manteca
productos.append("jugo")
productos.append("ddl")
productos.append("harina")

for producto in productos:
    print(producto)
    
print("================================")

productos.remove("jugo") #compran el jugo

for producto in productos:
    print(producto)

productos.pop(2) #compran el valor 2 del array que es harina
print("================================")
for producto in productos:
    print(producto)
productos.insert(0, "yogurth") #sumamos yogurth en la primera posicion
print("================================")
print(productos)
productos.clear() #clausuro el negocio y se quedo sin nada. Siempre va vacio entre parentesis
print("================================")
print(productos)