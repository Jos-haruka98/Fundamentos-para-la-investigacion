Valor_BTC = 1239785.74

print("Igrese el monto en bitcoin: ")
monto_BTC = float(input())

conversion = monto_BTC * Valor_BTC
print(f"el valor de {monto_BTC} BTC en pesos mexicanos {conversion:.2f} $ MXN")