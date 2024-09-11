ingreVege= "Pimiento o Tofu"
ingreNoVege= "Peperoni, Jamon o Salmón"
pizza= "mozzarella, tomate y"
vege = input("Quieres una pizza vegetariana?: ").upper()
if vege == "SI":
    print(f"Elige un ingrediente \n{ingreVege}")
    ingre= input("Ingresa el ingrediente: ")
    print("Pizza vegetariana de", ingre)
    print("Ingredientes:",pizza,ingre)
elif vege == "NO":
    print(f"Elige un ingrediente \n{ingreNoVege}")
    ingre= input("Ingresa el ingrediente: ")
    print("Pizza no vegetariana de", ingre)
    print("Ingredientes:",pizza,ingre)