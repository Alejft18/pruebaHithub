#punto 1

#producto 1 = 5%
#producto 2 =10%
#producto 3 = 15%

#solo pueden llevar 3 productos 

#si el valor final es mas del 100.000 se hara un descuento del 5% y si es menor es un descuento del 2%

while True:
    producto1= int(input("Digita el valor del primer producto "))

    if producto1<=0:
        print("Digite un precio para el producto 1")
    else:
        producto2= int(input("Digita el valor del segundo producto "))

        if producto2<=0:
            print("Digite un precio para el producto 2")
        else:
            producto3= int(input("Digita el valor del tercer producto "))

            if producto3<=0:
                print("Digite un precio para el producto 3")
            else:

                descuento1=(producto1*5)/100
                descuento2=(producto2*10)/100
                descuento3=(producto3*15)/100

                subtotal=(producto1-descuento1)+(producto2-descuento2)+(producto3-descuento3)


                if subtotal>=100000:
                    descuentoFin=(subtotal*5/100)

                else:
                    descuentoFin=(subtotal*2)/100


                valFin=subtotal-descuentoFin

                print(f"el descuento del producto 1 es {descuento1}")
                print(f"El nuevo valor del producto 1 es de {producto1-descuento1}")

                print(f"el descuento del producto 2 es {descuento2}")
                print(f"El nuevo valor del producto 2 es de {producto2-descuento2}")

                print(f"el descuento del producto 3 es {descuento3}")
                print(f"El nuevo valor del producto 3 es de {producto3-descuento3}")

                print(f"El subtotal de la compra es: {subtotal}")
                print(f"Su descuento por el subtotal es {descuentoFin}")
                print(f"El total a pagar es de : $ {valFin}")

                pregunta=input("¿Desea vover a iniciar el programa? \n si=s  \n No=n \n ")
                if pregunta=="n":
                    break
