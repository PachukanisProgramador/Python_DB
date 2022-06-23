import operacoes
import this

this.opcao = -1

def menu():
    print('Escolha a opção que deseja:\n\n1. Inserir nova pessoa.\n2. Atualizar pessoa existente.\n3. Consultar todas as pessoas.'
                  '\n4. Consultar pessoa.\n5. Excluir pessoa.\n0. Sair.\n')
    this.opcao = int(input())


def escolhas():

    while this.opcao != 0:
        menu()

        if this.opcao == 1:
            print('Informe o nome da pessoa: ')
            nome = input()
            print('Informe o telefone da pessoa: ')
            telefone = input()
            print('Informe o endereço da pessoa: ')
            endereco = input()
            print('Informe a data de nascimento da pessoa: ')
            data_nascimento = input()

            operacoes.inserir(nome, telefone, endereco, data_nascimento)

        elif this.opcao == 2:
            id = input('Digite o id da pessoa que deseja atualizar: ')
            campo  = input('Digite o campo da pessoa que deseja atualizar: ')
            novo_dado = input('Digite o novo dado do campo da pessoa que deseja atualizar: ')
            operacoes.atualizar(id, campo, novo_dado)
        elif this.opcao == 3:
            operacoes.cosultar_tudo()

        elif this.opcao == 4:
            id = input('Digite o código da pessoa que deseja buscar: ')
            operacoes.consultar(id)

        elif this.opcao == 5:
            id = input('Digite o código da pessoa que deseja EXCLUIR: ')
            operacoes.excluir_pessoa(id)

