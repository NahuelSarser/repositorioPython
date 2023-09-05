
intentos = 3 
regusuario = int(input("Cree numero de usuario: "))
regpassword = int(input("Cree numero de clave: "))
chequear=input("Desea ingresar al sistema? si/no: ")
if chequear == "si": 
        while intentos !=0:
            usuario = int(input("Ingrese usuario: "))
            password = int(input("Ingrese password: ")) 
            if usuario == regusuario:
                if password == regpassword:
                    print("Bienvenidos al sistema")
                    intentos = 0
                else:
                    intentos = intentos - 1
                    print("Error de autenticacion, intente nuevamente, te quedan: ", intentos," intentos")
            else:
                intentos = intentos -1
                print("Error de autenticacion, intente nuevamente, te quedan: ", intentos," intentos")            
else:
    print("Fin")