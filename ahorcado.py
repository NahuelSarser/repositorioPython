palabra = ["H","O","L","A","H"]
guiones = ["-","-","-","-", "-"]
INTENTOS = 8 
fallos = 0

#En mayusculas porque INTENTOS es una constante, no cambia su valor





while INTENTOS > fallos:
    acierto=False
    print(guiones[0],guiones[1],guiones[2],guiones[3],guiones[4])
    letra=input("Ingrese letra: ")
    for i in range(0,len(palabra),1):        
        if str(palabra[i]).lower()==str(letra).lower():                     
            print("Contiene: ",palabra[i])
            guiones[i]= letra
            acierto=True
    
    if acierto == False:
        fallos +=1
        print("Fallos: ", fallos)
    




        
    

