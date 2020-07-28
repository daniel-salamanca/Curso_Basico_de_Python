menu = """
Bienbenido al conversor de monedas 💰

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Eexicanos
4 - Euros 

Elige una opción"""

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
    pass
elif opcion == 3:
    pass
elif opcion == 4
    pass
else:
    print("Ingresa una opción correcta por favor")

