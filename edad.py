edad = 0
while edad != -1:
    edad = int(input("Ingrese edad (Ingrese -1 para terminar operacion): "))
    if edad == -1:
        print ("Fin de operacion")
    if edad <= 18 and edad >= 0:
        print("Su arancel corresponde a: $1.000 ")
    elif edad > 18 and edad <= 28:
        print ("Su arancel corresponde a $2.000")
    elif edad > 28 and edad <= 38:
        print ("Su arancel corresponde a $2.500")
    elif edad > 38 and edad <= 48:
        print ("Su arancel corresponde a $3.000")
    elif edad >48 and edad <=58:
        print ("Su arancel corresponde a $3.200")
    elif edad > 58 and edad <= 68:
        print ("Su arancel corresponde a $2.100")
    elif edad > 68 and edad <= 78:
        print ("Su arancel corresponde a $500")
    elif edad > 78 and edad <= 88:
        print ("Su arancel corresponde a $250")
    elif edad > 88 and edad <= 98:
        print ("Su arancel corresponde a $100")
    elif edad > 98 and edad <= 108:
        print("Su arancel corresponde a $50")
    elif edad > 108:
        print("Todavia seguis vivo?")
