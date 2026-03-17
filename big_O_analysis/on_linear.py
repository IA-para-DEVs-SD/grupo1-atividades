# O(n) - Tempo Linear
# O tempo de execução cresce proporcionalmente ao tamanho da entrada.


def encontrar_maximo(arr):
    maior = arr[0]
    for item in arr:
        if item > maior:
            maior = item
    return maior


def retornar_quadrados(arr):
    lista_quadrados = []
    for num in arr:
        lista_quadrados.append(num * num)
    return lista_quadrados


nums = [2, 16, 7, 9, 8, 23, 12]
print(encontrar_maximo(nums))              # 23
print(retornar_quadrados([2, 4, 6, 8, 10]))  # [4, 16, 36, 64, 100]


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
# encontrar_maximo:   Tempo O(n), Espaço O(1)
# retornar_quadrados: Tempo O(n), Espaço O(n) — cria uma nova lista de tamanho n
