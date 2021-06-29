"""
Classe Apartamento

Observação:
- O id será auto incrementado como um serial;
- E o número do Apartamento também, mas com um valor pré definido.
"""
from Torre import Torre

class Apartamento(Torre):

    contador = 0
    numeroProg = 100

    def __init__(self, nome=None, endereco=None, vaga=None, torre=None, apartamento=None):
        super().__init__(nome, endereco)
        self.__id = Apartamento.contador + 1
        self.__numero = Apartamento.numeroProg + 1
        self.__torre = torre
        self.__vaga = vaga
        self.__proximo = apartamento
        Apartamento.contador += 1
        Apartamento.numeroProg += 1

    @property
    def id(self):
        return self.__id

    @property
    def numero(self):
        return self.__numero

    @property
    def torre(self):
        return self.__torre

    @property
    def vaga(self):
        return self.__vaga

    @property
    def proximo(self):
        return self.__proximo

    @vaga.setter
    def vaga(self, nova_vaga):
        self.__vaga = nova_vaga

    @proximo.setter
    def proximo(self, novo_proximo):
        self.__proximo = novo_proximo

    @torre.setter
    def torre(self, torre_nome):
        self.__torre = torre_nome

    def imprimir(self):
        return f'TORRE: {self.torre.imprimir()} \n' \
                f'APARTAMENTO Id: {self.id} || Numero: {self.numero} ||  Vaga: {self.vaga}'

    def cadastrar(self, torre, vaga):
        self.vaga = vaga
        self.torre = torre

    def atualizar_proximo(self, k):
        self.proximo = k

    def imprimir_apartamento(self):
        return f' Número: {self.numero}'

    def fila(self):
        if self.proximo is None:
            k = self.proximo = 'Nenhum ainda!'
            return f'Torre: {self.torre.nome} \n' \
                   f'Apartamento {self.numero}\n' \
                   f'Próximo Apartamento {k}'
        k = self.proximo.imprimir_apartamento()
        return f'Torre: {self.torre.nome} \n' \
               f'Apartamento {self.numero}\n' \
               f'Próximo Apartamento {k}'
