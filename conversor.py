menu = """
Bienbenido al conversor de monedas 💰

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos
4 - Euros 

Elige una opción:  """

opcion =int(input(menu))

if opcion == 1:
    pesos = input("¿cuántos pesos Colombianos tirns?:  ")
    pesos = float(pesos)
    valor_dolar = 3687
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares +" dólares" ) 
elif opcion == 2:
    pesos = input("¿cuántos pesos Argentinos tirns?:  ")
    pesos = float(pesos)
    valor_dolar = 72.13
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares +" dólares" ) 
elif opcion == 3:
    pesos = input("¿cuántos pesos Mexicanos tirns?:  ")
    pesos = float(pesos)
    valor_dolar = 21.92
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares +" dólares" ) 
elif opcion == 4:
    pesos = input("¿cuántos euros tirns?:  ")
    pesos = float(pesos)
    valor_dolar = 0.85
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares +" dólares" ) 
else:
    print("Ingresa una opción correcta por favor")

