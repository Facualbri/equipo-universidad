examen1 =float(input("ingrese la nota del primer examen: "))
examen2 =float(input("ingrese la nota del segundo examen: "))
examen3 =float(input("ingrese la nota del tercer examen: ")) 
umbralaprobacion= float(input("ingrese el umbral de aprobacion: "))
promedio = examen1+examen2+examen3/3
if promedio>=6:
    print("está aprobado, felicitaciones!!")
elif promedio<6:
 print("está desaprobado.")
 
print("Fin del programa")