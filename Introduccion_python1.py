#funcion print: permite imprimir un mensaje en la consola, ya sea introduciendo algun tipo de dato, una o más variables o ambas
print("Hola Mundo")
#Al igual que en otros legunajes de programación, una variable es un valor que puede cambiar durante el codigo y es capaz de almacenar un solo tipo de dato a la vez. Se le asigna un dato correspondiente haciendo uso del operador de asignación "="
variable = "Soy una variable"
print(variable)
print("Hola Mundo, ",variable)
#Existen diversos tipos de datos en Python, aunque los 4 datos principales en este son el String, Entero, Flotante y Booleano
variable = "Soy un String" #Cadena de caracteres que puede ser alfanumerica y va encerrada entre comillas
variable = 4 #Numero entero, como cualquier numero real, positivo, neutro o negativo que no sea decimal
variable = 4.1 #Numero flotante, todo numero real igual que el entero pero que posea la caracteristica decimal, aunque este sea 0
variable = True #Bool, Condicion verdadera o falsa en cualquier tipo de dato

#Podemos averiguar el tipo de dato en la consola usando la funcion type()
print(type(variable))

#Se puede designar el tipo de dato en una variable, aunque Python se caracteriza por tener un tipado dinamico, es decir, que el tipo de dato puede variar dentro de la misma variable
variable = str("Hola Mundo")
variable = int(4)
variable = float(4.1)
variable = bool(False)
#Operadores aritmenticos: los mismos operadores matematicos basicos pero aplicados a programación, entre estos: suma, resta, multiplicacion, division, cociente, exponente y mas conocido en este aspecto, modulo
variable = 3 + 1
variable = 5 - 1
variable = 2 * 2
variable = 8 / 2
variable = 9 // 2
variable = 2**2
variable = 76 % 8
#Asi como en las matematicas, estos tiene una jerarquia la cual de mayor a menor seria: parentesis(), exponente **, multiplicación *, division / (junto a modulo % y cociente //), suma +, resta -
variable = ((3+1)*3/2)-(2**2)%2
print(variable)

#Entrada de datos: Función que permite al usuario ingresar un tipo de dato simple (Numero, Bool o String)
variable=input("Hola, escriba un tipo de dato: ")
print(variable)

#Aqui se encuentran los ejercicios que vimos en el video (nota: si quieren probarlos, creen un nuevo archivo .py y pruebenlos ahi para evitar problemas)

#Calculo de descuento

producto=float(input("Introduzca el precio de su producto: "))
descuento=0.40
precio_final=producto-producto*descuento
print("El precio de su producto con el descuento es de", precio_final)

#Promedio de notas

nota1=float(input("Introduzca la primer nota: "))
nota2=float(input("Introduzca la segunda nota: "))
nota3=float(input("Introduzca la tercer nota: "))
nota4=float(input("Introduzca la cuarta nota: "))

promedio=(nota1+nota2+nota4)/4
print("El promedio de las notas es: ", promedio)


