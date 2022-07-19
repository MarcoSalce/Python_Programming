## EJERCICIOS CADENAS ##

# EJERCICIO 1 #
def invertir(cadena):
    reverse = cadena[::-1]
    return reverse

cadena = input("Escribe algo: ")
print(invertir(cadena))

## EJERCICIO 2 ##
def contar_a(cadena):
    letra = cadena.count('a')
    return letra
   
cadena = input("Ingresa palabras con a: ")
print(f"La cantidad que aparece 'a' es: {contar_a(cadena)}")

### EJERCICIO 3 ###
def letra_dni(cadena):
    cadena = int(cadena)
    tabla_dni = 'TRWAGMYFPDXBNJZSQVHLCKE'
    dni_asig = tabla_dni[cadena%23]
    return dni_asig

cadena = input("Entra los numeros del DNI: ")
print("La letra de tu dni es:",letra_dni(cadena))

#### EJERCICIO 4 ####
def contar_palabras(cadena):
    palabras = len(cadena.split())
    return palabras

cadena = input("Entra los numeros del DNI: ")
print(f"La cadena tiene: {contar_palabras(cadena)} palabras")

##### EJERCICIO 5 #####
cadena_0 = input("Entra la primera palabra: ")
cadena_1 = input("Entra la segunda palabra: ")

if len(cadena_0) > len(cadena_1):
    print(f"La primera palabra es mayor y tiene: {len(cadena_0)} letras")
if len(cadena_0) < len(cadena_1):
    print(f"La segunda palabra es mayor y tiene: {len(cadena_1)} letras")
if len(cadena_0) == len(cadena_1):
    print("Ambas palabras son iguales")

###### EJERCICIO 6 ######
cadena = input("")
cadena = cadena + "\n"
print(len(cadena)*cadena)

# Segunda versión
cadena = input("")
for element in cadena:
    print(cadena)

####### EJERCICIO 7 #######
def contar_vocales(cadena):
    vocal = 0
    for element in cadena:
        if element.lower() in "aeiou":
            vocal += 1
    return vocal

cadena = input("")
print(contar_vocales(cadena))

######## EJERCICIO 8 ########
cadena = input("")
palabra = cadena.split()
print(" BONICA PARAULA ".join(palabra), end = " BONICA PARAULA ")

########## EJERCICIO 9 #########
cadena = input("Escribe aquí: ")
for element in cadena.split():
    longi = len(element)
    print(element+str(longi))

########## EJERCICIO 10 ##########
cadena = input("Escribe aquí: ")
for element in cadena.split():
    longi = len(element)
    print(element+str(longi), end = " ")

########## EJERCICIO 11 ###########
cadena = input("Ingrese numero: ")
nume = None
for element in (int, float):
    try:
        nume = element(cadena)
        break
    except ValueError:
        pass

if nume is None:
    print(f"{cadena} no és un número")
if type(nume) is float:
    print(f"{nume} es un número real")
if type(nume) is int:
    print(f"{nume} es un número entero")

########### EJERCICIO 12 ############
cadena1 = input("")
cadena2 = input("")

if cadena1 in cadena2:
    print(f"La cadena '{cadena1}' SI esta dentro de '{cadena2}'")
if not cadena1 in cadena2:
    print(f"La cadena '{cadena1}' NO esta dentro de '{cadena2}'")

############ EJERCICIO 13 #############
cadena1 = input("")
cadena2 = input("")
cadena3 = input("")

if cadena1 in cadena3 and cadena2 not in cadena3:
    new_cadena0 = cadena3.replace(cadena1,cadena2)
    print(new_cadena0)
if cadena2 in cadena3 and cadena1 not in cadena3:
    new_cadena1 = cadena3.replace(cadena2,cadena1)
    print(new_cadena1)

############## EJERCICIO 14 ##############
def palindromo(cadena):
    cadena = cadena.replace(' ','')
    long_cade = len(cadena)
    if long_cade % 2 == 0:
        part1_cade = cadena[:long_cade//2]
        part2_cade = cadena[long_cade//2:]
    else:
        part1_cade = cadena[:long_cade//2]
        part2_cade = cadena[long_cade//2+1:]
    
    palin_cadena = part1_cade == part2_cade[::-1]
    return palin_cadena

cadena = input("")
if palindromo(cadena) is True:
    print("La cadena es un palindromo")    
if palindromo(cadena) is False:
    print("La cadena no es un palindromo")
