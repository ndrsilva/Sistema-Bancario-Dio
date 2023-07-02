""" Escrever docstrings """
from src.Endereco import Endereco
from src.Pessoa import Pessoa
from src.Conta import Conta
import textwrap


def menu():
    """ Escrever docstrings """
    opcao_menu = """
    [1] - \tDepositar
    [2] - \tSacar
    [3] - \tExtrato
    [4] - \tNova conta
    [5] - \tListar contas
    [6] - \tNovo cliente
    [7] - \tSair
    """
    print(textwrap.dedent(opcao_menu))

    return input()


if __name__ == '__main__':
    conta = Conta()

    while True:
        opcao = menu()

        if opcao == '1':
            valor = float(input('Informe o valor do depósito:\nR$ '))
            conta.depositar(valor)

        elif opcao == '2':
            valor = float(input('Informe o valor do saque:\nR$ '))
            conta.saque(valor)

        elif opcao == '3':
            nome = input('Nome: ')
            sobrenome = input('Sobrenome: ')
            data_nasc = input('Data Nasc. (dd/mm/aaaa): ')
            rg = input('RG: ')
            cpf = input('CPF: ')

            rua = input('Rua: ')
            numero = int(input('N° da casa: '))
            bairro = input('Bairro: ')
            municipio = input('Município: ')
            estado = input('Estado: ')

            endereco = Endereco(rua, numero, bairro, municipio, estado)
            cliente = Pessoa(nome, sobrenome, data_nasc, rg, cpf, endereco)
