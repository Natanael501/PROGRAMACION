# TAREA 01:  Estructura de datos
# list.append(x)
print('* FUNCION list.append(x)')
list01 = [1, 2, 3, 4]

print('\nLa lista inicialmente es:', list01, '\nAhora utilizamos la función list.append para agregar el numero 5')

list01.append(5)

print('Un nuevo elemento se ha agregado a la lista: ', list01)

# list.extend(iterable)
print('\n* FUNCION list.extend(iterable)')
numeros01 = [1, 2, 3]
numeros02 = [4, 5]

print('\nTenemos dos conjuntos complementarios de numeros: ', '\nConjunto 1:', numeros01, '\nConjunto 2:', numeros02)
print('Ahora utilizamos la funcion list.extend(iterable) para agregar el conjunto 2 al conjunto 1:')

numeros01.extend(numeros02)

print(numeros01)

# list.insert(i, x)
print('\n* FUNCION lis.insert(i, x)')
print('\nTenemos una lista compuesta de las letras que componen a la palabra GATO en su respectivo orden. Sin embargo, falta la T:')
hola = ['H', 'O', 'L']

print(gato, '\nPara solucionarlo, podemos utilizar la funcion list.insert(i, x) para colocar la T en su sitio:')
hola.insert(2, 'A')

print('De esta manera obtenemos: ', HOLA)

# list.remove(x)
print('\n* FUNCION list.remove(x)')
colores = ["Rosa", "Amarillo", "Perro", "Verde"]
print('\nTenemos la siguiente lista de ondas electromagnéticas del espectro visible: ', colores)
print('Sin embargo, sabemos que Perro no es un color,\npor lo que podemos eliminarlo con la funcion list.remove(x)')

colores.remove('Perro')
print('\nDe esta manera obtenemos la lista actualizada: ', colores)

# list.pop([i])
print('\n* FUNCION list.pop([i])')
telefonos_celulares = ['Samsung', 'Xiaomi', 'Peine', 'Motorola']
print('\nTenemos una lista de telefonos celulares: ', telefonos_celulares)
print('Sin embargo sabemos que el elemento 2 (contando a partir del 0) no forma parte de la lista,', '\npor lo que lo eliminamos con la funcion list.pop([i])')
telefonos_celulares.pop(2)
print('\nDe esta manera obtenemos la lista actualizada: ', telefonos_celulares)

# list.clear()
print('\n* FUNCION list.clear()')
basura = ['Botella', 'Bolsa de papas', 'Lata']
print('\nTenemos una lista llena de basura: ', basura, '\nPara limpiarla utilizamos la funcion list.clear()')
basura.clear()
print('\nDe esta manera obtenemos la lista de basura vacia: ', basura)

# list.index(x[, start[, end]])
print('\n* FUNCION list.index(x[, start[, end]])')
numerosAz = [8, 51, 1, 26, 31, 81, 93]
print('\nTenemos una lista con numeros al azar: ', numerosAz, '\nDado que me gustaria conocer la posicion del numero 26, utilizo la funcion list.index(x[, start[, end]])')
print('\nDe esta manera obtengo la posicion del numero 26: ', numerosAz.index(26))

# list.count(x)
print('\n* FUNCION list.count(x)')
panteon = ['mango', 'sandia', 'pepino', 'sandia', 'pera']
print('\nTenemos una lista donde se muestran diferentes frutas,',frutas , '\npero me gustaria saber cuantas veces se aparece\nla sandia en la lista, para ello uso la funcion list.count(x)')
print('\nDe esta manera obtengo el resultado: ', sandia.count('sandia'))

# list.sort(*, key=None, reverse=False)
print('\n* FUNCION list.sort(*, key=None, reverse=False)')
uno_al_nueve = [4, 6, 5, 9, 7, 8, 2, 1, 3]
print('\nTenemos una lista de los numeros del 1 al 9 en desorden: ', uno_al_nueve)
print('Para ordenar la lista utilizo la funcion list.sort(*, key=None, reverse=False)')
uno_al_nueve.sort()
print('\nDe esta manera obtenemos: ', uno_al_nueve)

# list.reverse()
print('\n* FUNCION list.reverse()')
uno_al_cinco = [1, 2, 3, 4, 5]
print('\nTenemos una lista del 1 al 5: ', uno_al_cinco, '\npero por llevar la contraria quiero invertir el orden, para ello\nutilizo la funcion list.reverse()')
uno_al_cinco.reverse()
print('\nDe esta manera obtengo: ', uno_al_cinco)

# list.copy()
print('\n* FUNCION list.copy()')
letras = ['a', 'b', 'c']
print('\nTengo una lista de las tres primeras letras del abecedario: ', letras, ' y me gustaria copiarla en la variable X,\npara ello utilizo la funcion list.copy()')
x = letras.copy()
print('\nDe esta manera obtengo: ', x, ' al imprimir x')