
#¿Estas soletro?
persona_1 = True #Declaro variable booleana con un 1
persona_2 = False #Está casado
persona_3= False #Está casada
persona_4= True #Está soltera

#1 and 1 - 1           0 and 1 - 1       1 and 0 - 0     0 and 0 - 0
print("Persona 1 hace match con Persona 2: " + str(persona_1 and persona_2)) # 0 False
print("Persona 1 hace match con Persona 3: " + str(persona_1 and persona_3)) # 0 False
print("Persona 1 hace match con Persona 4: " + str(persona_1 and persona_4)) # 1 True



input()