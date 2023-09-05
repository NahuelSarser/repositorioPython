print("Bienvenido al sistema de verificacion de apto para votaciones, recuerde que necesitara contar con DNI, estar empadronado y tener mas de 18 años")
edad = int(input("Ingrese edad: "))

if edad >= 18:
    empadronado = input("Estas empadronado? si/no: ")
    if empadronado == "si":
        dni = input("Tenes tu dni? si/no: ")
    else:
        print("No podes votar")
    if dni =="si":
        print("Podes votar")
    if dni != "si":
        cedula = input("Tenes cedula? si/no: ")
        if cedula =="si":
            print("Podes votar")
        else:
            print("no podes votar")
else:
    print("No podes votar")
