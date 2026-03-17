# O(n³) - Tempo Cúbico
# Três laços aninhados, cada um rodando ~n vezes, produzem n³ operações.
# O laço mais interno sempre executa 9 vezes → O(1), portanto não adiciona um fator.


def muitos_niveis(n):
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, k + 10):  # sempre 9 iterações → O(1)
                    total += 1
    return total


print(muitos_niveis(25))


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
# Tempo: O(n³)
#   Laço i: O(n)
#   Laço j: O(n)  (roda uma fração de n, mas constantes são descartadas)
#   Laço k: O(n)
#   Laço l: O(1)  (sempre 9 iterações, independente da entrada)
# Espaço: O(1)
