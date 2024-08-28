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