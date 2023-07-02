""" Escrever docstrings """


class Endereco:
    """ Escrever docstrings """

    def __init__(self, rua: str = '', numero: int = '', bairro: str = '',
                 municipio: str = '', estado: str = ''):
        self._rua = rua
        self._numero = numero
        self._bairro = bairro
        self._municipio = municipio
        self._estado = estado

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: " \
               f"{', '.join([f'{chave}= {valor}' for chave, valor in self.__dict__.items()])}"

    @property
    def rua(self) -> None:
        """ Escrever docstrings """
        print(f'Rua: {self._rua}.')
        return None

    def get_rua(self) -> str:
        """ Escrever docstrings """
        return self._rua

    def alterar_rua(self, nome: str) -> None:
        """ Escrever docstrings """
        self._rua = nome
        return None

    @property
    def numero_da_casa(self) -> None:
        """ Escrever docstrings """
        print(f'Casa N°: {self._numero}.')
        return None

    def get_numero_da_casa(self) -> int:
        """ Escrever docstrings """
        return self._numero

    def alterar_numero_da_casa(self, numero: int) -> None:
        """ Escrever docstrings """
        self._numero = numero
        return None

    @property
    def bairro(self) -> None:
        """ Escrever docstrings """
        print(f'Bairro: {self._bairro}.')
        return None

    def get_bairro(self) -> str:
        """ Escrever docstrings """
        return self._bairro

    def alterar_bairro(self, nome) -> None:
        """ Escrever docstrings """
        self._bairro = nome
        return None

    @property
    def minicipio(self) -> None:
        """ Escrever docstrings """
        print(f'Município: {self._municipio}.')
        return None

    def get_municipio(self) -> str:
        """ Escrever docstrings """
        return self._municipio

    def alterar_municipio(self, nome) -> None:
        """ Escrever docstrings """
        self._municipio = nome

    @property
    def estado(self) -> None:
        """ Escrever docstrings """
        print(f'Estado: {self._estado}')
        return None

    def get_estado(self) -> str:
        """ Escrever docstrings """
        return self._estado

    def alterar_estado(self, nome) -> None:
        """ Escrever docstrings """
        self._estado = nome
        return None
