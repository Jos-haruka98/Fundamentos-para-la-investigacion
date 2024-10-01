def promedio_cuatro():

    #Promedio de 4 calificaciones
    nota_s1 = float(input("Ingresa la nota de la semana 1: "))
    nota_s2 = float(input("Ingresa la nota de la semana 2: "))
    nota_s3 = float(input("Ingresa la nota de la semana 3: "))
    nota_s4 = float(input("Ingresa la nota de la semana 4: "))

    promedio = ((nota_s1 + nota_s2 + nota_s3 + nota_s4) / 4)

    print(f"El promedio de los valores dados es: {promedio:.0f}")

    if promedio >= 6:
        print(f"Felicidades pasaste con {promedio:.0f}")
    else:
        print(f"Lo siento usted no aprobo {promedio:.0f}")

        