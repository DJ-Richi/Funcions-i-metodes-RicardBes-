# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 07/11/2024
# Versió: 1
#
# Descripció: Escriu una funció filtra_parells(llista) que:
# Rebi una llista de nombres.
# Retorni una nova llista només amb els nombres parells.
# Especificacions Programa que amb una funció que amb a b c retorni el nombre mes gran dels tres.

# Funció que et filtra i retorna només els nombres parells d'una llista
def filtra_parells(llista):
    return [num for num in llista if num % 2 == 0]

# Imprimeix la llista pero en numeros parells
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parells = filtra_parells(nombres)
print("Nombres parells:", parells)
