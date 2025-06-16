# Declaración de variables
nombre = "Samuel"
edad = 25
a = 10
b = 5

# Operaciones básicas
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

# Mostrar resultados
print("Hola,", nombre)
print("Edad:", edad)
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

# Condicional
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Ciclo for
print("\nContando del 1 al 5 con for:")
for i in range(1, 6):
    print(i)

# Ciclo while
print("\nContando del 5 al 1 con while:")
contador = 5
while contador > 0:
    print(contador)
    contador -= 1
