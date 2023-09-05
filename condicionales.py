aforo = 0
while aforo < 10:    
    edad =int(input("Ingresa tu edad: "))
    if edad >= 18:
        print("Podes pasar")
        aforo = aforo + 1
        print("Quedan", 10-aforo,"lugares")
    elif edad ==17:
        print("Podes pasar acompañado")
        aforo = aforo + 2
        print("Quedan", 10-aforo,"lugares")
    else:
        mayor_edad = input("Mayor edad acompaña? s/n: ")
        emancipado = input("Sujeto emnacipado? s/n: ")
        if mayor_edad =="s" or emancipado =="s":
            print ("Podes pasar")
            aforo = aforo + 2
            print("Quedan", 10-aforo,"lugares")
        else:
            print("No podes pasar")
print("Fin de aforo")