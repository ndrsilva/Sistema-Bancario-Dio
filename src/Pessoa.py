from src.Endereco import Endereco

class Pessoa:

    def __init__(self, nome: str, sobrenome: str, data_nascimento: str, rg: str, cpf: str, endereco: Endereco) -> None:
        self._nome = nome
        self._sobrenome = sobrenome
        self._data_nascimento =  data_nascimento
        self._rg = rg
        self._cpf = cpf
        self.endereco = endereco

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: "\
            f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    @property
    def nome(self) -> None:
        print(f'Nome: {self._nome}')
        return None
    
    def get_nome(self) -> str:
        return self._nome
    
    def alterar_nome(self, nome) -> None:
        if isinstance(nome, str):
            self._nome = nome
            return None

        else:
            print('Favor digitar um nome válido.')
            return None

    @property
    def sobrenome(self) -> None:
        print(f'Sobrenome: {self._sobrenome}')
        return None
    
    def get_sobrenome(self) -> str:
        return self._sobrenome
    
    def alterar_sobrenome(self, sobrenome) -> None:
        if isinstance(sobrenome, str):
            self._sobrenome = sobrenome
            return None
        
        else:
            print('Favor digitar um nome válido.')
            return None

    @property
    def data_nascimento(self) -> None:
        print(f'Data Nasc.: {self._data_nascimento}')
        return None
    
    def get_data_nascimento(self) -> str:
        return self._data_nascimento
    
    def alterar_data_nascimento(self, data_nascimento) -> None:
        self._data_nascimento = data_nascimento

        return None

    @property
    def rg(self) -> None:
        print(f'RG: {self._rg}')
        return None
    
    def get_rg(self) -> str:
        return self._rg
    
    def alterar_rg(self, rg) -> None:
        if len(rg) == 7:
            self._rg = rg

            print('RG alterado com sucesso.')
            return None
        
        else:
            print('Favor digitar um RG válido.')
            return None

    @property
    def cpf(self) -> None:
        print(f'CPF: {self._cpf}')
        return None
    
    def get_cpf(self) -> str:
        return self._cpf
    
    def alterar_cpf(self, cpf: str) -> None:
        if len(cpf) == 11:
            self._cpf = cpf

            print('CPF alterado com sucesso.')
            return None
        
        else:
            print('Favor digitar um CPF válido.')
            return None
