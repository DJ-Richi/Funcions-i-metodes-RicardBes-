# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 07/11/2024
# Versió: 1
#
# Descripció: Escriu una funció estat_persona(edat) que:
# Retorni "Menor d'edat", "Adult" o "Jubilat" segons l'edat.
# Torni tant l'estat com una descripció (return estat, descripcio).
# Especificacions Programa que amb una funció que amb a b c retorni el nombre mes gran dels tres.

# Funció que determina l'estat d'una persona segons l'edat de esta
def estat_persona(edat):
    if edat < 18:
        estat = "Menor d'edat"
        descripcio = "És una persona jove que encara no ha arribat a ser major d'edat."
    elif edat < 65:
        estat = "Adult"
        descripcio = "És una persona en edat laboral o activa socialment."
    else:
        estat = "Jubilat"
        descripcio = "És una persona gran que probablement ja no treballa activament."
    return estat, descripcio

# Imprimeix l'edat i te la mostra per pantalla
edat = int(input("Introdueix l'edat: "))
estat, descripcio = estat_persona(edat)
print(f"Estat: {estat}")
print(f"Descripció: {descripcio}")
