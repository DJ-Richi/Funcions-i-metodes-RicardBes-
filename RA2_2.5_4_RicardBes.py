# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 07/11/2024
# Versió: 1
#
# Descripció: Escriu una funció es_parell(numero) que retorni True si numero és parell i False si no.
# Especificacions Programa que amb una funció que retorni True si numero és parell i False si no es.

# Funció que retorna True si el número és parell, False si no
def es_parell(numero):
    return numero % 2 == 0

# Exemple d'ús
num = int(input("Introdueix un número: "))
if es_parell(num):
    print("El número és parell.")
else:
    print("El número és inparell.")
