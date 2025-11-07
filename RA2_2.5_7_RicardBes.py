# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 07/11/2024
# Versió: 1
#
# Descripció: Escriu una funció maxim(a, b, c) que retorni el nombre més gran entre els tres.
# Especificacions Programa que amb una funció que amb a b c retorni el nombre mes gran dels tres.

# Funció que retorna el màxim de tres nombres
def maxim(a, b, c):
    return max(a, b, c)

# El Resultat
a = int(input("Introdueix el primer nombre: "))
b = int(input("Introdueix el segon nombre: "))
c = int(input("Introdueix el tercer nombre: "))

print("El nombre més gran és:", maxim(a, b, c))
