from src.Pessoa import Pessoa
from src.Conta import Conta


p1 = Pessoa(
    nome='André',
    sobrenome='Silva',
    data_nascimento='12-12-1989',
    rg='3154875',
    cpf='45874589652'
    )

c1 = Conta('4232', p1, 3500.00, 10000)

c1.depositar(200)
c1.saque(200)
c1.saque(159.50)
c1.extrado()
c1.historico.imprime()
c1.saque(100)
c1.extrado()
c1.historico.imprime()



