import random
penales = 6
golr=0
golb=0
penales = 10
while penales > 0:
    penalr= random.randint(0,1)
    penales = penales -1
    penalb = random.randint(0,1)
    penales = penales -1
    if penalr == 1:
        golr=golr+1
    if penalb==1:
        golb=golb+1
if golr > golb:
    print("Gano river","River:",golr, "a", "Boca:",golb)
elif golb > golr:
    print("Gano boca","River:",golr, "a", "Boca:",golb) 




