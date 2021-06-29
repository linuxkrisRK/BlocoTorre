"""
Classe Queue
O primeiro elemento a ser inserido deve ser o primeiro a ser removido!
"""
from Node import Node

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    # Inserir elementos na fila
    def adicionar(self, elem):
        node = Node(elem)
        # Verificar se já tem um ultimo elemento na fila
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        # Verificar se o primeiro elemento é vazio
        if self.first is None:
            self.first = node
        # Aumenta tamanho da fila
        self._size = self._size + 1

    # remover elementos da fila
    def remover(self):
        # Verificar se existe elementos na fila
        # len(self)
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self._size = self._size - 1
            # Retornar elemento removido
            return elem
        raise IndexError("A queue está vazia(sem elementos)")

    # Retornar primeiro(topo) elemento da fila
    def retornar_topo(self):
        if self._size > 0:
            elem = self.first.data
            return elem
        raise IndexError("A queue está vazia(sem elementos)")

    # Retornar tamanho da lista
    def __len__(self):
        return self._size

    # Exibir a fila, desde o primeiro até o último. (IMPRIMIR)
    def __repr__(self):
        if self._size > 0:
            fila = ""
            pointer = self.first
            while(pointer):
                fila = fila + str(pointer.data) + " \n " + '\n'
                pointer = pointer.next
            return fila
        return "Fila vazia!"

    def __str__(self):
        return self.__repr__()
