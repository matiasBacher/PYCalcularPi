tope=10000
x=-tope
y=-tope
areaCirculo=0


while y<=tope:
    while x<=tope:
        hipotenusa=(x**2+y**2)**0.5
        if hipotenusa<=tope:
            areaCirculo+=1
        x+=1
    y+=1
    x=-tope

vPi=areaCirculo/tope**2

print (vPi)