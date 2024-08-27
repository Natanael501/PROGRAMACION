###Mutabilidad de Range
#El objeto que devuelve range() es un tipo de objeto inmutable. Esto significa que, una vez creado, no se puede cambiar.
r = range(10)  # Crea un objeto range de 0 a 9
print(r[2])   # Accede al tercer elemento (2)
# r[2] = 10   # Esto generaría un error porque no se puede modificar un objeto range

###Suma
#El objeto range es una secuencia inmutable que representa una serie de números generados sobre la marcha, en lugar de almacenarse en memoria. Por lo tanto, range no soporta la operación de suma directa porque no tiene una implementación específica para combinar dos rangos.
r1 = range(5)   # 0, 1, 2, 3, 4
r2 = range(5, 10) # 5, 6, 7, 8, 9
# r3 = r1 + r2  # Esto generará un error de TypeError

###Producto por un entero
#Los objetos "range" en Python no soportan la multiplicación por un entero de la misma manera que las listas o las cadenas.
r = range(5)
# r * 3  # Esto generará un error de TypeError

###Slicing
#Los objetos range en Python sí soportan slicing (rebanado), lo que te permite acceder a una subsecuencia de los números en el rango de la misma manera que lo harías con listas o cadenas.
# ejemplo: r = range(10)  # Esto genera la secuencia: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
sub_r = r[2:7]  # Obtiene desde el índice 2 hasta el 6 (excluye el índice 7)
print(list(sub_r))

###Convertir a lista o tupla
#1.Para convertir a lista
r = range(5)  # Esto genera la secuencia: 0, 1, 2, 3, 4
lista = list(r)
print(lista)
#2.Convertir a tupla
r = range(5)  # Esto genera la secuencia: 0, 1, 2, 3, 4
tupla = tuple(r)
print(tupla)

###Funcion len
#La funcion len te devolverá el número de elementos en el rango.
longitud = len(r)
print(longitud) # la salida nos deberia de dar
