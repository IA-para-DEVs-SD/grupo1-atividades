# O(log n) - Tempo Logarítmico
# Cada iteração divide (ou multiplica) o tamanho do problema por 2.
# O laço executa log₂(n) vezes.


def imprimir_potencias_de_2(n):
    i = 1
    while i < n:
        print(i)
        i = i * 2


def imprimir_metades(n):
    while n > 1:
        print(n)
        n = n // 2


print("Potências de 2 até 25:")
imprimir_potencias_de_2(25)

print("\nDividindo 36 pela metade:")
imprimir_metades(36)


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
# Tempo: O(log n) — número de execuções = log₂(n)
# Espaço: O(1)
