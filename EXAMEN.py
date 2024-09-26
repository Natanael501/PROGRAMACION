#   while condicion:
#       codigo
#
#   Su funcion se basa en repetir una accion varias veces a partir de
#   de evaluar una condicion logica, siempre que sea True.

#El siguiente ejemplo esta mal, porque el codigo entrara en bucle:
val = 3
while val < 5:
    print(val)

#1: Condicion inicial: condicion que es evaluada
#2: Condicion de paro: para que el codigo ya no se repita otra vez
#3: Condicion de incremento: para que los valores cambien y no se convierte en una condicion en bucle
# la manera correcta seria la siguiente
val = 3
while val < 5:
    print(val)
    val += 1

# Else en bucle con while
# se encadena al while para ejecutar un bloque de codigo una vez la
# condicion ya no devuelve True (normalmente al final)
#el siguiente es la manera incorrecta, ya que entra en bucle al no incrementar
lista = ['chocolate', 'tristeza', 'cualquiera', 'naranjas', 'azul', 'parque']
indice = -3
while lista[indice] == 'cualquiera':
    print(indice, lista[indice])

else:
    print('se cumplio la condicion, ya me quiero mimir')

# la siguiente es la manera correcta, ya que tinene incremento en indice += 1
lista = ['chocolate', 'tristeza', 'cualquiera', 'naranjas', 'azul', 'parque']
indice = -3
while lista[indice] != 'cualquiera':
    print(indice, lista[indice])
    indice += 1
else:
    print('se cumplio la condicion, ya me quiero mimir')

# Ejemplo donde no se cumple con la condicion de paro, ya que siempre es true
idx = 0
while True:
    idx *= 2
    print(idx)
else:
    print('salio')


# Ejemplo con brake (el contrario de continue, el cual sigue con la siguiente parte de while)

c = 0
while c <= 5:
    c += 1
    if c == 4:
        print("Rompemos el bucle cuando c vale ", c)
        break
    print("c vale", c)
else:
    print("Se ha completado toda la iteracion y c vale", c)

# Donde colocamos las diferentes condiciones (como la de incremento)
# es muy importante para los resultados al ejecutar el codigo.


# FORMAS DE USAR LOS print(): convinar cadenas con la funcion .format
#1 format despues
print('5 * {} = {}'.format({1er valor}, {2do valor}))
#2: format (f) antes
print(f'5 * {val} = {5*val}')


# FUNCIONES
# Son fragmentos de codigo que se pueden ejecutar multiples veces. Pueden
# recibir y devolver informacion para comunicarse con el proceso principal.
# definicion y llamada
# todo lo que se hace dentro de una funcion se queda dentro de la funcion.
def nombre_de_la_funcion():
    for i in range(11):
        print("5 x ", i, " = ", 5*i)

nombre_de_la_funcion()

def tabla_del_5():
    for i in range(1, 11):
        print("5 x ", i, " = ", 5*i)
tabla_del_5()

# VARIABLES GLOBALES(fuera de la funcion) VS VARIABLES LOCALES(dentro de la funcion)
# return saca de la funcion el valor local ("lo hace global")...ademas, lo mejor es cambiar el 
#nombre de la variable cuando ya es global. Esto no es recomendable..pero existe la herramienta
# return tambien nos permite sacar mas valores relacionados con el original(n) como n*5. Esto nos lo devuelve
# en forma de tupla. Pero esto lo podemos cambiar con la sintaxis.

x = 8
def chuchito():
    x= 1
    print(x)

chuchito()
print(x)

# La variable se ejecuta hasta que es nombrada dentro del codigo (argumento: 'parametros" pero fuera
# de la definicion de funcion). Por buen habito no se recomienda
# empezar el nombre de la funcion con mayuscula.

# En la definicion de un afuncion, los valores que se reciben se denominan parametros,
# y en la llamada se denominan argumentos

def test(parametro1, parametro2):
    print(parametro1, parametro2)

argumento1 = argumento2 = 5, ['casa']
test(argumento1,argumento2)

# A la hora de asignar parametros a la funcion, Python no tiene restricciones con respecto al tipo
# de dato de los parametros. Sin embargo, nosotros como buenos programadores podemos definir el tipo
# dato de los parametros , esto definiendolo con : y despues el tipo de dato.
def test(parametro1: int, parametro2: int):
    print(parametro1, parametro2)
#
argumento1 , argumento2 = 5, 9
test(argumento1,argumento2)

# ARGUMENTOS POR POSICION
# podemos ordenar el valor de los parametros cuando colocamos los argumentos
def funcion01(a, b):
    print(a-b)
#aqui definimos las variables
x, y = 25, 7
# ahora puedo colocar los parametros en el orden que quiera y asignarles el valor de las variables x y.
funcion01(b= x, a=y)

#no podemos poner mas, menos o diferentes argumentos que el numero de parametros.

#PARAMETROS POR DEFECTO
# para solucionarlo podemos asignar unos valores por defecto nulos a los parametros

def test(a=25, b=7):
    print(a-b)

test(a=10)
#si no cambiamos el valor del parametro a la hora de colocar el argumento, entonces
# tomara el valor original, en el caso contrario tomara el valor del argumento.

# PASO POR REFERENCIA
# El programa trabaja en base a la ubicacion de la memoria en donde esta la variable,
# la otra forma es PASE POR VALOR, donde no trabaja con la ubicacion de la memoria, sino
# con el valor de la variable. Para que trabaje de una forma u otra debemos de cambiar la forma
# en la que presentamos el argumanto de la funcion (por decirlo de alguna manera el type del argumento)

#***ADJUNTAR EJEMPLO DEL PROFE***

# CREAR UNA FUNCION QUE RECIBA UN ENTERO Y CALULE EL FACTORIAL
# DE ESE NUMERO

# CREAR UNA FUNCION QUE RECIBA 3 NUMEROS Y VERIFIQUE SI SE CUMPLE
# QUE EL TERCER NUMERO ESTA ENTRE LOS PRIMEROS 2

# CREAR UNA FUNCION QUE CUENTE EL NUMERO DE ESPACIOS DENTRO DE UNA CADENA

#FUNCIONES RECURSIVAS
# suele utilizarse para dividir una tarea en subtareas mas simples de forma que sea mas facil abordar
#el problema y solucionarlo.
# dentro de la funcion se manda llamar a la misma funcion
num = 4
def cuenta_regresiva(num):
    num -=1
    if num > 0:
        print(num)
        cuenta_regresiva()
    else:
        print('BOOOM')
    print("Fin de la funcion")



