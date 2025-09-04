from math import sqrt 
# verdensrom og hastighet

# a)

names = ["Hastighet", "Bevegelsesmengde", "Relativistisk Bevegelsesmenge"]
print(f'{names[0]:<11}{names[1]:<18}{names[2]:<20}\n')
n = 0.1
cV = 3*10**8
mV = 1200

while n <= 0.9:
    vV = n*cV
    yV = 1/(sqrt(1-(vV**2/cV**2)))
    pResultR = mV * vV * yV
    pResultN = vV * mV
    print(f'{vV:<11.1e}{pResultN:<18.1e}{pResultR:<20.1e}')
    n = n + 0.1
