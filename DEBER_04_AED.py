#Presentacion del programa....
print("\n ******BIENVENIDO AL BURGER KING****** \n")
print(" Ingrese los datos para la factura electrónica.\n")
#ingreso de datos--
nombre = input(" Ingrese su nombre: ")
cedula = input(" Ingrese su número de cédula: ")
correo = input(" Ingrese su correo: ")
n_hamburguesas = int(input(" Ingrese el número de hamburguesas a adquirir: "))

#opciones a elegir: tipo y forma de pago...
print("\n Ingrese uno de los siguientes tipos de hamburguesas:\n 1) Sencilla\n 2) Doble\n 3) Triple")
opcion = int(input(" Ingrese la opción: "))

precios_hamburguesas = {1: 1.50, 2: 2.50, 3: 3.25}
recargo_por_tarjeta = 0.05
#resolucion del problema....
match opcion:
    case 1 | 2 | 3:
        print("\n Ingrese su forma de pago:\n 1) Tarjeta de crédito\n 2) Efectivo")
        opcion_pago = int(input("Ingrese la opción: "))
        
        if opcion_pago not in [1, 2]:
            print("\n No existe ese tipo de pago.\nMuchas gracias....\n")
        else:
            precio_unitario = precios_hamburguesas[opcion]
            subtotal = n_hamburguesas * precio_unitario

            match opcion_pago:
                case 1:
                    recargo = subtotal * recargo_por_tarjeta
                    total = subtotal + recargo
                case 2:
                    total = subtotal

            print(f"\n Genial, {nombre}, el precio final es ${total:.2f} \n La factura se enviará a su correo {correo}.\n")
    case _:
        print("\n Este tipo de hamburguesa no existe.\nMuchas gracias....")
