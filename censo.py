import statistics


r_pesos = []
r_edades = []
r_sexos = []
retiro = 0
c_pesos = []
c_edades = []
c_sexos = []
constitucion = 0
peso = 0

def ingresodatos():
    global peso
    global edad
    global sexo
    global sede
    peso=int(input("Ingrese su peso: "))    
    edad=int(input("Ingrese su edad: "))
    sexo=input("Ingrese su sexo M o F: ")
    sede=input("Ingrese sede(retiro o constitucion): ")

def sumadatos():
    if sede == "retiro":
        if peso > 0:
            r_pesos.append(peso)
        else:
            print("Peso invalido!!")
        if edad > 0:
            r_edades.append(edad)
        else:
            print("Edad invalida!!")
        if sexo == "M" or sexo == "F":
            r_sexos.append(sexo)
        else:
            print("Sexo invalido!!")
    if sede == "constitucion":        
        if peso > 0:
            c_pesos.append(peso)
        else:
            print("Peso invalido!!")
        if edad > 0:
            c_edades.append(edad)
        else:
            print("Edad invalida!!")
        if sexo == "M" or sexo == "F":
            c_sexos.append(sexo)
        else:
            print("Sexo invalido!!") 
     

def r_promedioedad():
    promedio = statistics.mean(r_edades)
    print ("El promedio de edades tomados en la sede retiro es de: ", promedio)



while peso != -1:
    ingresodatos()
    sumadatos()
    
    

    
for i in range(0, len(r_pesos)):
    print(i+1,"Retiro Peso",  r_pesos[i],"Edad", r_edades[i], "Sexo", r_sexos[i])
for i in range (0,len(c_pesos)):
    print (i+1, "Constitucion Pesos", c_pesos[i], "Edad", c_edades[i], "Sexo", c_sexos[i])

r_promedioedad()




