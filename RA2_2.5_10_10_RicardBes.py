# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 10/11/2024
# Versió: 1
#
# Descripció: Defineix filtra_parells(llista).
# Aplica la funció a:
# [1, 2, 3, 4, 5, 6]
# [10, 15, 20, 25, 30]
# Imprimeix la nova llista de parells.
# Especificacions Programa que filtri 2 llistes de parelles i que en elles es mostrin els numeros parells.

def filtra_parells(llista):
    return [num for num in llista if num % 2 == 0]

# Llistes d'exemple
llista1 = [1, 2, 3, 4, 5, 6]
llista2 = [10, 15, 20, 25, 30]

# Aplicar la funció i imprimir els resultats
print("Parells de la primera llista:", filtra_parells(llista1))
print("Parells de la segona llista:", filtra_parells(llista2))
