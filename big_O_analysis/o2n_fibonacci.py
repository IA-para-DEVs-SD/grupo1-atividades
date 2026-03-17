# O(2^n) - Tempo Exponencial
# Fibonacci recursivo: cada chamada se divide em 2 novas chamadas.
# A árvore de chamadas tem ~2^n nós.


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(10))  # 55

# Sequência de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...


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
# Tempo: O(2^n) — cada chamada gera 2 novas, formando uma árvore binária de profundidade n.
# Espaço: O(n) — profundidade máxima da pilha de chamadas é n
#          (ramo mais fundo: f(n) → f(n-1) → ... → f(0)).
