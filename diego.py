# Programa básico en Python

# Pedimos el nombre y la edad al usuario
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))

# Mostramos un mensaje personalizado
print(f"Hola, {nombre}! Tienes {edad} años.")

# Calculamos el año en que cumplirá 100 años
anio_actual = 2025
faltan = 100 - edad
anio_100 = anio_actual + faltan

print(f"Cumplirás 100 años en el año {anio_100}.")
