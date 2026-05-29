# Funçoes
def escolha_tipo():
    while True:

        print("Entre com o Tipo de Madeira desejado")
        print("PIN - Tora de Pinho")
        print("PER - Tora de Peroba")
        print("MOG - Tora de Mogno")
        print("IPE - Tora de Ipê")
        print("IMB - Tora de Imbuia")

        tipo = input(">> ")

        match tipo :
            case "PIN":
                return 150.40
            case "PER":
                return 170.20
            case "MOG":
                return 190.90
            case "IPE":
                return 210.10
            case "IMB":
                return 220.70
            case _:
                print("Opção Inválida, tente novamente!")
                print()
                print()
                continue

def qtd_toras():
    while True:
        try:
            qtd = float(input("Entre com a quatidade de toras (m3): "))
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um Número ate 2000m3")
            print()
            continue

        if (qtd > 2000) :
            print("Não aceitamos pedidos com essa quatidade de toras.")
            print("Por favor, entre com a quantidade novamente.")
            print()
            continue
        return qtd

def disc(qtd):

    try:
        if qtd < 100:
            return 1
        elif qtd >= 100 and qtd < 500:
            return 4 / 100
        elif qtd >= 500 and qtd < 1000:
            return 9 / 100
        elif qtd >= 1000 and qtd <= 2000:
            return 16 / 100
    except:
        print("valor inválido para desconto")

def transporte():

    while True:

        print("Escolha o tipo de Transporte: ")
        print("1 - Transporte Rodoviário  - R$ 1000.00")
        print("2 - Transporte Ferroviário - R$ 2000.00")
        print("3 - Transporte Hidroviário - R$ 2500.00")

        try:
            num = int(input(">> "))
        except ValueError:
            print("Valor inválido, por favor, tente novamente!")
            continue
        if num == 1:
            return 1000
        elif num == 2:
            return 2000
        elif num == 3:
            return 2500
        else:
            continue

# Sistema principal (main)

total = 0

print("Bem vindo a Madeireira do Lenhador Tiago Brasil")
print()

try:
    # resultado sera o retorno da funçao
    valor = escolha_tipo()

    # resultado sera o retorno da funçao
    qtd = qtd_toras()

    # Desconto baseado no quantidade de toras
    disconto = disc(qtd)

    # Tansporte baseado na escolha do cliente
    trans = transporte()

    total = ((valor * qtd)*(1 - disconto)) + trans

    # Teste de retornos...
    # print(f"valor da madeira: {valor}, quantidade: {qtd}, Disconto: {disconto}, Transporte: {trans}")
    print(f"Total do pedido: R$ {total:.2f}")

except:
    print("Desculpe... algo errado no sistema.")


