""" Escrever docstrings """
from datetime import datetime


class Historico:
    """ Escrever docstrings """

    def __init__(self):
        self.data_abertura = datetime.today()
        self.transacoes = []

    def imprime(self):
        """ Escrever docstrings """
        print(f'Data de abertura: {self.data_abertura}')
        print('Transações: ')

        for transacao in self.transacoes:
            print(f'- {transacao}')

        print()
