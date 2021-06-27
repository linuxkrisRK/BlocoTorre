"""
Classe Nó(Node)
- Estrutura de dado básica para interligar elementos que estão em espaço não contigo de memoria
- O Nó(node) vai ter dentro de si o dado a ser guardado e uma referência para o próximo Nó
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
