#Samme som forrige oppgave, men bruker en while løkke istedenfor.

s = 0
M = 3
k = 1

while k <= M:
    s += 1/(2*k)**2
    k += 1
print(s)

# Viktig å legge inn at 'k' oppdaterer seg, slik at det ikke forstetter i det uendelige.