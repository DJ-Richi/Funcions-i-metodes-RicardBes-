# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 10/11/2024
# Versió: 1
#
# Descripció: Determina l'estat de diferents edats
# Defineix estat_persona(edat).
# Per les edats [12, 25, 70], crida la funció i imprimeix quin estat retorna.
# Especificacions Programa que determini en quant a diferents edats que digi si es major o menor d'edat.

def estat_persona(edat):
    if edat < 18:
        return "Menor d'edat"
    elif edat < 65:
        return "Adult"
    else:
        return "Jubilat"

# Llista d'edats
edats = [12, 25, 70]

# Crida la funció per cada edat i imprimeix el resultat
for edat in edats:
    estat = estat_persona(edat)
    print(f"L'edat {edat} correspon a: {estat}")