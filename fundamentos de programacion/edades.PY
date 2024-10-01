# 0 a 5 bebé
#6 a 13 niño
#14 a 17 adolecente
#18 a 65 Aldulto
#65 a 125 Adulto Mayor
#otros casos no admisible

edad = (input("ingrese su edad: "))

if edad>0 and edad<=5:
    print("Usted es un bebé")
elif edad>5 and edad<=13:
    print("Usted es un niño")
elif edad>13 and edad<=17:
    print("Usted es un adolecente")
elif edad>17 and edad<=65:
    print("Usted es un adulto")
elif edad>65 and edad<=125:
    print("Usted es un adulto mayor")
else:
    print("Edad invalida")

input()