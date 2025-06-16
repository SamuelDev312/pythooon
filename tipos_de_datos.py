# Entero (int)
edad = 30
print("Edad (int):", edad)

# Número decimal (float)
altura = 1.75
print("Altura (float):", altura)

# Cadena de texto (str)
nombre = "Ana"
print("Nombre (str):", nombre)

# Booleano (bool)
es_mayor = True
print("¿Es mayor de edad? (bool):", es_mayor)

# Lista (list)
frutas = ["manzana", "banana", "naranja"]
print("Frutas (list):", frutas)
print("Primera fruta:", frutas[0])

# Tupla (tuple)
punto = (10, 20)
print("Coordenadas (tuple):", punto)

# Conjunto (set) – no permite duplicados
colores = {"rojo", "verde", "azul"}
print("Colores (set):", colores)

# Diccionario (dict) – clave: valor
persona = {"nombre": "Luis", "edad": 28, "ciudad": "Bogotá"}
print("Persona (dict):", persona)
print("Nombre de la persona:", persona["nombre"])

# Tipo None (valor nulo o sin definir)
nada = None
print("Valor de 'nada' (NoneType):", nada)

# Ver tipo de datos
print("\nTipos de datos:")
print(type(edad))
print(type(altura))
print(type(nombre))
print(type(es_mayor))
print(type(frutas))
print(type(punto))
print(type(colores))
print(type(persona))
print(type(nada))