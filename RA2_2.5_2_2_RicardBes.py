# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 07/11/2024
# Versió: 1
#
# Descripció: Suma de diferents parelles de nombres
# Defineix la funció suma(a, b).
# Fes tres crides amb diferents valors: suma(2, 3), suma(10, 20), suma(-5, 7).
# Imprimeix el resultat de cada crida.
# Especificacions: Programa que que mostri per pantalla els tres resultats

# Funció que retorna la suma de dos nombres
def suma(a, b):
    return a + b

# Crida a la funció amb diferents parelles
resultat1 = suma(2, 3)
resultat2 = suma(10, 20)
resultat3 = suma(-5, 7)

# Imprimeix els resultats
print("suma(2, 3) =", resultat1)
print("suma(10, 20) =", resultat2)
print("suma(-5, 7) =", resultat3)