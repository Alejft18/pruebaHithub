#punto 3

bisiestos=[1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096]

while True:
    print("digite n pasa salir")
    print("digite s para iniciar")
    respuesta=input("¿Desea iniciar el programa?")

    if respuesta=="n":
        break
    
    dia=int(input("Digite un dia "))
    mes=int(input("Digite un mes "))
    año=int(input("Digite un año "))
    

    if dia<0 and dia>31:
        print("Digite un dia valido")
        break
    if mes<= 0 and mes>12:
        print("Digite un mes valido")
        break
    if año<=0:
        print("Digite un año valido")
        break


    

    if mes==1 and dia==31:
        dia=1
        mes=2

    if año in bisiestos:
        if mes==2 and dia==29:
            dia=0
            mes=3
        
        elif mes==2 and dia<=30:
            print("Esta fecha no existe ")
            break
    
    if año not in bisiestos:
        if mes==2 and dia==28:
            dia=0
            mes=3

        elif mes==2 and dia>28:
            print("Esta fecha no existe")
            break

    
    


    if mes==3 and dia==31:
        dia=0
        mes=4

    if mes==4 and dia >30:
        print("esta fecha no existe")
        break
    if mes==4 and dia==30:
        dia=0
        mes=mes+1


    if mes==5 and dia==31:
        dia=1
        mes=6

    

    if mes==6 and dia >30:
        print("esta fecha no existe")
        break

    if mes==6 and dia==30:
        dia=0
        mes=7

    if mes==7 and dia==31:
        dia=1
        mes=8

    if mes==9 and dia >30:
        print("esta fecha no existe")
        break

    if mes==9 and dia==30:
        dia=0
        mes=10
    
    if mes==10 and dia==31:
        dia=1
        mes=11 

    if mes==11 and dia >31:
        print("esta fecha no existe")
        break
    if mes==11 and dia==30:
        dia=0
        mes=12

    if mes==12 and dia==31:
        mes=1
        dia=0
        año=año+1
    if mes==12 and dia <31:
        mes=12

    dia=dia+1
     
    bisiestos

    
    
    print(f"La siguiente fecha es: {dia} ,{mes}, {año}")