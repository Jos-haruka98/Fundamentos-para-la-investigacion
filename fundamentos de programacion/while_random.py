import random

numero_secreto = random.randint(1,10)

adivinanza = int(input("Adivina el numero secreto entre 0 1 a 10"))

while adivinanza !=numero_secreto:
    adivinanza = int(input("Vuelve a intentar:"))

print("Felicidades has encontrado del numero secreto")