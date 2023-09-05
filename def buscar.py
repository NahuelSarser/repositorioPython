def buscar_posicion(v,x):
    n = len(v)
    i = 0
    while i < n and v[i] != x:
        i += 1
    if i == n:
        return -1
    
    return i

a = [10,5,1,0,20,1]
s = buscar_posicion(a,1)
print (s)
