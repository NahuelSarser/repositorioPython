import statistics

productos = ["Pizza de anchoas (Ray Liota)", "Pizza Peperoni(Joe Pesci)", "Pizza Napolitana (De Niro)", "Pizza Cuatro Quesos(Scorsese)", "Super Pizza(Goodfellas)"]
precios = [1500,1700,1800,1900,2000]
carrito = []
sumacarrito = []
cantidades = []
global sumatotal
sumatotal = 0
global seleccion

def mostrarmenu():
    for i in range(0,len(productos)):
        print(i+1, productos[i], precios[i])

def seleccionP():
    seleccion = -1
    while seleccion != 0:
        
        seleccion = int(input("Ingrese por numero la pizza que desee: "))
        cantidad = int(input("Seleccione la cantidad: "))
        if seleccion == 1:
                carrito.append(productos[0])
                cantidades.append(cantidad)
                precioseleccion = cantidad * precios[0]
                sumacarrito.append(precioseleccion)
        if seleccion == 2:
                carrito.append(productos[1])
                cantidades.append(cantidad)
                precioseleccion = cantidad * precios[1]
                sumacarrito.append(precioseleccion)
        if seleccion == 3:
                carrito.append(productos[2])
                cantidades.append(cantidad)
                precioseleccion = cantidad * precios[2]
                sumacarrito.append(precioseleccion)
        if seleccion == 4:
                carrito.append(productos[3])
                cantidades.append(cantidad)
                precioseleccion = cantidad * precios[3]
                sumacarrito.append(precioseleccion)
        if seleccion == 5:
                carrito.append(productos[4])
                cantidades.append(cantidad)
                precioseleccion = cantidad * precios[4]
                sumacarrito.append(precioseleccion)
        

        for i in range(0,len(carrito)):
            print("============================")
            print(carrito[i], "Cantidades: ", cantidades[i])
            print("============================")
            print("Precio orden parcial =  ","$", sumacarrito )

def sumafinal():
    for i in range(0,len(sumacarrito)):
        global sumatotal
        sumatotal = sumatotal + sumacarrito[i]
    print ("Ha finalizado su pedido, la suma total es de: $",sumatotal)


mostrarmenu()
seleccionP()
sumafinal()


