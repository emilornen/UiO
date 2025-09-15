#chemical formula and corresponding molar mass

#variablene får verdiene sine
n = 2
molmassCarbon = 12.011
molmassHydrogen = 1.0079

#gjør resten av oppgaven direkte inne i løkken
for n in range(n, 10):
    m = 2*n +2
    molmassHC = n*molmassCarbon + m*molmassHydrogen
    formCH = ("C"+str(n)+"H"+str(m))
    print(f'M({formCH}) = {molmassHC:<7.3f} g/mol')