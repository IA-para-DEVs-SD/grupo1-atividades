# O(n) - Soma de Prefixo (duas abordagens)
# Entrada:  [10, 20, 10, 5, 15]
# Saída:    [10, 30, 40, 45, 60]  (saida[i] = soma de entrada[0..i])


def soma_prefixo_novo_array(arr):
    """Cria um novo array de saída — Espaço O(n)."""
    saida = [arr[0]]
    for i in range(1, len(arr)):
        saida.append(saida[i-1] + arr[i])
    return saida


def soma_prefixo_in_place(arr):
    """Modifica o array original — Espaço extra O(1)."""
    for i in range(1, len(arr)):
        arr[i] = arr[i-1] + arr[i]
    return arr


print(soma_prefixo_novo_array([10, 20, 10, 5, 15]))  # [10, 30, 40, 45, 60]
print(soma_prefixo_in_place([10, 20, 10, 5, 15]))    # [10, 30, 40, 45, 60]


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
# soma_prefixo_novo_array: Tempo O(n), Espaço O(n)
# soma_prefixo_in_place:   Tempo O(n), Espaço O(1)
