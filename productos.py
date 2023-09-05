from math import prod


productos = ["coca", "sal", "fideos", "harina"]
carrito = []

def listar_productos():
    print ("Nuestros productos")
    for i in range (0, len(productos)):
        print (i, ".  " + productos[i])

def seleccionar_productos():
    global i_prod   
    i_prod = int(input("Seleccionar producto: "))
    return prod
    

def agregar_productos():
    #carrito.append(prod)
    #print("Mi carrito =======")
    #for producto in carrito:
        #print(producto)
    if i_prod == 0:
        carrito.append("coca")
        print("Sumaste coca")
        
    if i_prod == 1:
        carrito.append("sal")
        print("Sumaste sal")
    if i_prod == 2:
        carrito.append("fideos")
        print("Sumaste fideos")
    if i_prod == 3:
        carrito.append("harina")
        print("Sumaste harina")

listar_productos()
seleccionar_productos()
agregar_productos()

