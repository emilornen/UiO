#Emil Ørnes

# s = 0
# M = 3
# for i in range(M):
#     s += 1/2*k**2
# print(s)

# 1) Det finnes ingen 'k' variabel.
# 2) Python leser koden rett frem, slik at formelen er tolket feil. Det må være parantes rundt 2*k, ellers blir kun k^2.
# 3) 'i' er ikke definert i formelen vår. Regnestykket utføres 3 ganger så 'rangen' blir fra k til M+1.

s = 0
M = 3
k = 1

for k in range(k, M+1):
    s += 1/(2*k)**2
#   print(k)
#   print(s)
print(s)

#Forsøkte begge metoder, men feilen var åpenbar når en regnet på output for hver enkelt 'k' verdi.