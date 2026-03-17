# O(log n) - Busca Binária
# Um algoritmo logarítmico divide o espaço de busca pela metade a cada iteração.


def busca_binaria(arr, alvo):
    indice_min = 0
    indice_max = len(arr) - 1
    while indice_min <= indice_max:
        indice_atual = (indice_min + indice_max) // 2
        valor_atual = arr[indice_atual]
        if valor_atual == alvo:
            return indice_atual
        elif valor_atual < alvo:
            indice_min = indice_atual + 1
        else:
            indice_max = indice_atual - 1
    return -1


numeros = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]
print(busca_binaria(numeros, 23))   # 6
print(busca_binaria(numeros, 100))  # -1


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
# Tempo: O(log n) — o espaço de busca é dividido pela metade a cada iteração.
# Espaço: O(1)
