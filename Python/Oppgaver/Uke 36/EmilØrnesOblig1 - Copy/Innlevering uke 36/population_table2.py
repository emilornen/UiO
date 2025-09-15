from math import e
#Bruker koden min fra population_table.py

#Definerer alle variabler
bV = 50000  
kV = 0.2    
t_0 = 0
t_1 = 48
n = 12
cV = 9      
h = (t_1-t_0)/n

#lager en funksjon av tid (brukt den på 3 separate oppgaver nå)
def f(t):
    return (bV/(1+(cV*(e**(-kV*t)))))

#lager tomme lister
listT = []
listN = []

#Fyller listene med verier
for t in range(n+1):
    listT.append(t*h)
    listN.append(f(t*h)) 

#Definerer overskrift til tabellene (CSS på budsjett)
m = 0
listO = ["t", "N"]
print(f'Oppgave a)\n{listO[0]:<5}{listO[1]:<5}')



# a)

nestTN = [listT, listN]

for m in range(n+1):
    print(f'{int(nestTN[0][m]):<5}{int(nestTN[1][m]):<5}')


# b)


print(f'\nOppgave b)\n{listO[0]:<5}{listO[1]:<5}')

nestTN2 = []

for m in range(n+1):
    nestTN2.append([listT[m],listN[m]])

for m in range(n+1):
    print(f'{int(nestTN2[m][0]):<5}{int(nestTN2[m][1]):<5}')