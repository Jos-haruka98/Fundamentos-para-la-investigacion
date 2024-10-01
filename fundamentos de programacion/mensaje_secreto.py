# Un mensaje secrto protegido por contraseña

password = "Jos_Haruka98"
mensaje= "Mi frase para no rendirme es ''Plus Ultra!!!!!''"

password_in = input("ingrese la contraseña para ver el mensaje: ")

if password_in == password:
    print("El mensaje secreto es: ")
    print(mensaje)
else:
    print("contraseña equivocada")
