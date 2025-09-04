from math import *

# Quadratic root formula

a = int(input("Skriv inn en verdi for A "))
b = int(input("Skriv inn en verdi for B "))
c = int(input("Skriv inn en verdi for C "))
if (b**2) < (4*a*c):
    print("Det går ikke an å ta røtter av minus-verdier!")

else:
    arrayABC = [a, b, c]
    root = sqrt((b**2) - (4*a*c))
    formulaPluss = ((-b + root)/2*a)
    formulaMinus = ((-b - root)/2*a)
    print(f'For verdiene [A, B, C] = {arrayABC}, \nfår vi nullpunktene {formulaPluss:.2f} og {formulaMinus:.2f}.')
    
# REMINDER: print("Ved verdiene A,B,C = ",a,",",b,",",c,",","får du nullpunktene "+"%0.2f"%formulaMinus+" og "+"%0.2f"%formulaPluss)
