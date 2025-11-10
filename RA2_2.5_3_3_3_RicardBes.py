# main.py

import geometria

# Entrada de l'usuari
costat = float(input("Introdueix el costat del quadrat: "))
radi = float(input("Introdueix el radi del cercle: "))
base = float(input("Introdueix la base del rectangle: "))
altura = float(input("Introdueix l'altura del rectangle: "))

# Càlculs
print(f"\nÀrea del quadrat: {geometria.area_quadrat(costat):.2f}")
print(f"Àrea del cercle: {geometria.area_cercle(radi):.2f}")
print(f"Àrea del rectangle: {geometria.area_rectangle(base, altura):.2f}")
