

binario = input("Ingrese el binario a encontrar en decimal: ")

for numero in range(0,1000000000001):
    binario_contador = bin(numero)[2:]
    if binario_contador == binario:
        print(f"El numero {binario} es {numero} en decimal")