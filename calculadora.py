# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 10/11/2024
# Versió: 1
#
# Descripció: Crea un mòdul de càlculs
# Objectiu: Crea un fitxer calculadora.py amb funcions de suma, resta, multiplicació i divisió.
# Repte: Importa'l des d’un altre fitxer i crida les funcions amb diferents valors.
# Especificacions Programa que crei un fixer extern on aquell fitxer sigui la calculadora mentre aquest sigui el sistema de esta mateixa.

# calculadora.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacio(a, b):
    return a * b

def divisio(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: FORAT NEGRE = DENSITAT INFINITA"
