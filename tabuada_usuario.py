#Agora altere o código para solicitar a tabuada 
#ao usuário
print("Bienvenidos a la tabla de multiplicar del número!")
print ("¿Qué mesa quieres?")
multiplicador = int(input("introduce el multiplicador:"))
contador = 0
while (contador <=10):
    print(f" {multiplicador} x {contador} = {contador * multiplicador}")  
    contador +=1
print ("Gracias por aprender las tablas de multiplicar con nosotros.")
