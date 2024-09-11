#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un 
# nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al 
# usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = str(input("Introduce tu nombre: "))
sexo = str(input("Introduce tu sexo (F para femenino, M para masculino): ").upper())
    
nombre.upper()

if sexo == 'F':
        if nombre[0].upper() < 'femenino':
            grupo = ("perteneces al grupo A")
        else:
            grupo = ("perteneces al grupo B")
elif sexo == 'masculino':
        if nombre[0].upper() < 'N':
            grupo = grupo = ("perteneces al grupo A")
        else:
            grupo = ("perteneces al grupo B")
else:
        grupo = grupo = ("sexo no valido")

print(f"El grupo que te corresponde es: {grupo}")

