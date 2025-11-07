# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 07/11/2024
# Versió: 1
#
# Descripció: Escriu una funció multiplica_tot(*nombres) que rebi qualsevol quantitat de nombres i retorni la seva multiplicació.
# Especificacions Programa que amb una funció multipliqui qualsevol quantitat de nombres i que retorni la multiplicacio en concret.

# La funcio de la multiplicació multiplica els nombres introduits
def multiplica_tot(*nombres):
    resultat = 1
    for num in nombres:
        resultat *= num
    return resultat

# El resultat corresponent
print(multiplica_tot(2, 3, 4, 8, 9, 19))   # Imprimeix: 24
print(multiplica_tot(5, 9))                # Imprimeix: 5
print(multiplica_tot())                    # Imprimeix: 1
