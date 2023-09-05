def copiar(v,x,n):
    for i in range(n,len(v)):
        x.append(v[i])
    

def intercalar(v1,v2):
    vf = []
    if len(v1) < len(v2):
        n = len(v1)
    else:
        n = len(v2)
    
    for i in range(n):
        vf.append(v1[i])
        vf.append(v2[i])
    
    if len(v1) < len(v2):
        copiar(v2,vf,n)
    else:
        copiar(v1,vf,n)
    
    return vf

 #-------------------------------------------   

cant = int(input("Ingresar tamaño del arreglo v1:"))
v1 = []*cant

cant2 = int(input("Tamaño de larreglo v2:"))


for i in range(len(v)):
    v[i] = int(input("valor"))

s = intercalar()