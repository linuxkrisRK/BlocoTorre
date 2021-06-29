"""
Rodando
"""

from apartamento import Apartamento, Torre
from Queue import Queue

# =====================================================================================================================
# Torre
torre1 = Torre()
torre1.cadastrar('Bloco A', 'Rua Andradas, 80')
print(torre1.imprimir())
torre2 = Torre()
torre2.cadastrar('Bloco B', 'Rua Coronel, 65')
print(torre2.imprimir())
# =====================================================================================================================

# =====================================================================================================================
# Apartamento
apartamento1 = Apartamento()
apartamento1.cadastrar(torre1, '12', None)
print(apartamento1.imprimir())
print('\n')

apartamento2 = Apartamento()
apartamento2.cadastrar(torre2, '10', None)
print(apartamento2.imprimir())
print('\n')

apartamento3 = Apartamento()
apartamento3.cadastrar(torre2, '14', apartamento2)
print(apartamento3.imprimir())
print('\n')

apartamento4 = Apartamento()
apartamento4.cadastrar(torre2, '16', apartamento3)
print(apartamento4.imprimir())
print('\n')

apartamento5 = Apartamento()
apartamento5.cadastrar(torre2, '22', apartamento4)
print(apartamento5.imprimir())
print('\n')
# =====================================================================================================================

# =====================================================================================================================
# Fila
# Adicionar as vagas na fila
fila = Queue()
fila.adicionar(apartamento2.imprimir())
fila.adicionar(apartamento3.imprimir())
fila.adicionar(apartamento4.imprimir())
fila.adicionar(apartamento5.imprimir())
print('Fila:')

# Imprimir a fila
print(fila)
print('\n')

# Remover da fila
fila.remover()
print('Fila:')
print(fila)
print('\n')

# Mostrar o primeiro elemento da fila
print(fila.retornar_topo())
print('\n')

# Tamanho da fila
print(len(fila))
# =====================================================================================================================
