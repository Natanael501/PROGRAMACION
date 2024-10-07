###FUNCIONES
# Son fragmentos de código que se pueden ejecutar múltiples veces.
# Pueden recibir y devolver información para comunicarse con el proceso principal.

def saludar(name = 'Alfredo'):
    print("Hola pinche bola de mayates les habla su compa", name)

print(saludar('Adame'))
#Dentro de una función podemos utilizar variables y sentencias de control:
def dibujar_tabla_del_5():
    for i in range(10):
        print("5 * {} = {}".format(i, i*5))

dibujar_tabla_del_5()