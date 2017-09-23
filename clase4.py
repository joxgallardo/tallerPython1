#Condicionales.

#Diferenciales: while. Esta función permite ejecutar un comando mientras 
#la condición sea TRUE. 

#Hay que detener las funciones infinitas.

variable = 5
suma = 0
while suma < variable :
    suma += 1
    print (suma)

#Diferenciales: for. Esta función se repite siempre y cuando haya 
#una lista. Se ejecuta siempre y cuando haya un elemento en una lista.

arreglo = [1, 2, 3, 4, 5]
for i in arreglo:
    print(i)

 # A cada uno de los elementos de la lista le va a correr una función

arreglo = [1, 2, 3,"hola", 1.8]
for element in (range(0,60) arreglo):
    print(element)


# En este ejemplo la función for va a tomar el rango declarado (0,60). 

arreglo = [1, 2, 3, "hola", 1.8]
for element in range(0,len(arreglo)):
    print(element)

 # En este ejemplo la función for va a tomar la longitud total
 # del arreglo: (0,len(arreglo)). 

arreglo = ["elemento1", 1, 2, 3, "hola", 1.8]
for element in range(0,len(arreglo)):
    print(element)

for element in range(0, len(arreglo)):
 	print(element)

#Para romper ciclos usar break. Es una ruta de escape.

arreglo = ["elemento1", 1, 2, 3, "hola", 1.8]
for element in range(0,len(arreglo)):
    print(element)
    break

for element in arreglo:
    print (element)
    break

for element in range(0, len(arreglo)):
     print(element)
     break



# Esto es una matriz.

matriz = [["hola", 5][, 1, 6,][2.4, 3.6]]




# 0.0 Ejercicio: Imprimir todos los valores de una matriz


matriz = [["hola", 5, 8,],["mundo", 12, 9.8], ["better", 100, 1.15]]
for element in matriz:
	for inception in element:
		print(inception)

# 1.0 Ejercicio: Imprimir sólo los valores string.

#1.0
matriz = [["hola", 5, 8,],["mundo", 12, 9.8], ["better", 100, 1.15]]
for element in matriz:
	for a in element:
		print(a)
		break

#1.1
matriz = [["hola", 5, 8,],["mundo", 12, 9.8], ["better", 100, 1.15]]
for element in matriz:
	for a in element:
		print(a[0])

va
# Ejercicio 2.0. Iteración que incrementa una variable y otra que 
#decrementa una variable hasta que sean iguales. Contar ciclos


v1 = int(input("Inserta un número mayor: "))
v2 = int(input("Otro número, menor: "))
contador = 0

if v2 > v1:
    print ("Intenta de nuevo")
else:
    while v1 > v2:
        v1 -= 1
        v2 += 1
        contador += 1
        print ("Número de iteraciones: ",contador)



# Ejercicio 2.1. Iteración que intercambia los valores mayores y menores
# entre las variables.

maxi = int(input("Inserta un número mayor: "))
mini = int(input("Otro número, menor: "))
temp = 0

if maxi < mini:
    temp = maxi
    maxi = mini
    mini = temp
counter = 0
else:
while True:
    counter += 1
    if mini != maxi:
        mini += 1
        if mini != maxi:
            maxi = maxi -1
        else:
        	break

    else:
        break

print (counter)




# Para encontrar un elemento de un string
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

"a" in texto


# Ejercicio 3.0. Contar el número de vocales de un texto.

texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

vocal = 0

for i in texto:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vocal += 1

print ("El número de vocales en el texto es: ",vocal)

#3.1


text = input ("Ingresa un texto: ")


vocal = "aeiou"
counter = 0
for letter in text:
    if letter in vowels:
        counter += 1

print("hay ",counter," vocales")


# Ejercicio 4.0. Mostrar el número de cada vocal en un texto.

# solución 4.0

text = input ("Ingresa un texto: ")


a = "a"
e = "e"
i = "i"
o = "o"
u = "u"
countera = 0
countere = 0
counteri = 0
countero = 0
counteru = 0

for letter in text:
    if letter in a:
        countera += 1

for letter in text:
    if letter in e:
        countere += 1

for letter in text:
    if letter in i:
        counteri += 1

for letter in text:
    if letter in o:
        countero += 1

for letter in text:
    if letter in u:
        counteru += 1

print("hay ",countera," letras a")
print("hay ",countere," letras e")
print("hay ",counteri," letras i")
print("hay ",countero," letras o")
print("hay ",counteru," letras u")


# solución 4.1

a = 0
e = 0
i = 0
o = 0
u = 0

text = input("dame un texto")
for letter in text:
    if letter is "a":
        a += 1
    if letter is "e":
        e += 1
    if letter is "i":
        i += 1
    if letter is "o":
        o += 1 
    if letter is "u":
        u += 1
print("That text has", a," letter a")
print("That text has", e," letter e")
print("That text has", i," letter i")
print("That text has", o," letter o")
print("That text has", u," letter u")



# Declarar funciones

def suma (val1,val2):
    val3 = val1 + val2
    return(val3)
print (suma(5,8))

# Void function

def saludar():
    print("hola")

# Int function

def constante():
    return(7)


print(suma5,8))
saludar()
variable = constante()




