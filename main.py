#La clase a la que pertenece un dato se obtiene
print(type(1))

print(type("Hola"))

print("\n")

# Para cadena de texto
a1 = str("Hola, tengo 18 años")
print(a1)
print(type(a1))

print("\n")

# Para numeros de entero
a2 = int(input("Introduce un numero: "))
print(a2)
print(type(a2))

print("\n")

#Para numeros con decimales
a3 = float(input("Intoduce un numero decimal: "))
print(a3)
print(type(a3))

print("\n")

#Para asignar a la variable un valor introducido por la consola se utiliza
a4 = input("Introduce el valor de la variable a4: ")
print(a4)
print("\n")

# Para mostrar un dato
print("Hola")
nombre = "Javier"
print("Hola", nombre)
print("Hola", nombre, sep = " ")
print("Hola", nombre, end = ".")

print("\n")

#Operadores aritmeticos
num1 = 5
num2 = 3
num3 = 8
# Suma
print(num1 + num2)
# Resta
print(num1 - num2)
# Producto
print(num1 * 4)
# Cociente
print(num3 / 2)
# Cociente division entera
print(num3 // 3)
# Resto division entera
print(num1 % 2)
# Potencia
print(num2 ** 3)

print("\n")

# Operadores logicos
#Igual 
5 == 5
# Menor
5 < 4
# Mayor
6 > 8
# Menor igual
7 <= 9
# Mayor igual
3 >= 6
# Distinto
3 != 4

print("\n")

# Condicionales
color1 = input("Introduce un color: ")
color2 = input("Introduce un color: ")
if color1 == color2:
  print("Son el mismo color")
else:
  print("Son distintos colores")




