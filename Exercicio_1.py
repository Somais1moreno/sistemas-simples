print("Bem vindo ao Sistema do Tiago Brasil")

#recebendo valores
valor_b = float(input("Informe o valor Base do plano: R$"))
idade = int(input("Informe a idade do cliente: "))
valor_m = 0

#validações
if (idade >= 0 and idade < 19):
    valor_m = valor_b * (100/100)
    print(f"O valor mensal do plano é de: R${valor_m:.2f}")
elif (idade >= 19 and idade < 29):
    valor_m = valor_b * (150/100)
    print(f"O valor mensal do plano é de: R${valor_m:.2f}")
elif (idade >= 29 and idade < 39):
    valor_m = valor_b * (225/100)
    print(f"O valor mensal do plano é de: R${valor_m:.2f}")
elif (idade >= 39 and idade < 49):
    valor_m = valor_b * (240/100)
    print(f"O valor mensal do plano é de: R${valor_m:.2f}")
elif (idade >= 49 and idade < 59):
    valor_m = valor_b * (350/100)
    print(f"O valor mensal do plano é de: R${valor_m:.2f}")
elif (idade >= 59):
    valor_m = valor_b * (600/100)
    print(f"O valor mensal do plano é de: R${valor_m:.2f}")
else:
    print("Você não digitou algo válido!")