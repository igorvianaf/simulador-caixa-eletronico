class Conta:
    def __init__(self, titular, numero, saldo=0):
        self.numero = numero
        self._titular = titular
        self._saldo = saldo

    #Criado para acessar o valor do (atributo privado) saldo
    @property
    def saldo(self):
        return self._saldo

    #criar condição para (atributo privado) o saldo do cliente não ser negativo
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print('O saldo não pode ser negativo')
        else:
            self._saldo = saldo
    #acessando o saldo do cliente (atributo privado) atraves do metodo get
    def get_saldo(self):
        return self._saldo

# estabelecendo metódo para saque
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print('Saque realizado com sucesso')
        else:
            print('Saldo insuficiente')

# estabelecendo metódo para depósito
    def deposito(self, valor):
        self.saldo += valor

# estabelecendo metódo para extrato
    def extrato(self):
        print('Cliente:', self._titular, "Saldo Atual:", self._saldo, 'Número da conta:', self.numero)
