#punto 2

#ascensor de 10 pisos
#no hay sotano

#el ascensor comienza en el piso



ascensor=1


while True:
    print("digite n pasa salir")
    print("digite s para iniciar")
    respuesta=input("¿Desea iniciar el ascensor? ")

    if respuesta=="n":
        break

    pedir=int(input("¿En que piso se encuentra? "))

    if ascensor<pedir:
        print("El ascensor esta subiendo")
        
        for i in range(ascensor,pedir+1):
            print(f"Estoy en el piso {i}")
        
        ascensor=pedir
        print("Puertas abiertas")

    elif ascensor==pedir:
        print("el ascensor se encuentra en ese piso")
    
    else:
        print("El ascensor esta bajando")
        for i in range(ascensor,pedir+1,-1):
            print(f"Estoy en el piso {i}")
        
        ascensor==pedir
        print("Puertas abiertas")




    pisoFin=int(input("¿A que piso vas? "))
    
    if ascensor<pisoFin:
        for i in range(ascensor,pisoFin+1,1):
            print(f"Estoy en el piso {i}")
        
        ascensor==pisoFin
        print("El ascensor esta en su piso")
        print("Puertas abiertas")

    elif ascensor > pisoFin:
        while i >= pisoFin:
                print(f"Estoy en el piso {i}")
                i=i-1
        ascensor==pisoFin
        print("El ascensor esta en su piso")
        print("Puertas abiertas")
