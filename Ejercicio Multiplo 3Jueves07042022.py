"""
 Ingresar números hasta un múltiplo de 3. Mostrar el último número ingresado
"""

numero=int(input("ingrese un valor:"))
anterior=numero

while numero %3!=0:
    numero=int(input("ingrese un multiplo de 3:"))

if anterior%3==0:
    print("No hay valor previo")
else:
    print(anterior)






