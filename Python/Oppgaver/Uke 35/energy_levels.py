#Energien til forskjellige nivå

mV = 9.1094e-31         #Elektronmassen, kg
eV = 1.6022e-19         #Elementærladningen, C
epsilonV = 8.8542e-12   #Elektriske tomromspermittiviteten
hV = 6.6261e-34         #J s
constant = (-((mV*eV**4)/(8*epsilonV**2*hV**2)))

# n = 1
# while n <= 20:
#     eFormula = constant*(1/n**2)
#     print(f'{eFormula:.2e}')
#     n += 1


ni = 1
nf = 1

for ni in range(1, 6):
    for nf in range(1, 6):
        deltaEFormula = constant*((1/ni**2)-(1/nf**2))
        print(f'{deltaEFormula:<15.2e}',end="")
    print("")