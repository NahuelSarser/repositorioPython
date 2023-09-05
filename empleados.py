cantempleados = int(input("Ingresar cantidad de empleados: "))
cat1=0
cat2=0
cat3=0
cat4=0
sueldobruto=0
while cantempleados > 0:
    categoria = int(input("Ingrese categoria: (1,2,3,4): "))
    if categoria==1:
        horas=int(input("Ingrese cantidad de horas: "))
        sueldobruto=sueldobruto+(150*horas)
        sueldoneto=sueldoneto+(sueldobruto*0,17)
        cantempleados -=1
        cat1+=1
    elif categoria==2:
        horas=int(input("Ingrese cantidad de horas: "))
        sueldobruto=sueldobruto+(200*horas)
        sueldoneto=sueldoneto+(sueldobruto*0,17)
        cantempleados -=1
        cat2+=1
    elif categoria==3:
        horas=int(input("Ingrese cantidad de horas: "))
        sueldobruto=sueldobruto+(250*horas)
        sueldoneto=sueldoneto+(sueldobruto*0,17)
        cantempleados -=1
        cat3+=1
    elif categoria==4:
        horas=int(input("Ingrese cantidad de horas: "))
        sueldobruto=sueldobruto+(280*horas)
        sueldoneto=sueldoneto+(sueldobruto*0,17)
        cantempleados -=1
        cat4+=1
print("El sueldo bruto abonado es de: $",sueldobruto)
print("Cantidad de empleados en categoria 1: ",cat1, "Cantidad de empleados en categoria 2: ", cat2, "Cantidad de empleados en categoria 3: ", cat3, "Cantidad de empleados en categoria 4: ", cat4)
    