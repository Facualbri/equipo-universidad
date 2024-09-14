pizza = str(input("¿Quiere una pizza vegetariana (si/no): "))
pizza.upper()

if pizza == "si":
    ingrediente = int(input("ingrese el numero del ingrediente que le quiere añadir a su pizza\n 1.pimiento\n 2.tofu\n"))
    if ingrediente == 1:
         ingrediente = "pimiento"
    else:
         ingrediente = "tofu"
    print(f"su pizza es vegetariana y contiene los siguentes ingredientes:\n mozzarella\n tomate \n {ingrediente}")

else: 
     ingre = int(input("ingrese el numero del ingrediente que le quiere añadir a su pizza:\n 1.peperoni\n 2.jamon\n 3.salmon\n"))
     if ingre == 1:
          ingre = "peperoni"
     elif ingre == 2:
          ingre = "jamon"
     else:
          ingre = "salmon"
     print(f"su pizza no es vegetariana y contiene los siguentes ingredientes:\n mozzarella\n tomate \n {ingre}")