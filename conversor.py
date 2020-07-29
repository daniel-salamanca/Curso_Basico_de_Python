menu = """
Bienbenido al conversor de monedas 💰

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos
4 - Euros 

Elige una opción:  """

def conversor(tipo_de_moneda,valor_dolar):
    pesos = input("¿cuántos pesos "+tipo_de_moneda+ " tienes?:  ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares +" dólares" ) 


opcion =int(input(menu))

if opcion == 1:
    conversor("Colombianos",3687)   
elif opcion == 2:
    conversor("Argentinos",72.13)
elif opcion == 3:
    conversor("Mexicanos",21.92)
elif opcion == 4:
    conversor("euros",0.85)    
else:
    print("Ingresa una opción correcta por favor")

