def factorial(numero):
    if numero ==0 or numero ==1:
        resultado = 1
    elif numero > 1:
        resultado = numero * factorial(numero - 1)
    return resultado
    print(resultado)
    


def run():
        numero = int(input("Escriba el numero: "))
        input (factorial(numero))
        

if __name__ == "__main__":
    run()