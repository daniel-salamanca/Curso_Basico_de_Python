import random


def run():
    numero_aleatorio = random.randint(1, 100 )
    numero_elegido = int(input("Elige un número del 1 al 100: "))
    contador = 0

    while numero_elegido != numero_aleatorio or contador == 3 :
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande') 
        else:
            print('Busca un número más pequeño') 
        contador += 1
        numero_elegido = int(input("Elige otro número: "))

    if contador == 3:
        print ("perdiste")
    else:
        print("ganaste")  



if __name__ == "__main__":
    run()