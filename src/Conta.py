""" Escrever docstrings """
from src.Pessoa import Pessoa
from src.Historico import Historico


class Conta:
    """ Escrever docstrings """

    def __init__(self, numero: str = 0, titular: Pessoa = '',
                 saldo: float = 0, limite_saldo: float = 0):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo
        self._limite_saldo = limite_saldo
        self.historico = Historico()

        self._LIMITE_SAQUE_DIARIO = 3
        self._LIMITE_MAXIMO_POR_SAQUE = 500.00

    def __str__(self):
        return f"{self.__class__.__name__}: " \
               f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def dados_titular(self) -> None:
        """ Escrever docstrings """
        print('# DADOS GERAL DO TITULAR')
        self.titular.nome
        self.titular.sobrenome
        self.titular.cpf
        self.titular.rg
        self.titular.data_nascimento
        print()
        return None

    def endereco_geral(self) -> None:
        """ Escrever docstrings """
        print('# ENDEREÇO GERAL DO TITULAR')
        self.titular.endereco.numero_da_casa
        self.titular.endereco.rua
        self.titular.endereco.bairro
        self.titular.endereco.minicipio
        self.titular.endereco.estado
        print()
        return None

    @property
    def saldo(self) -> None:
        """ Escrever docstrings """
        print(f'R$ {self._saldo:.2f}')
        return None

    def depositar(self, valor: float) -> None:
        """ Escrever docstrings """
        if valor > 0:
            valor = float(valor)
            self._saldo += valor

            self.historico.transacoes.append(f'Depósito de R$ {valor:.2f}')
            print(f'Depósito de R$ {valor:.2f} realizdo com sucesso.\n')
            return None

        print('O depósito não pode ser igual ou menor que zero.\n'
              'Favor informar um valor válido.\n')
        return None

    def saque(self, valor: float) -> None:
        """ Escrever docstrings """
        if valor > 0:
            if not self._vefiricar_limite_do_saque(valor):
                if self._verificar_quantidade_saque_diario():
                    if valor <= self._saldo:
                        valor = float(valor)
                        self._saldo -= valor

                        self.historico.transacoes.append(f'Saque de R$ {valor:.2f}')
                        self._LIMITE_SAQUE_DIARIO -= 1

                        print(f'Saque de R$ {valor:.2f} realizado com sucesso.')

                        if self._verificar_quantidade_saque_diario():
                            print(f'Você ainda poder realizar {self._LIMITE_SAQUE_DIARIO} saque, '
                                  f'no valor máximo de R$ {self._LIMITE_MAXIMO_POR_SAQUE:.2f} cada.\n')
                        else:
                            print('O seu limite para saque acabou.\n')
                        return None

                    else:
                        print('Não a saldo suficiente para realizar o saque.\n'
                              'Favor retirar o extrato para ver o saldo em caixa')
                        return None

                else:
                    print('O seu limite de saque diário acabou.\n'
                          'Volte amanhã.\n')
                    return None

            else:
                print('O seu limite máximo é de R$ 500,00 por saque.\n'
                      'E apenas 3 saques por dia, favor informar um valor menor.\n')
                return None

        print('O valor do saque não pode ser igaul ou menor que zero.\n'
              'Favor informar um valor válido.\n')
        return None

    def _vefiricar_limite_do_saque(self, valor):
        """ Escrever docstrings """
        if valor > self._LIMITE_MAXIMO_POR_SAQUE:
            return True

        return False

    def _verificar_quantidade_saque_diario(self):
        """ Escrever docstrings """
        if self._LIMITE_SAQUE_DIARIO > 0:
            return True

        return False

    def extrado(self):
        """ Escrever docstrings """
        print('Extrato do dia.')
        for transacao in self.historico.transacoes:
            print(f'- {transacao}')
        print(f'# Saldo atual: {self._saldo:.2f}')

        print()
        self.historico.transacoes \
            .append(f'Tirou extrato do saldo - Saldo atual de R$ {self._saldo:.2f}')
