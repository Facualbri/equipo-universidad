try:
    presup = float(input("ingrese su presupuesto: $"))
except ValueError:
   print("ERROR: por favor ingrese un valor valido")

if presup >= 20:
    if presup >= 70:
        juego_clase = int(input("ingrese el numero de la clase de juego que desea:\n 1.accion\n 2.estrategia\n 3.aventura\n"))
        if presup <= 70 and presup > 69 and juego_clase == 1:
            juego1 = int(input("ingrese el numero del juego que desea:\n 1.call of duty- $70\n 2.halo- $70\n 3.GTA V- $70\n"))
            juego1 = 70
            vuelto = presup - juego1
            print(f"le orresponde ${vuelto} de vuelto")
        elif presup <= 50 and presup > 49 or juego_clase == 2:
             if juego_clase == 2:
                juego2 = int(input("ingrese el numero del juego que desea:\n 1.civilization VI- $50\n 2.age of empires IV- $50\n 3.starcraft II- $50\n"))
                juego2 = 50
                vuelto = presup - juego2
                print(f"le orresponde ${vuelto} de vuelto")
             elif juego_clase != 3 and juego_clase != 2:
                juego_clase = int(input("ingrese el numero de la clase de juego que desea:\n 1.estrategia\n 2.aventura\n"))
                juego2 = int(input("ingrese el numero del juego que desea:\n 1.civilization VI- $50\n 2.age of empires IV- $50\n 3.starcraft II- $50\n"))
                juego2 = 50
                vuelto = presup - juego2
                print(f"le orresponde ${vuelto} de vuelto")
        elif presup <= 20 and presup > 19 or juego_clase == 3:
         juego3 = int(input("ingrese el numero del juego que desea:\n 1.the legend of zelda- $20\n 2.uncharted 4- $20\n 3.assassin's creed- $20\n"))
         juego3 = 20
         vuelto = presup - juego3
         print(f"le orresponde ${vuelto} de vuelto")
    else:
        juego_clase = int(input("ingrese el numero de la clase de juego que desea:\n 2.estrategia\n 3.aventura\n"))
        if presup <= 70 and presup > 69 and juego_clase == 1:
            juego1 = int(input("ingrese el numero del juego que desea:\n 1.call of duty- $70\n 2.halo- $70\n 3.GTA V- $70\n"))
            juego1 = 70
            vuelto = presup - juego1
            print(f"le orresponde ${vuelto} de vuelto")
        elif presup <= 50 and presup > 49 or juego_clase == 2:
             if juego_clase == 2:
                juego2 = int(input("ingrese el numero del juego que desea:\n 1.civilization VI- $50\n 2.age of empires IV- $50\n 3.starcraft II- $50\n"))
                juego2 = 50
                vuelto = presup - juego2
                print(f"le orresponde ${vuelto} de vuelto")
             elif juego_clase != 3 and juego_clase != 2:
                juego_clase = int(input("ingrese el numero de la clase de juego que desea:\n 1.estrategia\n 2.aventura\n"))
                juego2 = int(input("ingrese el numero del juego que desea:\n 1.civilization VI- $50\n 2.age of empires IV- $50\n 3.starcraft II- $50\n"))
                juego2 = 50
                vuelto = presup - juego2
                print(f"le orresponde ${vuelto} de vuelto")
             elif presup <= 20 and presup > 19 or juego_clase == 3:
              juego3 = int(input("ingrese el numero del juego que desea:\n 1.the legend of zelda- $20\n 2.uncharted 4- $20\n 3.assassin's creed- $20\n"))
              juego3 = 20
              vuelto = presup - juego3
              print(f"le orresponde ${vuelto} de vuelto")

else:
    print(f"saldo insuficiente")