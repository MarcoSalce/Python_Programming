#### EJERCICIO CLASES ####

# EJERCICIO 1 #
class metodos():
    def __init__(self):
        self.string = ""
    def get_String(self):
        self.string = input()
    def print_String(self):
        print(self.string.upper())

met1 = metodos()
met1.get_String()
met1.print_String()

## EJERCICIO 2 ##
class rectangulo():
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura   
    def area_rectangulo(self):
        area = self.base*self.altura
        return area
    
rect1 = rectangulo(50,700)
print(f" El area del rectangulo es equivalente a: {rect1.area_rectangulo()}")

### EJERCICIO 3 ###
from math import pi
class circulo():
    def __init__(self,radio):
        self.radio = radio
    def area(self):
        return self.radio**2*pi
    def perimetro(self):
        return 2*self.radio*pi
    
circ1 = circulo(8)
print(circ1.area())
print(circ1.perimetro())

#### EJERCICIO 4 ###
class Persona():
    def __init__(self,nombre="",edad=0,dni=""): #Datos vacios
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def get_dni(self):
        return self.dni
    def nombre(self,nombre):
        self.nombre = nombre
    
    def dni_valido(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(self.dni) != 9:
            self.dni = ""
            return "Invalido"
        else:
            letra = self.dni[8]
            nume = int(self.dni[:8])
            if letra.upper() == letras[nume % 23]:
                self.dni=""
                return "Valido"
                            
    def es_mayor_edad(self):
        if self.edad >= 18:
            return "mayor de edad"
        else:
            return "menor de edad"
   
    def mostrar_datos(self):
        return f"La persona cuyo nombre es {self.nombre} con la edad de {self.edad} años, {self.es_mayor_edad()} y con dni {self.dni} {self.dni_valido()}"
    
    
p1 = Persona("Marco", 34 ,"48078299l")
print(p1.mostrar_datos())

##### EJERCICIO 5 #####
class Triangulo():
    def __init__(self,lado_a=0,lado_b=0,lado_c=0):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
        
    def get_lado_a(self):
        return self.lado_a
    def get_lado_b(self):
        return self.lado_b
    def get_lado_c(self):
        return self.lado_c 
    def lado_max(self):
        lados = []
        for element in (self.lado_a,self.lado_b,self.lado_c):
            lados.append(element)
        return max(lados)
    
    def tipo_triangulo(self):
        if self.lado_a==self.lado_b and self.lado_a==self.lado_c:
            return "Equilátero"
        if self.lado_a!=self.lado_b and self.lado_a!=self.lado_c and self.lado_b!=self.lado_c:
            return "Escaleno"
        if (self.lado_a==self.lado_b and self.lado_a!=self.lado_c) or (self.lado_a==self.lado_c and self.lado_a!=self.lado_b) or (self.lado_b==self.lado_c and self.lado_b!=self.lado_a):
            return "Isósceles"
        
    def resultado_triangulo(self):
        return f"El triangulo cuyos lados son: {self.lado_a}, {self.lado_b}, {self.lado_c}.\nCuyo lado mayor es {self.lado_max()}.\nEs un triangulo de tipo {self.tipo_triangulo()}."   

t1 = Triangulo(50,300,100)
print(t1.resultado_triangulo())

###### EJERCICIO 6 ######
class Cuadrado():
    def __init__(self, lado_a=0):
        self.lado_a = lado_a
        
    def get_lado_a(self):
        return self.lado_a
    
    def area_cuadrado(self):
        area = self.lado_a * self.lado_a
        return area
    
    def perimetro_cuadrado(self):
        perimetro = self.lado_a * 4
        return perimetro
    
    def resultado_cuadrado(self):
        return f"El cuadrado cuyos lados son equivalentes a {self.lado_a}.\nTiene una arena equivalente a {self.area_cuadrado()}.\nCon un perimetro equivalente a {self.perimetro_cuadrado()}."
    
cuadrado1 = Cuadrado(30)
print(cuadrado1.resultado_cuadrado())

####### EJERCICIO 7 #######
class CuentaBancaria():
    def __init__(self, nombre,apellido,numcuenta,tipocuenta,saldo=0):
        self.nombre = nombre
        self.apellido = apellido
        self.numcuenta = numcuenta
        self.tipocuenta = tipocuenta
        self.saldo = saldo
        
    def titular(self):
        return f"El titular de la cuenta es: {self.nombre} {self.apellido}"
    
    def consulta(self):
        return f"El saldo de la cuenta es: {self.saldo}€"
    
    def ingresar(self,ingreso):
        self.saldo = self.saldo + ingreso
    
    def retirar_dinero(self,retiro):
        if self.saldo - retiro > 0:
            self.saldo = self.saldo - retiro
            return f"El nuevo saldo: {self.saldo}€"
    
    def __str__(self):
        return f"Los datos de la cuenta son:\n\
                Nombre: {self.nombre}\n\
                Apellido: {self.apellido}\n\
                Numero de cuenta: {self.numcuenta}\n\
                Tipo de cuenta: {self.tipocuenta}\n\
                Saldo en cuenta: {self.saldo}\n\
                "

persona = CuentaBancaria("Marco","Salcedo","0003213","Corriente",4000)

### Menu Ventana###
while True:
    cadena = input("1. Informacion cuenta\n2. Consulta saldo\n3. Ingreso a cuenta\n4. Retiro de dinero\n5. Salir")
    if cadena == '1':
        print(persona)
    elif cadena == '2':
        print(persona.consulta())
    elif cadena == '3':
        ingreso = input("Introduzca cantidad de ingreso: 	")
        persona.ingresar(int(ingreso))
    elif cadena == '4':
        retirar = input("Introduza cantidad de retiro: ")
        print(persona.retirar_dinero(int(retirar)))  
    elif cadena == '5':
        print("Hasta la proxima")
        break
    else:
        print("Introduzca una opcion valida")

######## EJERCICIO 8 ########
import math
class Calculos():
    def __init__(self,numero=0, numero1=0):
        self.numero = numero
        self.numero1 = numero1
    
    def get_numero(self):
        return self.numero
    
    def factorial(self):
        factor = math.factorial(self.numero)
        return factor
    
    def suma(self):
        numeros = []
        for element in range(1,self.numero+1):
            numeros.append(element)
        
        total_suma = sum(numeros)
        return numeros, total_suma #CORREGIR MEJOR
    
    def testPrimo(self):
        for element in range(2, self.numero):
            if self.numero % element == 0:
                print("No es primo", element, "es divisor")
                return False
        print("Es primo")
        return True # CORREGIR MEJOR
    
    def testPrimos(self):
        a = min(self.numero,self.numero1)
        b = max(self.numero,self.numero1)
        div = 2
        
        while (div <=a):
            if ((a % div == 0) and (b % div == 0)):
                return False
            div += 1
        return True
    
    def tablaMult(self): 
        nume = self.numero
        for element in range(nume+1):
            tabla = nume * element
            print(f"{nume} x {element} = {tabla}")
        return
    
    def allTablesMult(self): 
        nume = self.numero
        for element in range(1,10):
            entero = nume * element
            print(f"{nume} x {element} = {entero}") #CORREGIR
        return 

    def listDiv(self):
        nume = self.numero
        lista = []
        for element in range(1,nume+1):
            if nume % element == 0:
                lista.append(element)
        return lista
                   
calcu = Calculos(5)
print(calcu.suma())
print(calcu.factorial())
print(calcu.testPrimo())

calcu1 = Calculos(4,24)
print("")
print(calcu.testPrimos())

calcu2 = Calculos(8)
print("")
print(calcu2.tablaMult())
print(calcu2.allTablesMult())
print(calcu2.listDiv())

######### EJERCICIO 9 #########
class Triangulo():
    def __init__(self,angle1=0,angle2=0,angle3=0):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        
    def numero_de_lados(self):
        lados = (self.angle1,self.angle2,self.angle3)
        if len(lados) == 3:
            return True, f"Es un triangulo" ##PREGUNTAR
        else:
            return False, f"No es un triangulo"
    
    def comprobar_angulos(self):
        a = self.angle1
        b = self.angle2
        c = self.angle3
        
        if a+b+c == 180:
            return True
        else:
            return False
        
mi_triangulo = Triangulo(90,30,60)
print(mi_triangulo.numero_de_lados())
print(mi_triangulo.comprobar_angulos())

########## EJERCICIO 10 ##########
class Songs():
    def __init__(self,lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for linea in self.lyrics:
            cancion = print(linea)
        return cancion
    
happy_bday = Songs(["May god bless you, ",
                    "Have a sunshine on you,",
                    "Happy Birthday to you !"])

print(happy_bday.sing_me_a_song())
