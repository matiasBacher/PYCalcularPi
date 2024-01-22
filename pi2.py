divisor=3
annadir=2

pi=4

for i in range(100000001):
    if i%2==0:
        pi-=(4/divisor)
    else:
        pi+=(4/divisor)
    divisor+=annadir

print(pi)
