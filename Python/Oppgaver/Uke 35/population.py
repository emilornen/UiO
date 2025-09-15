from math import e

#lage et program som regner populasjon

bV = 50000  #kapasitet
kV = 0.2    #units h (timer)
t = 24
cV = 9      #   5000 = 50000/1+C, C=9

def n(t):
    return (bV/(1+(cV*(e**(-kV*t)))))
print(f'{n(24):.2f}')
