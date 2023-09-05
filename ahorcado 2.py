palabra = ["H","O","L","A"]
guiones = ["-","-","-","-"]
INTENTOS = 8 
fallos = 0
#En mayusculas porque INTENTOS es una constante, no cambia su valor


print(guiones[0],guiones[1],guiones[2],guiones[3])
letra=input("Ingrese letra: ")
for i in range(0,len(palabra),1):        
     if str(palabra[i]).lower==str(letra).lower:            
         print("Contiene: ",palabra[i])
         guiones[i]= letra
    



        
    
