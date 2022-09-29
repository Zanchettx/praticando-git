assinatura = input("Insira a assinatura do cliente : ")
faturamento = int(input("Insira o faturamento anual do seu canal: R$"))
assinatura = assinatura.upper()
#Teste lógico
if assinatura == "BASIC":
    bonus = 30/100*(faturamento)
    print("Valor do pagamento do cliente: {}".format(bonus))

elif assinatura == "SILVER":
    bonus = (faturamento) * 0.2
    print("Valor do pagamento do cliente: {}".format(bonus))

elif assinatura == "GOLD":
    bonus = 10%(faturamento)
    print("Valor do pagamento do cliente: {}".format(bonus))

elif assinatura == "PLATINUM":
    bonus = 5%(faturamento)
    print("Valor do pagamento do cliente: {}".format(bonus))

else:
    print("Insira uma assinatura válida (basic - silver - gold - platinum)")
#elif assinatura != "BASIC" != "SILVER" != "GOLD" != "PLATINUM":
 #   print("Insira uma assinatura válida (basic - silver - gold - platinum)")