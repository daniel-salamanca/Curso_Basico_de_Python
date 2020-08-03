def factorial(factor):
    if factor ==0 or factor ==1:
        resultado = 1
    elif factor > 1:
        resultado = factor * factorial(factor - 1)
    return resultado


def es_primo(numero):
    factor = numero - 1
    contador = factorial(factor) + 1
    sobrante =contador % numero
    if sobrante == 0:
        return True
    else:
        return False


def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == "__main__":
    run()