# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 10/11/2024
# Versió: 1
#
# Descripció: # Conversió de temperatures
# Crea un mòdul conversions.py amb funcions:
# celsius_a_fahrenheit(c),
# fahrenheit_a_celsius(f)
# Fes servir el mòdul des d’un script principal per convertir diferents valors.
# Especificacions Programa que crei un fixer extern on aquell fitxer sigui la calculadora de temperatura i a l'altre que les diferens opcions es mostrin en pantalla.

# conversions.py

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9
