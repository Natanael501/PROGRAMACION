from typing import AnyStr


def teorema_de_pitagoras(*args):
    if args[AnyStr] % 2 == 0:
        print(args)

    else:
        print(f'{args} es impar')

Numeros_de_la_suerte = [1, 2, 3, 4]
Resultado = teorema_de_pitagoras(Numeros_de_la_suerte)
print(Resultado)