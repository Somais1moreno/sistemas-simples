def valida_opc (pergunta, min, max):
    while True:
        try:
            opc = int(input(pergunta))
        except ValueError:
            print(f"valor inválido, tente novamente ({min}a{max})")
            continue
        else:
            while opc < min or opc > max:
                opc = int(input(pergunta))
        return opc

def cadastrar_contato(id,tam_l):
    dic_local = {}

    print("-" * 50)
    print("-" * 12, " MENU CADASTRAR CONTATO ", "-" * 12)
    print(f"ID do Contato: {id}")
    nome = input("Por favor entre com o Nome do Contato: ")
    atividade = input("Por favor entre com a Atividade do Contato: ")
    telefone = input("Por favor entre com o Telefone do Contato: ")

    # insiro todas as variaveis em um dicionario
    dic_local = {'id': id,
                 'nome': nome,
                 'atividade': atividade,
                 'telefone': telefone}

    return dic_local

def consultar_contatos():

    while True:
        print()
        print("-" * 50)
        print("-" * 12, " MENU  CONSUTAR CONTATOS ", "-" * 12)

        print("Escolha a opção desejada:")
        print("1 - Consultar todos os Contato")
        print("2 - Consultar Contato por ID")
        print("3 - Consultar Contato por Atividade")
        print("4 - Retornar")

        escolha_consulta = valida_opc(">>", 1,4)

        resultado = []
        if escolha_consulta == 1:
            print("-" * 30)
            print()
            for contato in lista_contatos:
                print("-" * 20)
                print(f"ID: {contato['id']}")
                print(f"Nome: {contato['nome']}")
                print(f"Atividade: {contato['atividade']}")
                print(f"Telefone: {contato['telefone']}")
            continue
        elif escolha_consulta == 2:
            print("-" * 30)
            print()
            opc_id = valida_opc("Digite o ID do Contato: ", 1, 9999999)
            for contato in lista_contatos:
                if contato['id'] == opc_id:
                    resultado.append(contato)
                    print(resultado)
            if resultado:
                for item in resultado:
                    print("-" * 20)
                    print(f"ID: {item['id']}")
                    print(f"Nome: {item['nome']}")
                    print(f"Atividade: {item['atividade']}")
                    print(f"Telefone: {item['telefone']}")

            continue
        elif escolha_consulta == 3:
            print("-" * 30)
            print()
            opc_ativ = input("Digite a Atividade do(S) Contato(S): ")
            for contato in lista_contatos:
                if contato['atividade'] == opc_ativ:
                    resultado.append(contato)
            if resultado:
                for contato in resultado:
                    print("-"*20)
                    print(f"ID: {contato['id']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}")
                continue
        elif escolha_consulta == 4:
            return

def remover_contato():

    while True:
        print()
        print("-" * 50)
        print("-" * 12, " MENU  REMOVER CONTATOS ", "-" * 12)

        escolha_remover = valida_opc("Digite o ID do contato a ser removido: ", 1, 9999999)


        for contato in lista_contatos:
            if contato["id"] == escolha_remover:
                lista_contatos.remove(contato)
                print("Contato Removido com Sucesso!")
                return True
        print("ID inválido, tente novamente...")
        continue

# PROGRAMA MAIN

lista_contatos = []
tam_lista = len(lista_contatos)
id_global = 5478025

while True:

    print()
    print("  Bem vindo a Lista de Contatos do Tiago Brasil")
    print("-" * 50)
    print("-" * 16, " MENU PRINCIPAL ", "-" * 16)

    print("Escolha a opção desejada:")
    print("1 - Cadastrar Contato")
    print("2 - Consultar Contato")
    print("3 - Remover Contato")
    print("4 - Sair")

    escolha_menu = valida_opc(">>", 1, 4)

    if escolha_menu == 1:
        print()
        try:
           contato = cadastrar_contato(id_global, tam_lista)
           lista_contatos.append(contato)
           id_global += 1
        except:
            print("Algo errado no sistema, por favor tente novamente!")
            continue
    elif escolha_menu == 2:
        print()
        try:
            consultar_contatos()
        except:
            print("Algo errado no sistema, por favor tente novamente!")
            continue
    elif escolha_menu == 3:
        print()
        try:
            remover_contato()
        except:
            print("Algo errado no sistema, por favor tente novamente!")
            continue
    else:
        print("Obrigado por usar o Sistema do Tiago Brasil!")
        break