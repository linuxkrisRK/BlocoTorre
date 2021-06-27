"""
Classe Torre
"""

class Torre:

    contador = 0

    def __init__(self, nome=None, endereco=None):
        self.__idT = Torre.contador + 1
        self.__nome = nome
        self.__endereco = endereco
        Torre.contador += 1

    @property
    def id_t(self):
        return self.__idT

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    def imprimir(self):
        return f'Id: {self.id_t} || Nome: {self.nome} || Endereco: {self.endereco}'

    def cadastrar(self, x, y):
        self.nome = x
        self.endereco = y