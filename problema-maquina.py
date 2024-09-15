bebidas = {'coca cola': 50, 'sprite': 50, 'fanta de uva': 50}
snacks = {'lays': 30, 'doritos': 30, 'papas sultas': 30}
dulces = {'chupetin': 10, 'huevo kinder': 10, 'alfajor rasta': 10}

presupuesto = float(input("Ingresa tu presupuesto: "))

if presupuesto <= 0:
    print("El presupuesto debe ser mayor a cero.")
else:
    categorias = {
        'bebidas': bebidas,
        'snacks': snacks,
        'dulces': dulces
    }
    
    print("\nProductos disponibles según tu presupuesto:")
    
    opciones_disponibles = False
    
    for categoria, productos in categorias.items():
        productos_disponibles = {p: precio for p, precio in productos.items() if presupuesto >= precio}
        
        if productos_disponibles:
            opciones_disponibles = True
            print(f"\n{categoria.capitalize()} disponibles:")
            for producto, precio in productos_disponibles.items():
                print(f" - {producto}: ${precio}")

    if not opciones_disponibles:
        print("Saldo insuficiente para cualquier producto.")
    else:
        categoria_elegida = input("\nElige una categoría (bebidas, snacks, dulces): ").strip().lower()
        
        if categoria_elegida in categorias:
            productos_disponibles = {p: precio for p, precio in categorias[categoria_elegida].items() if presupuesto >= precio}
            
            if productos_disponibles:
                print("\nProductos disponibles en la categoría elegida:")
                for producto, precio in productos_disponibles.items():
                    print(f" - {producto}: ${precio}")
                
                producto_elegido = input("\nElige un producto: ").strip().lower()
                
                if producto_elegido in productos_disponibles:
                    precio_producto = productos_disponibles[producto_elegido]
                    cantidad_ingresada = float(input("Ingresa el valor con el que vas a pagar: "))
                    
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
                print(f"No hay productos disponibles en la categoría '{categoria_elegida}' con el presupuesto dado.")
        else:
            print("Categoría no válida.")
