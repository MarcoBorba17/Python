Nota = int(input("Insira sua nota"))
if Nota < 60:
    print ("F")
elif Nota >= 60 and Nota < 69:
    print ("D")
elif Nota > 70 and Nota < 79:
    print("C")
elif Nota > 89 and Nota < 80:
    print ("B")
elif Nota >=90 and Nota == 100:
    print ("A")
else:
    print ("Nota Inválida")