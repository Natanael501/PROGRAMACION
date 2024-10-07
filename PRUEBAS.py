###Asignadores
#Operadores de asignación, relacionales y logicos:
#En programación, una variable está formada por un espacio en el sistema de almacenaje
#- y un nombre simbólico que está asociado a dicho espacio.

#Ese espacio contiene una cantidad de información conocida o desconocida, es decir un valor.

##Operadores de asignación
#Los operadores de asignación que se verán en el curso son:
# =, +=, *=, /=, //=, %=, **=. != (diferente a)

# +=, simplifica una suma de un número a una variable
Variable1 = 15
Variable1 += 5

print(Variable1)

# Operadores relacionales
#Los operadores relacionales a considerar son: (siempre son resultados boelianos)

##Operadores logicos: son or, and y not (not es la negación lógica)

###Expresiones anidadas
#Se pueden solucionar empleando las reglas de preferencia:
#Primero, los parentesis: Segundo, las expresiones aritmeticas
# Tercero, las expreciones racionales: Cuarto, las expresiones lógicas


###CONTROLADORES DE FLUJO
#se trata de una estructura de control condicional.
#Nos permite evaluar si una o más condiciones se cumplen
#Para decidir qué acción vamos a ejecutar.

#Sentencia If (Sì)
#Permite dividir el flujo de un programa en diferentes caminos.
#El if se ejecuta siempre que la expresión que comprueba devuleva True
if True:
    print('TARTARO') #si mi if es verdadero se hace lo que yo quería hacer, si es false entonces no se hace
#si quiero que se ejecute algo tambièn cuando mi if sea False sería:
#Ejemplo de if else
condicional = (5-16) and False
if condicional:
    print('la condicional es verdadera')
else:
    print('la condicional es falsa')

## Tercer comando elif doble condicional(si mi condicional es falso entonces elif nos ayuda a condicionar esa respuesta falsa)
condicional = 55
if condicional < 10:
    print('chiquito')
elif condicional <25:
    print('mediano')
elif condicional > 2:
    print('Grande')
###Comando pass (para "saltar esa parte del código y que no nos salga error")
if condicional != 0:
    pass
### Sentencia For (para) listas
numeros = [1,2,3,4,5]
for idx in numeros: #Para (variable local) en (lista)
    print(idx) #el idx literal puede ser cualquier palabra

###1ra pregunta
x = int(input('INTRODUCE UN NUMERO: '))
serie = [0, 1]
print(x)


def fibo(long, ser, aum, ant):
    if aum != long:
        aum += 1
        ser += ant
        serie.append(ser)
        ant = serie[-2]
        fibo(long, ser, aum, ant)

    else:
        print(serie)
        print('El ultimo numero es: ', serie[-1])


fibo(x, 1, 0, 0)

def greet (name):
    print(f'¡VECINOS SALGAN! ¡{name}!')

greet('VECINOOOOOS')

def add(a, b):
    return a + b

Resultado = add(358, 342)
print(Resultado)

def teorema_de_pitagoras(*args):
    if args[tuple] % 2 == 0:
        print(args)

    else:
        print(f'{args} es impar')