# O(n) - Verificação de Duplicatas com Conjunto (Set)
# Percorre a lista uma vez, usando um conjunto para rastrear os vistos.


def tem_duplicata(nums):
    vistos = set()
    for num in nums:
        if num in vistos:
            return True
        vistos.add(num)
    return False


def encontrar_duplicatas(numeros):
    vistos = set()
    duplicatas = set()
    for n in numeros:
        if n in vistos:
            duplicatas.add(n)
        vistos.add(n)
    return duplicatas


print(tem_duplicata([1, 2, 3, 4, 5]))         # False
print(tem_duplicata([1, 2, 3, 2, 5]))         # True

print(encontrar_duplicatas([1, 2, 3, 2, 5]))  # {2}
print(encontrar_duplicatas([1, 1, 2, 3, 3]))  # {1, 3}
print(encontrar_duplicatas([1, 2, 3]))        # set()


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
# Tempo: O(n) — percorre a lista uma única vez.
# Espaço: O(n) — no pior caso, todos os elementos são adicionados ao conjunto.
#
# Alternativa ingênua com laços aninhados seria O(n²) tempo, O(1) espaço.
