pi=3
v1=2
v2=3
v3=4

for i in range(1000001):
    calculo=4/(v1*v2*v3)
    if i%2==0:
        pi+=calculo
    else:
        pi-=calculo
    v1+=2
    v2+=2
    v3+=2

print(pi)