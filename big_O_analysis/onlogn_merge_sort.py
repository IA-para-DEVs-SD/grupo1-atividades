# O(n log n) - Tempo Linearítmico
# Merge Sort: divide o array recursivamente ao meio (log n níveis),
# depois mescla cada nível em O(n) — total O(n log n).


def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        metade_esq = lista[:meio]
        metade_dir = lista[meio:]
        merge_sort(metade_esq)
        merge_sort(metade_dir)
        i = j = k = 0
        while i < len(metade_esq) and j < len(metade_dir):
            if metade_esq[i] < metade_dir[j]:
                lista[k] = metade_esq[i]
                i += 1
            else:
                lista[k] = metade_dir[j]
                j += 1
            k += 1
        while i < len(metade_esq):
            lista[k] = metade_esq[i]
            i += 1
            k += 1
        while j < len(metade_dir):
            lista[k] = metade_dir[j]
            j += 1
            k += 1


arr = [11, 22, 55, 44, 77, 66, 44, 33, 88]
merge_sort(arr)
print(arr)  # [11, 22, 33, 44, 44, 55, 66, 77, 88]


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
# Tempo: O(n log n) — log n níveis de recursão, cada um fazendo O(n) de trabalho.
# Espaço: O(n) — arrays auxiliares criados durante a divisão.
