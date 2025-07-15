productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], 
         '2175HD': [327990,4], 
         'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21], 
         '123FHD': [290890,32], 
         '342FHD': [444990,7],
         'GF75HD': [749990,2], 
         'UWU131HD': [349990,1], 
         'FS1230HD': [249990,0]}

##opcion 1
def stock_marca(marca):
    encontrado = False
    for modelo in productos:
        if productos[modelo][0].lower() == marca.lower():
            if modelo in stock:
                nombre = productos[modelo][0]
                cantidad = stock[modelo][1]
                print(f"Marca: {nombre} // cantidad disponible: {cantidad}")
            encontrado = True
    if not encontrado:
        print ("No se ha encontrado este modelo ")

#stock_marca("")

##opcion 2

def busqueda_precio(p_min, p_max):
    lista =[]
    
    for modelo in stock:
        precio, cantidad = stock[modelo]
        if p_min <= precio <= p_max and precio > 0:
            marca = productos.get(modelo, [""])[0]
            lista.append(f"{marca} // {modelo}")

            if lista:
                lista.sort()
                print("Computadores en el rango de precios")
                for item in lista:
                    print(item)
            else:
                print("No hay computadores en ese rango de precios")

#busqueda_precio(290000,900000)


##opcion 3                

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    else:
        return False

#actualizar_precio()

def menu():
    while True:
        print ("*** MENU PRINCIPAL ***")
        print("[1] - Stock marca")
        print("[2] - Busqueda por precio")
        print("[3] - Actualizar precio")
        print("[4] - SALIR")

        while True:
            try:
                opcion = int(input("Ingrese una opcion: "))
                if opcion < 1 or opcion > 4:
                    print ("Ingrese una opcion valida(1, 2, 3 o 4)")
                    continue
            except ValueError:
                print ("Solo puede ingresar valores enteros(1, 2, 3 o 4)")
                continue
            break


        if opcion == 1:
            while True:
                try:
                    marca = input("Ingrese la marca a consultar: ").lower()
                    if marca == "":
                        print("Esta opcion no puede estar vacia")
                        continue
                except ValueError:
                    print ("Debe ingresar caracteres")
                    continue 
                break
            stock_marca(marca)

        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese el Precio minimo: "))
                    p_max = int(input("Ingrese el Precio maximo: "))

                    if p_min > p_max:
                        print ("El minimo no puede ser mayor que el maximo")

                    else:
                        break

                except ValueError:
                    print ("Debe ingresar valores enteros!!")
                    continue 
                break
            busqueda_precio(p_min, p_max)


        elif opcion == 3:
            while True:
                try:
                    modelo = input("Ingrese el modelo: ").lower()
                    if modelo == "":
                        print ("Esta area no puede estar vacia")
                        while True:
                            try:
                                nuevo_precio = int(input("Ingrese el nuevo precio que le asignara al producto: "))
                                if nuevo_precio < 0:
                                    print ("Ingrese un precio valido")
                                    continue 
                            except ValueError:
                                print ("Solo puede ingresar enteros")
                                continue 
                            break
                    actualizado = actualizar_precio(modelo, nuevo_precio)
                    if actualizado:
                        print("Precio actualizado con exito")
                    else: 
                        print (("El modelo no existe"))


                except ValueError:
                    print ("Ingrese caracteres validos")
                    continue
                while True:
                    try:
                        continuar = input ("¿Desea actualizar otro precio?(si/no): ").lower()
                        if continuar != "si" or continuar != "no":
                            print ("Debe escribir una opion valida(si/no)")
                            if continuar != "si":
                                continue
                    except ValueError:
                        print("Debe escribir una opcion valida(si/no)")
        elif opcion == 4:
            print ("SALIENDOOOO")
            break


menu()

