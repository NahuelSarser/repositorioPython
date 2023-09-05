ventas = [1500, 2000, 900, 2500, 1800, 2500,1000]

def buscar_max(v):
    maximo = v[0]

    for i in range(len(v)):
        if v[i] > maximo:
            maximo = v[i]
    
    return maximo

def buscar_maximoss(v):
    dias = []
    valor_maximo = buscar_max(v)

    for i in range(len(v)):
        if v[i] == valor_maximo:
            dias.append(i)
    
    return dias