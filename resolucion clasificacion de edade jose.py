edad=int(input("Ingrese su edad: "))
if edad <2:
    categoria="Infante"
elif 3<= edad <=12:
    categoria="Niño"
elif 13<=edad<=17:
    categoria="Adolecente"
else:
    categoria="Adulto"
print(f"Usted es un {categoria}.")