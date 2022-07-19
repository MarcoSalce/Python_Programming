### EJERCICIOS FUNCIONES ###

# EJERCICIO 1 #
def ordena(cadena):
    cadena = cadena.split(',')
    lista= []
    for element in cadena:
        lista.append(int(element))
    return sorted(lista)

cadena = input("Entra valores: ")
print(ordena(cadena))

## EJERCICIO 2 ##
def suma(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total
        
c = input("Escribe numeros separados por coma: ")
c = c.split(',')
for pos in range(len(c)):
    c[pos] = int(c[pos])
print(suma(c))

### EJERCICIO 3 ###
def sumaquadrats(lista):
    total = 0
    for elemento in lista:
        total += elemento ** 2
    return total
        
c = input("Escribe numeros separados por coma: ")
c = c.split(',')
for pos in range(len(c)):
    c[pos] = int(c[pos])
print(sumaquadrats(c))

#### EJERCICIO 4 ####
def sumacubs(lista):
    total = 0
    for elemento in lista:
        total += elemento ** 3
    return total
        
c = input("Escribe numeros separados por coma: ")
c = c.split(',')
for pos in range(len(c)):
    c[pos] = int(c[pos])
print(sumacubs(c))

##### EJERICICIO 5 #####
def minim(lista):
    for elemento in lista:
        valor = min(lista)
    return valor

c = input("Escribe numeros separados por coma: ")
c = c.split(',')
for pos in range(len(c)):
    c[pos] = int(c[pos])
print(minim(c))

###### EJERCICIO 6 ######
def maxim(lista):
    for elemento in lista:
        valor = max(lista)
    return valor

c = input("Escribe numeros separados por coma: ")
c = c.split(',')
for pos in range(len(c)):
    c[pos] = int(c[pos])
print(maxim(c))

####### EJERICICIO 7 #######
def inverteix(lista):
    return lista[::-1]

c = input("Escribe numeros separados por coma: ")
c = c.split(',')
for pos in range(len(c)):
    c[pos] = int(c[pos])
print(inverteix(c))

######## EJERICICIO 8 ######## 
def parell(cadena):
    cadena = cadena.split(',')
    lista = []
    for element in cadena:
        lista.append(int(element))
    pos_par = []
    for pos in range(len(lista)):
        if pos % 2 == 0:
            pos_par.append(lista[pos])
    return pos_par

cadena = input("")
print(parell(cadena))

######### EJERICICIO 9 #########
def senar(cadena):
    cadena = cadena.split(',')
    lista = []
    for element in cadena:
        lista.append(int(element))
    pos_inpar = []
    for pos in range(len(lista)):
        if pos % 2 == 1:
            pos_inpar.append(lista[pos])
    return pos_inpar

cadena = input("")
print(senar(cadena))

########## EJERICICIO 10 ##########
def digits(cadena):
    cadena = cadena.split(',')
    lista = []
    for element in cadena:
        lista.append(len(element))
    return lista

cadena = input("")
print(digits(cadena))

########### EJERICICIO 11 ###########
def longitud(cadena):
    cadena = cadena.split(',')
    lista = []
    for element in cadena:
        lista.append(len(element))
    return lista

cadena = input("")
print(longitud(cadena))

############ EJERICICIO 12 ############
def minuscules(cadena):
    cadena = cadena.split(',')
    lista = []
    for element in cadena:
        lista.append(element.lower())
    return lista

cadena = input("")
print(minuscules(cadena))

############# EJERICICIO 13 #############
def majuscules(cadena):
    cadena = cadena.split(',')
    lista = []
    for element in cadena:
        lista.append(element.upper())
    return lista

cadena = input("")
print(majuscules(cadena))

############## EJERICICIO 14 ##############
def majuscules(cadena):
    cadena = cadena.split(',')
    lista = []
    for element in cadena:
        lista.append(element)
    return "".join(lista)

cadena = input("")
print(majuscules(cadena))

############### EJERICICIO 15 ###############
def ordenarstring(cadena):
    cadena = cadena.split(',')
    lista = []
    for element in cadena:
        lista.append(element)
    return sorted(lista)

cadena = input("")
print(ordenarstring(cadena))

################ EJERICICIO 16 ################
def parelles(cadena):
    cadena = cadena.split(',')
    pares = []
    for pos in range(len(cadena)):
        if pos % 2 != 1:
            pares.append(cadena[pos])
    return pares
    
cadena = input("Escribe algo: ")
print(parelles(cadena)) 

################# EJERICICIO 17 #################
def senars(cadena):
    cadena = cadena.split(',')
    inpar = []
    for pos in range(len(cadena)):
        if pos % 2 != 0:
            inpar.append(cadena[pos])
    return inpar
    
cadena = input("Escribe algo: ")
print(senars(cadena))

################## EJERICICIO 18 ##################
def nolast(cadena):
    cadena = cadena.split(',')
    lista = []
    for element in cadena:
        lista.append(element[:-1])
    return lista

cadena = input("")
print(nolast(cadena)

################### EJERICICIO 19 ###################
def nofirst(cadena):
    cadena = cadena.split(',')
    lista = []
    for element in cadena:
        lista.append(element[1:])
    return lista

cadena = input("")
print(nofirst(cadena))

#################### EJERICICIO 20 ####################
def inversio(cadena):
    cadena = cadena.split(',')
    lista = []
    for element in cadena:
        lista.append(element[::-1])
    return lista

cadena = input("")
print(inversio(cadena))
