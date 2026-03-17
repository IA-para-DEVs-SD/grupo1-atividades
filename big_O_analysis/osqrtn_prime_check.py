# O(√n) - Tempo Raiz Quadrada
# Verificar primalidade requer testar divisores apenas até √n.
# Se nenhum divisor for encontrado até lá, o número é primo.

import math


def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print(eh_primo(2))    # True
print(eh_primo(17))   # True
print(eh_primo(18))   # False
print(eh_primo(97))   # True
print(eh_primo(100))  # False


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
# Tempo: O(√n) — o laço executa no máximo √n vezes.
# Espaço: O(1)
