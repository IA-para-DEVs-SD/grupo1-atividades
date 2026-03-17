# Espaço O(n²) — Fatiamento Recursivo
# Este exemplo tem tempo O(n) mas espaço O(n²) devido ao fatiamento de lista na recursão.


def soma_recursiva(dados):
    if dados == []:
        return 0
    primeiro = dados[0]
    return primeiro + soma_recursiva(dados[1:])


print(soma_recursiva([5, 4, 3, 2, 1, 0]))  # 15


#
#
#
#
#
#
#
#
#
#
#
#
# Tempo: O(n) — uma chamada recursiva por elemento.
# Espaço: O(n²) — cada chamada cria um fatia da lista (O(n) cada),
#          e há n chamadas, logo O(n * n) = O(n²) de espaço total.
#
# Fatias na pilha de chamadas:
#   [5, 4, 3, 2, 1, 0]
#   [4, 3, 2, 1, 0]
#   [3, 2, 1, 0]
#   [2, 1, 0]
#   [1, 0]
#   [0]
#   []
