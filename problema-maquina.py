bebidas = {'coca cola': 50, 'sprite': 50, 'fanta de uva': 50}
snacks = {'lays': 30, 'doritos': 30, 'papas sultas': 30}
dulces = {'chupetin': 10, 'huevo kinder': 10, 'alfajor rasta': 10}

presupuesto = float(input("Ingresa tu presupuesto: "))

if presupuesto <= 0:
    print("El presupuesto debe ser mayor a cero.")
else:
    print("\nBebidas disponibles:")
    tiene_opciones = False
    if presupuesto >= 50:
        print(" - coca cola: $50")
        tiene_opciones = True
    if presupuesto >= 50:
        print(" - sprite: $50")
        tiene_opciones = True
    if presupuesto >= 50:
        print(" - fanta de uva: $50")
        tiene_opciones = True
    
    print("\nSnacks disponibles:")
    if presupuesto >= 30:
        print(" - lays, doritos, papas sueltas: $30")
    else:
        print("saldo insuficiente")

    
    print("\nDulces disponibles:")
    if presupuesto >= 10:
        print(" - chupetin: $10")
        tiene_opciones = True
    if presupuesto >= 10:
        print(" - huevo kinder: $10")
        tiene_opciones = True
    if presupuesto >= 10:
        print(" - alfajor rasta: $10")
        tiene_opciones = True

    # Si no hay opciones disponibles, mostrar un mensaje
    if not tiene_opciones:
        print("Saldo insuficiente para cualquier producto.")
    else:
        # Solicitar la categoría elegida
        categoria_elegida = input("\nElige una categoría (bebidas, snacks, dulces): ").strip().lower()
        
        # Verificar la categoría y mostrar productos disponibles
        if categoria_elegida == 'bebidas':
            print("\nProductos de bebidas disponibles:")
            tiene_producto = False
            if presupuesto >= 50:
                print(" - coca cola: $50")
                tiene_producto = True
            if presupuesto >= 50:
                print(" - sprite: $50")
                tiene_producto = True
            if presupuesto >= 50:
                print(" - fanta de uva: $50")
                tiene_producto = True
            if not tiene_producto:
                print("No hay productos disponibles en la categoría 'bebidas' con el presupuesto dado.")
            else:
                producto_elegido = input("\nElige un producto de la categoría bebidas: ").strip().lower()
                if producto_elegido == 'coca cola' and presupuesto >= 50:
                    precio_producto = 50
                elif producto_elegido == 'sprite' and presupuesto >= 50:
                    precio_producto = 50
                elif producto_elegido == 'fanta de uva' and presupuesto >= 50:
                    precio_producto = 50
                else:
                    print("Producto no válido o no disponible.")
                    precio_producto = None
                
        elif categoria_elegida == 'snacks':
            print("\nProductos de snacks disponibles:")
            tiene_producto = False
            if presupuesto >= 30:
                print(" - lays: $30")
                tiene_producto = True
            if presupuesto >= 30:
                print(" - doritos: $30")
                tiene_producto = True
            if presupuesto >= 30:
                print(" - papas sultas: $30")
                tiene_producto = True
            if not tiene_producto:
                print("No hay productos disponibles en la categoría 'snacks' con el presupuesto dado.")
            else:
                producto_elegido = input("\nElige un producto de la categoría snacks: ").strip().lower()
                if producto_elegido == 'lays' and presupuesto >= 30:
                    precio_producto = 30
                elif producto_elegido == 'doritos' and presupuesto >= 30:
                    precio_producto = 30
                elif producto_elegido == 'papas sultas' and presupuesto >= 30:
                    precio_producto = 30
                else:
                    print("Producto no válido o no disponible.")
                    precio_producto = None
                
        elif categoria_elegida == 'dulces':
            print("\nProductos de dulces disponibles:")
            tiene_producto = False
            if presupuesto >= 10:
                print(" - chupetin: $10")
                tiene_producto = True
            if presupuesto >= 10:
                print(" - huevo kinder: $10")
                tiene_producto = True
            if presupuesto >= 10:
                print(" - alfajor rasta: $10")
                tiene_producto = True
            if not tiene_producto:
                print("No hay productos disponibles en la categoría 'dulces' con el presupuesto dado.")
            else:
                producto_elegido = input("\nElige un producto de la categoría dulces: ").strip().lower()
                if producto_elegido == 'chupetin' and presupuesto >= 10:
                    precio_producto = 10
                elif producto_elegido == 'huevo kinder' and presupuesto >= 10:
                    precio_producto = 10
                elif producto_elegido == 'alfajor rasta' and presupuesto >= 10:
                    precio_producto = 10
                else:
                    print("Producto no válido o no disponible.")
                    precio_producto = None
                
        else:
            print("Categoría no válida.")
            precio_producto = None
        
        # Si se seleccionó un producto válido, procesar el pago
        if precio_producto is not None:
            cantidad_ingresada = float(input("Ingresa el valor con el que vas a pagar: "))
            if cantidad_ingresada < precio_producto:
                print("Saldo insuficiente para pagar el producto seleccionado.")
            else:
                vuelto = cantidad_ingresada - precio_producto
                if vuelto > 0:
                    print(f"Has recibido un vuelto de ${vuelto:.2f}.")
                else:
                    print("No hay vuelto. Gracias por tu compra.")

                print(f"No hay productos disponibles en la categoría '{categoria_elegida}' con el presupuesto dado.")
            else:
                # Solicitar el producto elegido
                producto_elegido = input("\nElige un producto de la categoría seleccionada: ").strip().lower()
                
                # Verificar si el producto elegido es válido
                if producto_elegido in productos_categoria:
                    precio_producto = productos_categoria[producto_elegido]
                    
                    # Solicitar el valor con el que se va a pagar
                    cantidad_ingresada = float(input("Ingresa el valor con el que vas a pagar: "))
                    
                    # Verificar si la cantidad ingresada es suficiente
                    if cantidad_ingresada < precio_producto:
                        print("Saldo insuficiente para pagar el producto seleccionado.")
                    else:
                        vuelto = cantidad_ingresada - precio_producto
                        if vuelto > 0:
                            print(f"Has recibido un vuelto de ${vuelto:.2f}.")
                        else:
                            print("No hay vuelto. Gracias por tu compra.")
                else:
                    print("Producto no válido o no disponible.")
        else:
            print("Categoría no válida.")
