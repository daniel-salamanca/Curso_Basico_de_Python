def run():
    print("Las tablas de mustiplicar")
    for tablas  in range(1,11):
        print("tabla del "+ str(tablas) )
        for multiplicador in range(1,11):
            print(str(tablas)+"*"+str(multiplicador)+"="+str(tablas * multiplicador))
            
    
if __name__ == "__main__":
    run()