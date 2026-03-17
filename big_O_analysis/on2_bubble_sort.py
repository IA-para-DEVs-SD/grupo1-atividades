# O(n²) - Bubble Sort (Ordenação por Bolha)
# Compara elementos adjacentes e os troca até o array estar ordenado.
# Pior caso: cada elemento precisa ser comparado com todos os outros.


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)  # [11, 12, 22, 25, 34, 64, 90]


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
# Tempo: O(n²) — dois laços aninhados, cada um com até n iterações.
# Espaço: O(1) — ordenado no próprio array.
