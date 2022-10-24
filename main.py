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
print("Hola", nombre, sep=" ")
print("Hola", nombre, end=".")

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
print(num2**3)

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

print("\n")

#Tupla
ciudades = ("Madrid", "Stuttgart", "Munich", "Paris", "Florencia", "Viena")
print(ciudades)
#Penultimo elemento
print(f"El penultimo elemento es: ", ciudades[4])
#Longitud de l tupla
print(f"La tupla mide: ", len(ciudades))
#Busqueda en la tupla
print(f"Queremos buscar: ", ciudades[1])
#Añadir elemento
#A diferencia de las listas, en las tuplas no podemos añadir elementos, ya que no existe esa posibilidad.
#Elimanar elemento
# A diferencia de las listas, en las tuplas no podemos eliminar elentos, ya que no existe esa posibilidad.

print("\n")

# LISTAS
# Asi se declara una lista
paises = ["España", "Alemania", "Italia", "Suiza", "Francia", "Inglaterra"]
print(paises)

#Crea una lista a partir de una frase, en la que cada letra y espacio es un elemento de la lista
lista = list("Python is awesome")

# Mostrar la lista
print("lista = ", lista)
# Imprimir un miembro de la lista
print("lista[4] = ", lista[4])
print("lista[-3] = ", lista[-3])

# Extracción de sub-lista
#Del 0 incluido al 5 incluido, sin incluir el 6
print("lista[:6] = ", lista[:6])
#Del 7 incluido hasta el 9 incluido, sin incluir el 10
print("lista[7:10] = ", lista[7:10])
#Del 10 incluido hasta el final
print("lista[10:] = ", lista[10:])
# A partir del 2 va sumando de 5 en 5 hasta el final (2, 7, 12...)
print("lista[2::5] = ", lista[2::5])
#A partir del -3 va restando de 6 en 6 hasta el final (-3, -9, -15)
print("lista[-3::-6] = ", lista[-3::-6])

# Escritura de un miembro de la lista (set)
#Inserta en el puesto 11 una letra b
print("""lista[11] = "b" """)
lista[11] = "b"
print("lista = ", lista)
#Inserta en puesto 13 y 14 las letras fg, sin incluir el puesto 15
print("""lista[13:15] = "fg" """)
lista[13:15] = "fg"
print("lista = ", lista)

# Eliminar un miembro de la lista (del)
# Elimina el elemento del puesto 15
print("""del lista[15]""")
del lista[15]
print("lista = ", lista)
# Elimina la y de la lista
print("""lista.remove("y")""")
lista.remove("y")
print("lista = ", lista)
# Mientras que haya espacios en la lista, borrar los espacios
print("""while " " in lista: lista.remove(" ")""")
while " " in lista:
    lista.remove(" ")
print("lista = ", lista)
# Elimina los elementos de la lista del 0 incluido hasta 6 incluido, sin incluir el 7
print("""del lista[:7]""")
del lista[:7]
print("lista = ", lista)

# Eliminar el último elemento (y devolverlo)
print("""lista.pop() -> Devuelve :""", lista.pop())
print("lista = ", lista)

# Agregar un elemento al final de la lista
print("""lista.append("h")""")
lista.append("h")
print("lista = ", lista)

# Agregar un elemento en cualquier lugar de la lista
print("""lista.insert(2, "d")""")
lista.insert(2, "d")
print("lista = ", lista)

print("""lista.insert(2, "c")""")
lista.insert(2, "c")
print("lista = ", lista)

# Concatenación de una lista
# Añade al final de la lista tantos elementos como quieras
print("""lista.extend(["i", "j"])""")
lista.extend(["i", "j"])
print("lista = ", lista)

print("\n")

#SET
comida = {"Tortilla", "Gazpacho", "Lentejas", "Fabada", "Cocido"}
print(comida)
#Longitud set
print(len(comida))
#Segundo elemento: No se pueden buscar elementos en los set
#Añadir elemento:
comida.add("Cocretas")
print(comida)
#Eliminar elemeneto:
comida.remove("Cocido")
print(comida)

print("\n")

# DICCIONARIOS

# En los diccionarios, cada elemento esta compuesto por keys: values, en la que cada carta tiene un valor

baseDeDatos = {"Nombre": "Javier", "Apellido": "Caletrio", "Pais": "España"}
print(baseDeDatos)
#Primer valor - clave
print(baseDeDatos.get("Nombre"))
print(baseDeDatos["Nombre"])
#Longitud diccionario
print(f"El diccionario mide: ", len(baseDeDatos.keys()))
#Añadir elemento
baseDeDatos["Gate"] = "D16"
print(baseDeDatos)
#Eliminar elemento
del (baseDeDatos["Apellido"])
print(baseDeDatos)

# Otro ejemplo
cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}
# Imprime el diccionario, tanto los elementos de la izquierda como los de la derecha
print(cartas)
# El .format(" ".join(cartas.keys())) es para imprimir todos los elementos de la izquierda del diccionario que son las cartas en dibujo. El " " es para que deje un espacio entre los dibujos y el join es para que se imprima solo las  cartas, ya que sino se imprime como un diccionario
print("Cartas: {}".format(" ".join(cartas.keys())))
# El .format(list(cartas.values())) imprime todos los elementos de la derecha del diccionario que son los valores de las cartas. Para  hacerlo mas bonito, lo imprime en una lista
print("Puntos: {}".format(list(cartas.values())))

# Para recorrer un diccionario se utiliza .items() y luego en el .format(keys, values)
print("1\ Iteración estándar sobre un diccionario")
for carta, valor in cartas.items():
    print("la carta {} vale {}".format(carta, valor))
# Para recorrer un diccionario de forma ordenada se utiliza sorted(para ordenar) y cartas.keys para recorrer el diccionario por las keys
print("2\ Iteración ordenada sobre un diccionario")
for carta in sorted(cartas.keys()):
    print("la carta {} vale {}".format(carta, cartas[carta]))

# FUNCIONES
# Las funciones son bloques de codigo, que una vez que los creas los puedes volver a utilizar tantas veces como quieras a lo largo de tu trabajo


def agenda(nombre, apellido):
    #Escribes todo lo que quieras
    lista = [nombre, apellido]
    print(lista)

    return lista


print(agenda(nombre, apellido))
