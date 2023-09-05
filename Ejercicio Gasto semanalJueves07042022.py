"""
Calcular el promedio semanal de gastos en un mes, ingresando como datos:
 Semana número
 Gasto semanal
El proceso termina cuando “semana número” es igual a 5.
"""

acum=0
cont=0



while cont < 5:
    gs=int(input("Ingrese el gasto semanal:"))
    
    semananum=int(input("Numero de semana:"))
    acum=acum+gs
    cont=cont+1

print("El promedio de gasto semanal es:",acum/semananum)



