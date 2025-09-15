from math import e
#Bruker koden min fra population.py

#Variabler tildeles verdier
bV = 50000  
kV = 0.2    
t_0 = 0
t_1 = 48
n = 12
cV = 9      
h = ((t_1-t_0)/n)

#definerer funksjonen
def f(t):
    return (bV/(1+(cV*(e**(-kV*t)))))

#lager tomme lister
listT = []
listN = []

#putter verdier inn i listene
for t in range(n+1):
    listT.append(t*h)
    listN.append(f(t*h)) 

#lager en oversikt mtp tabellen
m = 0
listO = ["t", "N"]
print(f'{listO[0]:<8}{listO[1]:<5}')

#printer verdiene ved hjelp av en for-løkke
for m in range(n+1):
    print(f'{listT[m]:<8}{listN[m]:<5.2f}')