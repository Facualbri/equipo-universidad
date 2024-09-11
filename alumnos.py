nombre = str(input("ingrese su nombre: "))
sexo = str(input("ingrese su sexo (masculino/femenino): "))
nombre.upper()

if sexo == "femenino":
    if nombre[0] > "M":
        print(f"pertenece al grupo A")

    else: print("pertenece al grupo B")
    
elif sexo == "masculino":
    if nombre[0] < "N":
        print("pertrnece al grupo A")
    else:
        print("pertenece al grupo B")
else:
    print("sexo no valido")