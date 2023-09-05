from re import X


fila = ["-", "-", "-"]
fila2 = ["-", "-", "-"]
fila3= ["-", "-", "-"]

print (fila)
print (fila2)
print (fila3)

columna = 0
intentos = 0

gano = False



def comprfila():
    global gano
    
    if fila[0] == "X" and fila[1] == "X" and fila[2] == "X":
        print("Gano el usuario 1")        
        gano = True

    if fila2[0] == "X" and fila2[1] == "X" and fila2[2] == "X":
        print("Gano el usuario 1")
        
        gano = True

    if fila3[0] == "X" and fila3[1] == "X" and fila3[2] == "X":
        print("Gano el usuario 1")
        
        gano = True

    
    if fila[0] == "O" and fila[1] == "O" and fila[2] == "O":
        print("Gano el usuario 2")
        
        gano = True

    if fila2[0] == "O" and fila2[1] == "O" and fila2[2] == "O":
        print("Gano el usuario 2")
        
        gano = True

    if fila3[0] == "O" and fila3[1] == "O" and fila3[2] == "O":
        print("Gano el usuario 2")
        
        gano = True

def comprcolumna():
    global gano
    
    if fila[0] == "X" and fila2[0] == "X" and fila3[0] =="X":
        print("Gano el usuario 1")
        
        gano = True
    if fila[1] == "X" and fila2[1] == "X" and fila3[1] =="X":
        print("Gano el usuario 1")
        
        gano = True
    if fila[2] == "X" and fila2[2] == "X" and fila3[2] =="X":
        print("Gano el usuario 1")
        
        gano = True
    
    if fila[0] == "O" and fila2[0] == "O" and fila3[0] =="O":
        print("Gano el usuario 2")
        
        gano = True
    if fila[1] == "O" and fila2[1] == "O" and fila3[1] =="O":
        print("Gano el usuario 2")
        
        gano = True
    if fila[2] == "O" and fila2[2] == "O" and fila3[2] =="O":
        print("Gano el usuario 2")
        
        gano = True
def comprdiagonal():
    global gano
    
    if fila[0] == "X" and fila2[1] =="X" and fila3[2] =="X":
        print("Gano el usuario 1")
        
        gano = True
    if fila[2] =="X" and fila2[1] =="X" and fila3[0] =="X":
        print("Gano el usuario 1")
        
        gano = True

    if fila[0] == "O" and fila2[1] =="O" and fila3[2] =="O":
        print("Gano el usuario 2")
        
        gano = True
    if fila[2] =="O" and fila2[1] =="O" and fila3[0] == "O":
        print("Gano el usuario 2")
       
        gano = True
        


  
while gano == False:
    columna = int(input("Ingrese numero de columna: "))
    filan = int(input("Ingrese numero de fila: "))
    if intentos % 2 == 0:
        valor = "X"
    else:
        valor = "O"

    if filan ==1:
        fila[columna-1] = valor

    if filan ==2:
        fila2[columna-1] = valor
    if filan ==3:
        fila3[columna-1] = valor

    print (fila)
    print (fila2)
    print (fila3)

    comprfila()
    comprcolumna()
    comprdiagonal()

    intentos = intentos + 1
    

















