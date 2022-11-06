#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
x = 8
print(x)
#2) Imprimir el tipo de dato de la constante 8.5
y = 8.5
print(type(y))
#3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(x))
#4) Crear una variable que contenga tu nombre
nombre = 'Jesus'
#5) Crear una variable que contenga un número complejo
comp = 4 + 5j
#6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(comp))
#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi = 3.1416
#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
t1 = True
t2 = 'True'
#No se trata de lo mismo porque una es booleana y la otra es un string
#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print(type(t1))
print(type(t2))
#10) Asignar a una variable, la suma de un número entero y otro decimal
suma = 8 + 8.5
#11) Realizar una operación de suma de números complejos
comp1 = 1 + 4j
comp2 = 5 + 8j
print(comp1 + comp2)
#12) Realizar una operación de suma de un número real y otro complejo
print(suma + comp1)
#13) Realizar una operación de multiplicación
print(suma * 12)
#14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)
#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
coc = 27/4
print(coc)
#16) De la división anterior solamente mostrar la parte entera
oper1 = int(coc)
print(int(coc))
#17) De la división de 27 entre 4 mostrar solamente el resto
oper2 = 27%4
print(oper2)
#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(4 * oper1 + oper2)
#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
x = '25ac'
y = 'h0la'
print(x + y)
#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
x = 2
y = '2'
print(x == y)
#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(x == int(y))
#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
#por la coma, debe ser punto
#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
x = 3
x -= 2
print(x)
#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(1<<2)
print(2<<3)
#da este resultado porque 1 en binario es 1, el operador << mueve el 1 las unidades de lado derecho hacia la izquierda añadiendo
#ceros lo que lo convierte en 100 en binario, que en realidad es 4.
#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
#No esta permitido porque no son del mismo tipo, no arrojaria el mismo resultado porque si convertimos el string en entero nos daria 4
#convirtiendo el entero en string nos daria '22'
#26) Realizar una operación válida entre valores de tipo entero y string
x = 23
y = '72349134'
print(x + int(y))
print(str(x) + y)