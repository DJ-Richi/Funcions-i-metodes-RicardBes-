# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 07/11/2024
# Versió: 1
#
# Descripció: Escriu una funció saluda_nom(nom="amic") que imprimeixi "Hola, <nom>". # Si no passes cap nom, ha de imprimir "Hola, amic".
# Especificacions Programa que amb una funció imprimeixi "Hola <nom>". Si no hi ha cam nom, imprimira "Hola, amic".

# Funcionament de la funció
def saluda_nom(nom="amic"):
    print(f"Hola, {nom}")

# Mostrau per pantalla
saluda_nom("Ricard")    # Imprimira: Hola, Ricard
saluda_nom()            # Imprimira: Hola, amic