monto=float(input("ingrese monto que desea gastar:"))
accion= "1- call of duty: $500, 2- halo: $550, 3- GTA V: $600"
estrategia= "4- Civilizacion VI: $400, 5- Starcraft II: $450, 6- AoE IV: $500"
aventura= "7- The Legend of Zelda: $300, 8- Uncharted 4: $350, 9- Assasin´s creed Valhalla: $400"
try:
    if monto <300:
        raise ValueError("no hay juegos disponibles por ese monto")
    elif monto<400:
        print(f"juegos disponibles:")
        print(aventura)
        juego=input("numero de juego elegido:")
    elif monto<500:
        print("juegos disponibles:")
        print(estrategia,aventura)
        juego=input("ingrese numero de juego:")
    elif monto <600:
        print("juegos disponibles:")
        print(accion,estrategia,aventura)
        juego=input("ingrese numero de juego:")
    match juego:
        case "1":
            montojuego=500
            nomJuego= "Call of Duty"
        case "2":
            montojuego=550
            nomJuego="Halo"
        case "3":
            montojuego=600
            nomJuego="GTA IV"
        case "4":
            montojuego=400
            nomJuego="Civilizacion VI"
        case "5":
            montojuego=450
            nomJuego="Starcraft II"
        case "6":
            montojuego=500
            nomJuego="Age of Empire IV"
        case "7":
            montojuego=300
            nomJuego="The Legend of Zelda"
        case "8":
            montojuego=350
            nomJuego="Uncharted 4"
        case "9":
            montojuego=400
            nomJuego="Assasin´s Creed Valhalla"
    montoPagar=float(input("ingrese monto para pagar:"))
    vuelto=float(montoPagar-montojuego)
    if vuelto<0:
        print("Dinero insuficiente")
    else:
        print(f"Es posible realizar la compra.\n Juego seleccionado: {nomJuego}\nsu vuelto es ${vuelto}")
finally:()