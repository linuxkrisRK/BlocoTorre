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
print('\n')
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

# =======================================================================
# Atualizando os próximos apartamento na fila
apartamento2.atualizar_proximo(apartamento3)
apartamento3.atualizar_proximo(apartamento4)
apartamento4.atualizar_proximo(apartamento5)
apartamento5.atualizar_proximo(apartamento5)

# =====================================================================================================================

# =====================================================================================================================
# Fila
# Adicionar as vagas na fila
fila = Queue()
fila.adicionar(apartamento2.fila())
fila.adicionar(apartamento3.fila())
fila.adicionar(apartamento4.fila())
fila.adicionar(apartamento5.fila())
print('Fila:')

# Imprimir a fila
print(fila)
print('\n')

# Remover da fila
print('Apartamento abaixo removido da lista!')
print(fila.remover())
print('\n')
print('Fila:')
print(fila)
print('\n')

# Mostrar o primeiro elemento da fila
print(fila.retornar_topo())
print('\n')

# Tamanho da fila
print(f'Existem {len(fila)} apartamentos na fila')
# =====================================================================================================================
