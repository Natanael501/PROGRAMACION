###Sentencia For
#La sentencia for en Python se utiliza para iterar sobre una secuencia (como una lista
#, una tupla, un diccionario, un conjunto o una cadena).
# Permite realizar una acción repetidamente para cada elemento de la secuencia.

#iterar sobre una lista
frutas = ['manzana', 'banana', 'cereza']
for fruta in frutas:
    print(fruta)
#iterar sobre una cadena
for letra in 'Python':
    print(letra)
#iterar usando range
for i in range(5): #El range(5) genera una secuencia de números del 0 al 4 (el número 5 no se incluye).
    print(i)
#iterar sobre un diccionario
estudiantes = {'Alice': 25, 'Bob': 30, 'Charlie': 28}
for nombre, edad in estudiantes.items():
    print(f'{nombre} tiene {edad} años.')

#EJERCICIOS
#1
for i in range(21):
    if i % 2 == 0: #si i entre 2 es igual a cero entonces:
        print(i) #imprime i

#2
lista1 = ['Fatima', 'Ximena', 'Cheche']
for nombre in lista1 :
    print(nombre, len(nombre))

#3
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for idx, season in enumerate(seasons):
    print(idx, season)

###FUNCIÓN ENUMERATE
#enumerate() es una función incorporada en Python que permite iterar sobre una colección
#(como una lista, tupla o cadena) mientras proporciona un contador automático junto con
#los elementos de dicha colección.
#Cuando utilizas enumerate(), esta función toma un iterable (como una lista) y devuelve
#un iterador que genera pares de tuplas. Cada tupla contiene:
#Un índice (empezando por defecto en 0).
#El elemento correspondiente del iterable.

#Ejemplo
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)
#enumerate(fruits): Esta función toma la lista fruits y crea un iterador que genera
#pares de valores: el índice de cada elemento y el elemento mismo de la lista.
#for index, fruit in enumerate(fruits):: En cada iteración del bucle, el enumerate()
#te devuelve una tupla que contiene dos cosas:

#El índice del elemento (es decir, la posición en la lista, que empieza en 0 por defecto).
#El elemento de la lista en esa posición.
#index, fruit: Aquí, index recibe el valor del índice (0, 1, 2, etc.) y fruit
#recibe el valor correspondiente del elemento en esa posición ('apple', 'banana', 'cherry').

#Por lo tanto, en cada iteración:
#index contiene el número de la posición del elemento en la lista.
#fruit contiene el valor del elemento en esa posición.

##Si usas enumerate() pero solo llamas a una variable, por ejemplo, fruit,
#obtendrás un error. Esto ocurre porque enumerate() devuelve dos valores (el índice y el
#elemento), y si intentas desempacar esos dos valores en una sola variable
#Python no sabrá qué hacer con el otro valor.

#Principio general:
#La clave es que la cantidad de variables a la izquierda del in debe coincidir con la
#cantidad de valores que la función o iterable a la derecha del in está devolviendo.

#Desempaquetar tuplas: Si estuvieras iterando sobre una lista de tuplas,
#puedes desempaquetar directamente los valores de las tuplas.
pairs = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
for number, fruit in pairs:
    print(number, fruit)
#Aquí, cada tupla tiene dos valores, así que debes capturar dos variables.

#entonces, en mi sentencia for puedo hacerle lo que quiera a mi lista siempre y cuando llame a
#todo lo que me de esa función que le puse a mi lista


