#Esto es un experimento para mi aprendizaje
#Primero tenemos que declarar variables
bulbasaur="Bienvenido programador esta es una calculadora para experimetar visual estudio"
squiretl=("""Menu\n
          1.-Suma
          2.-Resta
          3.-Multiplicacion
          4.-Division
          5.-Sorpresa""")

pikachu=("Seleccione la opcion que quiera realizar")
Charizard=("Este curso esta siendo muy bueno y divertido")
#Despues imprimir el texto y crear variable Ele para que el ususario seleccione las opciones de la calculadora
print(bulbasaur,squiretl);
print(pikachu)
Ele=int(input("> "));
#Crear el if y continuar con los elif del que pasaria si elije tal numero
if (Ele==1):
    bulbasur=float(input("Ingrese el primer numero: "));
    charemeleon=float(input("ingrese el segundo numero: "));
    suma=(bulbasur+charemeleon);
    print("es igual a: ",suma);
elif(Ele==2):
	bulbasur=float(input("Ingrese el primer numero: "));
	warttoltel=float(input("ingrese el segundo numero: "));
	resta=bulbasur-warttoltel;
	print("es igual a: ",resta);
elif(Ele==3):
	bulbasur=float(input("Ingrese el primer numero: "));
	warttoltel=float(input("ingrese el segundo numero: "));
	multi=bulbasur*warttoltel;
	print("es igual a: ",multi);
elif(Ele==4):
	bulbasur=float(input("Ingrese el primer numero: "));
	warttoltel=float(input("ingrese el segundo numero: "));
	divi=bulbasur/warttoltel;
	print("es igual a: ",divi);
elif(Ele==5):
	print(Charizard);

input();