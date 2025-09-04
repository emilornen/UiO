#Ideal Gas law

pV = 100000     # Trykk
vV = 4 * 1e-3   # Volum fra liter til m^3
rV = 8.314      # konstant (idk hva det er)
nV = 0          # Stoffmengde
tV = 273        # Temperatur (absolutt) kelvin

# a)

nV = (pV*vV)/(tV*rV)
print(f'Stoffmengden i ballongen, ved standardbetingelser, er {nV:.2f} mol')


# b)

mV = 7.074  # masse
molarMass = mV/nV

print(f'Den molare massen til gassen er {molarMass:.4f} g/mol')


# c) Jeg tror det er argon pga Molar masse er nesten 40 og argon er u=39.9 noe
