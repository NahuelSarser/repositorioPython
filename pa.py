print("P=450")
print("B=600")
print("los numeros de pedidos son P para la pantalla y B para la bateria")
numero=int(input(" Ingrese su numero de pedido: "))
partes= input("que parte deseas arreglar? : ")
npedido=int(input("cuanto de esta parte deseas comprar : "))
otra= input("deseas arreglar alguna otra parte: ")
npedido2=int(input("cuanto de esta parte deseas comprar : "))
total=npedido + npedido2
while numero != 0:
    if partes == "P":
        print("Eligiste pantalla", npedido)
    if partes == "B":
         print("Eligiste bateria", npedido)
print(otra)
if otra == "si":
     print("elige tu otra parte: ",npedido2)
else:
     print("seguiremos con tu compra")
total==npedido+npedido
print(total)
