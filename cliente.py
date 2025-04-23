class Cliente:
    def __init__(self, n, fone):
        self._nome = n
        self._telefone = fone
    #utilizando o metodo get para retornar o nome do cliente na chamada da funcao do main.py
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome