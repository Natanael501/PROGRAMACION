###Creamos el diccionario
diccionario1 = {'llave1': 'olmeca', 'llave2': 'azteca', 'llave3': 'teotihuacan'}
print(diccionario1)

##Pop: Elimina el elemento con la clave especificada y lo devuelve.
nuevo = diccionario1.pop('llave1') #basta con poner la llave del elemento que queremos quitar
print(diccionario1)

# pop (self, __key)
diccionario01 = {'Verde': 1, 'Amarillo': 2, 'Rojo': 3}
valor = diccionario01.pop('Rojo')

print('El valor de la llave eliminada era', valor)

# get (self, __key)
diccionario01 = {'Verde': 1, 'Amarillo': 2, 'Rojo': 3}

print("El valor de la llave verde es", diccionario01.get('Verde'))

# copy (self)
diccionario01 = {'Verde': 1, 'Amarillo': 2, 'Rojo': 3}
Copia_del_diccionario = diccionario01.copy()

print("La copia del diccionario es: ", Copia_del_diccionario)

# keys (self)
Llaves_del_diccionario = diccionario01.keys()

print("Las llaves del diccionario son: ", Llaves_del_diccionario)

# items (self)
lista_de_pares_llave_valor = diccionario01.items()
print("La lista de pares de llaves y sus valores es: ", lista_de_pares_llave_valor)

# clear (self)
dic_limpio = diccionario01.clear()

print("El diccionario ha sido limpiado: ", diccionario01)

# fromkeys (cls, __iterable, __value)
Llaves = ["Llave01", "Llave02", "Llave03"]
Valores = ":D"
Nuevo_diccionario = diccionario01.fromkeys(Llaves, Valores)
print("Se han asignado nuevas llaves y nuevos valores al diccionario: ", Nuevo_diccionario)

# popitem (self)
Diccionario01 = {"Llave01":1 , "Llave02": 2, "Llave03": 3}
Eliminacion_01 = Diccionario01.popitem()
print('Del diccionario ha sido eliminado un elemento', Diccionario01, "por lo que el\npar eliminado ha sido", Eliminacion_01)

# setdefault(self, __key, default)

Valor = Diccionario01.setdefault("Llave04", 4)
print('El valor es', valor, ' y se reasigna, por lo que el nuevo diccionario es', Diccionario01)

# update (self, __m, kwargs)
Diccionario01 = {"Llave01":1 , "Llave02": 2, "Llave03": 3}
Diccionario01.update({'Llave04': 4, 'Llave05': 5})
print('Se agregaron elementos al diccionario: ', Diccionario01)

# values (self)
Lista_valores = Diccionario01.values()
print("Los valores del diccionario son: ", Lista_valores)
