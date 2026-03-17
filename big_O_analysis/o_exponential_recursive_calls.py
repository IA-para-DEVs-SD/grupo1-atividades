# O(2^n) e O(3^n) - Tempo Exponencial
# Cada chamada recursiva se ramifica em múltiplas sub-chamadas.
# Visualize como uma árvore: fator de ramificação = base do expoente.


def duas_chamadas(n):
    """Ramifica em 2 chamadas → O(2^n)"""
    print(n)
    if n == 0:
        return
    duas_chamadas(n - 1)
    duas_chamadas(n - 1)


def tres_chamadas(n):
    """Ramifica em 3 chamadas → O(3^n)"""
    print(n)
    if n == 0:
        return
    tres_chamadas(n - 1)
    tres_chamadas(n - 1)
    tres_chamadas(n - 1)


print("duas_chamadas(3):")
duas_chamadas(3)

print("\ntres_chamadas(2):")
tres_chamadas(2)


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
# duas_chamadas: Tempo O(2^n), Espaço O(n) — profundidade da pilha é n.
# tres_chamadas: Tempo O(3^n), Espaço O(n) — profundidade da pilha é n.
