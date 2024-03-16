print("Bem vindo ao STORE Plus")

valordacompra = float(input("Informe o valor da Compra"))
formadepagamento = int(input("Informe a forma de Pagamento"))
parcela = float(input ("Informe a quantidade de Parcelas"))


if formadepagamento == 0:
    print ("à vista")
    if valordacompra <=500:
        resultado = valordacompra *0.90
    elif valordacompra >500:
        resultado = valordacompra *0.85
    elif valordacompra >1000:
        resultado = valordacompra *0.80
    print ("O seu valor final é:", resultado)

elif formadepagamento == 1:
    print ("à prazo")
    if valordacompra <=800 and parcela >5:
        resultado = float(valordacompra / parcela) 
        print ("Quantidade de Parcelas Inválidas")
    elif valordacompra >800 and parcela <=10:
        resultado = float (valordacompra /parcela)
    elif valordacompra >800 and parcela == 11:
        resultado = valordacompra *1.55
    elif valordacompra >800 and parcela == 12:
        resultado = valordacompra *1.78
    elif valordacompra >800 and parcela == 13:
        resultado = valordacompra *1.91
    elif valordacompra >800 and parcela == 14:
        resultado = valordacompra *2.26
    elif valordacompra >800 and parcela == 15:
        resultado = valordacompra *2.425
    elif valordacompra >800 and parcela == 16:
        resultado = valordacompra *2.60
    elif valordacompra >800 and parcela == 17:
        resultado = valordacompra *2.92
    elif valordacompra >800 and parcela == 18:
        resultado = valordacompra *3.16
    print ("O seu valor final é:", resultado)







