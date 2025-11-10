# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 10/11/2024
# Versió: 1
#
# Descripció: Mòdul de geometria
# Escriu un mòdul geometria.py amb funcions:
# area_quadrat(costat)
# area_cercle(radi)
# area_rectangle(base, altura)
# Fes servir-lo per calcular les àrees amb dades introduïdes per l’usuari.
# Especificacions Programa que crei un fixer extern on aquell fitxer sigui la calculadora de geometria i a l'altre fiter el resultat segons l'usuari.
# geometria.py

def area_quadrat(costat):
    return costat ** 2

def area_cercle(radi):
    return math.pi * radi ** 2

def area_rectangle(base, altura):
    return base * altura
