# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 07/11/2024
# Versió: 1
#
# Descripció: Calcula àrees de diversos rectangles
# Defineix area_rectangle(base, altura).
# Calcula i imprimeix:
# L'àrea d'un rectangle de 3x4.
# L'àrea d'un rectangle de 5x10.
# L'àrea d'un rectangle de 8x2.
# Especificacions: Programa que que mostri per pantalla les tres arees dels tres rectangles.

# Fer la funció
def area_rectangle(base, altura):
    return base * altura

# Nombrar la base i l'altura
print("Àrea de 3x4:", area_rectangle(3, 4))
print("Àrea de 5x10:", area_rectangle(5, 10))
print("Àrea de 8x2:", area_rectangle(8, 2))