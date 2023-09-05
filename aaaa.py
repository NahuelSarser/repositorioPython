from ast import If


USER="PEPE"
PASSWORD="1234"
user=input("ingrese el usuario:")
password=input("ingrese la contraseña:")
if user==USER and password==PASSWORD :
    print (user)
else: 
    print("credenciales invalidas")


numero =int (input("ingrese numero:"))
total=0
cont=0
while numero!=0:
    print (numero)
    numero =int (input("ingrese numero:"))
    cont =cont+1
    total=total+numero

if cont !=0:
    promedio =total
    print(promedio)