import numpy as np

#lage coulomb formel og gravitasjons kraft formel og sammenligne for et atom

kV = 9*10**9
eV = 1.6*10**-19
gV = 6.7*10**-11
mpV = 1.7*10**-27
meP = 9.1*10**-31
rV = 5.3*10**-11

fC = kV*(eV**2/rV**2)
fG = gV*((mpV*meP)/(rV**2))

print(f'Coulombs force equals to {fC:.1e}N and the Gravitational force equals to {fG:.1e}N.\nTHe ratio between them are {fC/fG:.1e}.')