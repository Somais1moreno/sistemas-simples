print("-"*10 + " Bem-vindo a Pizzaria do Tiago Brasil " + "-"*10)
print("-"*25 + "Cardápio" + "-"*25)
print("-"*58)
print("---| Tamanho  | Pizza Salgada(PS)  |  Pizza Doce(PD)  |---")
print("---|    P     |     R$ 30.00       |     R$ 34.00     |---")
print("---|    M     |     R$ 45.00       |     R$ 48.00     |---")
print("---|    P     |     R$ 60.00       |     R$ 66.00     |---")
print("-"*58)

#variaveis preço sabores
valore_s_pmg = [30,45,60]
valores_d_pmg = [34,48,66]
#somatorio total
total = 0

#loop pedido, enquanto quiser algo
sair = False

while (not sair):

    sabor = input("Entre com o sabor desejado (PS/PD): ")
    print()

    while (sabor.casefold() != "ps" and sabor.casefold() != "pd"):
        print("Sabor Inválido. Tente novamente")
        print()
        sabor = input("Entre com o sabor desejado (PS/PD): ")


    tamanho = input("Entre com o tamanho desejado (P/M/G): ")

    while (tamanho.casefold() != "p" and tamanho.casefold() != "m" and tamanho.casefold() != "g"):

        print("Tamanho Inválido. Tente novamente")
        print()
        tamanho = input("Entre com o tamanho desejado (P/M/G): ")

    if (sabor.casefold() == "ps" and tamanho.casefold() == "p"):
        print(f"Você pediu uma Pizza Salgada no tamanho {tamanho}: R${valore_s_pmg[0]}")
        total += valore_s_pmg[0]
    elif (sabor.casefold() == "ps" and tamanho.casefold() == "m"):
        print(f"Você pediu uma Pizza Salgada no tamanho {tamanho}: R${valore_s_pmg[1]}")
        total += valore_s_pmg[1]
    elif (sabor.casefold() == "ps" and tamanho.casefold() == "g"):
        print(f"Você pediu uma Pizza Salgada no tamanho {tamanho}: R${valore_s_pmg[2]}")
        total += valore_s_pmg[2]
    elif (sabor.casefold() == "pd" and tamanho.casefold() == "p"):
        print(f"Você pediu uma Pizza Doce no tamanho {tamanho}: R${valores_d_pmg[0]}")
        total += valores_d_pmg[0]
    elif (sabor.casefold() == "pd" and tamanho.casefold() == "m"):
        print(f"Você pediu uma Pizza Doce no tamanho {tamanho}: R${valores_d_pmg[1]}")
        total += valores_d_pmg[1]
    elif (sabor.casefold() == "pd" and tamanho.casefold() == "g"):
        print(f"Você pediu uma Pizza Doce no tamanho {tamanho}: R${valores_d_pmg[2]}")
        total += valores_d_pmg[2]

    print()
    continuar = input("Deseja mais alguma coisa? (S/N): ")

    if (continuar.casefold() == "n"):
        sair = True

        print(f"O valor total a ser pago: R${total:.2f}")
    elif (continuar.casefold() == "s"):
        continue