pantalla=450
bateria=600
tipo1="p"
tipo2="b"
precio=0
cont=0
cont_bateria=0
monto_total=0
numero_pedido=int(input("ingrese numero pedido: "))
while numero_pedido !=0:
    cantidad=int(input("Ingrese cantidad de partes: "))
    while cantidad < 0:
        cantidad=int(input("Ingrese cantidad de partes: "))
tipo=input("Ingrese tipo")
while tipo !="b" and tipo != "p":
    tipo=input("ingrese tipo")