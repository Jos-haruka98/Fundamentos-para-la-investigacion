#Encuesta final de la clase en Python
print("Escirbe tu nombre")
nombre = input()

print("Del 0 al 5 como fue tu entendimiento")
entendimiento= input()

print("Del 0 al 5 como fue tu participacion")
participacion= input()

print("Del 0 al 5 que tan comodo estuviste")
comodiad= input()

print("Que fue lo que mas te gusto")
gusto= input()

print("¿Que se puede mejorar?")
mejoras= input()

print("Comentario adiccional (opcional)")
comentario= input()

print(f"{nombre} entendio del 0 al 5 {entendimiento} y participo {participacion}, se sintio {comodiad} en comodidad y le gusto {gusto} pero piensa que se puede mejorar {mejoras} y comento que {comentario}")