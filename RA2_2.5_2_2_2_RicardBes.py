# importem el fiter anterior a aquest

import conversions

# Valors a convertir
celsius = [0, 20, 100]
fahrenheit = [32, 68, 212]

# Conversió de Celsius a Fahrenheit
print("Conversió de Celsius a Fahrenheit:")
for c in celsius:
    print(f"{c}°C = {conversions.celsius_a_fahrenheit(c):.2f}°F")

# Conversió de Fahrenheit a Celsius
print("\nConversió de Fahrenheit a Celsius:")
for f in fahrenheit:
    print(f"{f}°F = {conversions.fahrenheit_a_celsius(f):.2f}°C")
