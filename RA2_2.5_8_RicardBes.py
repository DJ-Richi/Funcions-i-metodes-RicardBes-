# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 07/11/2024
# Versió: 1
#
# Descripció: Escriu una funció factorial(n) que calculi el factorial d'un nombre n de forma recursiva. (Pista: factorial de n és n * factorial(n-1), amb factorial(0) = 1.)
# Especificacions Programa que amb una funció que amb a b c retorni el nombre mes gran dels tres.

# Funció que retorna el màxim de tres nombres amb el factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Exemple d'ús
num = int(input("Introdueix un nombre enter: "))
print(f"El factorial de {num} és {factorial(num)}")
