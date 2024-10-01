costo = float (input("Ingrese el costo de su producto: "));
codigo = str (input("Ingrese su codigo: "));

if codigo == "aco1":
    descuento= 0.10
elif codigo == "aco2":
    descuento= 0.12
else:
    descuento = 0.0

print(f"Con el codigo {codigo} usted adquiere un descuento de {descuento}");
print(f"Pagando en total {costo - descuento}");

input();