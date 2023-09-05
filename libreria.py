precio=1
preciolibros=0
preciojuguete=0
preciocontartescritorio=0
stocklibros=0
stockcontartescritorio=0
stockjuguete=0
while precio !=0:
    articulo = int(input("Ingrese tipo de articulo siendo 1 libros, 2 articulos de escritorio, 3 juguetes, o 0 para salir: "))
    if articulo==0:
        print("Fin")
        break
    precioarticulo = int(input("Ingrese precio del articulo: "))        
    nombrearticulo = input("Ingrese nombre de articulo: ")
    stockarticulo = int(input("Ingrese stock del articulo: "))
    if articulo==1:
        preciolibros=preciolibros+precioarticulo
        stocklibros=stocklibros+stockarticulo
    if articulo==2:
        preciocontartescritorio=preciocontartescritorio+precioarticulo
        stockcontartescritorio=stockcontartescritorio+stockarticulo
    if articulo==3:
        preciojuguete=preciojuguete+precioarticulo
        stockjuguete=stockjuguete+stockarticulo
seleccion=int(input("Ingrese que desea ver siendo 1 cantidad de cada articulo, 2 nombre del juguete mas barato, 3 cuanto dinero hay en stock"))
if seleccion ==1:
    print("Hay", stocklibros, "Libros", stockcontartescritorio, "Articulos de escritorio", stockjuguete, "Juguetes")
if seleccion ==2:
       
    
