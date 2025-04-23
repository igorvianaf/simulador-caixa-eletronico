from cliente import Cliente
from conta import Conta

print('Para processar seu saque precisamos de algumas informações')
nome = input('Informe o nome do cliente: ')
n_conta =  input('Informe sua conta: ')
valor_saque = int(input('Informe o valor do saque: '))

#instanciando a classe cliente e atribuindo valores
c1 = Cliente(nome, n_conta)

#instanciando a classe Conta e atribuindo valores
conta = Conta(c1.get_nome(), 1233211)

#utilizando os metodos da classe conta
#em conta deposito foi atribuido o valor da conta do cliente
conta.deposito(1500)
conta.saque(valor_saque)
conta.extrato()