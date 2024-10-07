#1. Funciones que toman argumentos:
#Cuando defines una función, puedes especificar cuántos argumentos necesita.
#Los argumentos son los valores que pasas a la función cuando la llamas.

#Ejemplo básico:
def greet(name):
    print(f"Hello, {name}!")
#Aquí, name es un argumento.
#Cuando llamas a greet("Alice"), el valor "Alice" se asigna al argumento name.
#Varias formas de pasar argumentos:
#Posicional: El argumento se asigna según la posición en que lo pasas.
#Nombrado: Puedes especificar el nombre del argumento cuando llamas a la función.

#Ejemplo con varios argumentos:
def add(a, b):
    return a + b

result = add(3, 5)  # Llamada posicional
print(result)  # Output: 8
#En este caso, la función add espera dos argumentos y devuelve su suma.

#2. Argumentos opcionales y por defecto:
#Puedes definir valores predeterminados para los argumentos,
#lo que hace que algunos sean opcionales.
def greet(name, message="Hello"):
    print(f"{message}, {name}!")
#Aquí, message tiene un valor por defecto ("Hello").
#Puedes llamar a la función con uno o dos argumentos:

greet("Alice")          # Output: Hello, Alice!
greet("Bob", "Hi")      # Output: Hi, Bob!
#Si no proporcionas el segundo argumento, se usa el valor predeterminado.

#3. Recibir un número variable de argumentos:
#Si no sabes cuántos argumentos vas a pasar a la función, puedes usar *args o **kwargs:

#*args: Recoge múltiples argumentos posicionales en una tupla.
#**kwargs: Recoge múltiples argumentos con nombre (keyword arguments) en un diccionario.
#Ejemplo con *args:
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(4, 5))     # Output: 9

#Aquí, *args recoge todos los valores que pasas en una tupla (1, 2, 3).

#Ejemplo con **kwargs:
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", message="Hello", age=25)
#Aquí, **kwargs captura todos los argumentos con nombre como
# un diccionario: {"name": "Alice", "message": "Hello", "age": 25}.

#4. Funciones que devuelven valores:
#Una función en Python puede devolver uno o varios valores usando la palabra clave
#return. Después de ejecutar return, la función termina y el valor o valores se devuelven
#al lugar donde se llamó la función.

#Ejemplo básico:
def multiply(a, b):
    return a * b

result = multiply(3, 5)
print(result)  # Output: 15

#Devolver múltiples valores:
#Si quieres devolver más de un valor, puedes hacerlo separándolos por comas.
#Python los agrupa en una tupla automáticamente.

def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print(x, y)  # Output: 10 20

#Aquí, get_coordinates() devuelve una tupla (10, 20), y puedes "desempaquetarla"
#en las variables x y y.

#5. Desempaquetado en funciones:
#De la misma manera que con enumerate() en los bucles for, puedes "desempaquetar"
#valores cuando llamas a una función o cuando devuelve múltiples valores.

#Ejemplo de desempaquetado al pasar argumentos:

def print_info(name, age):
    print(f"Name: {name}, Age: {age}")

info = ("Alice", 30)
print_info(*info)  # Output: Name: Alice, Age: 30

#Aquí, *info desempaqueta la tupla y pasa los valores a name y age.

#Desempaquetar un diccionario con **:

def print_info(name, age):
    print(f"Name: {name}, Age: {age}")

info = {"name": "Bob", "age": 25}
print_info(**info)  # Output: Name: Bob, Age: 25

#6. Funciones lambda (funciones anónimas):
#Puedes definir funciones "en una sola línea" usando lambda.
#Son útiles cuando necesitas funciones pequeñas y simples.

sum_lambda = lambda a, b: a + b
print(sum_lambda(3, 4))  # Output: 7
#lambda crea una función anónima que toma dos argumentos a y b y devuelve su suma.

#7. Manejo de errores en funciones:
#Puedes hacer que tus funciones sean más robustas usando try y except para manejar
#posibles errores:

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed."

print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Division by zero is not allowed.

####Resumen:
# 1.Las funciones pueden recibir argumentos que defines al llamarlas.
# 2.Pueden devolver uno o más valores, y puedes desempaquetarlos si es necesario.
# 3.Los argumentos pueden ser posicionales, con nombre, opcionales
# (con valores predeterminados), o incluso un número variable de ellos (*args y **kwargs).
# 4.Puedes manejar errores dentro de funciones y también usar lambda para crear
# funciones pequeñas y simples.
# 5.El principio general es el mismo que con el desempaquetado en bucles:
# si una función recibe o devuelve múltiples valores, asegúrate de asignar
# la cantidad correcta de variables para manejarlos correctamente.