# O(n) - Descartando Constantes
# Múltiplos laços sobre a mesma entrada ainda são O(n), não O(2n) ou O(n + 20).
# Em Big O, constantes são sempre descartadas.


def fazer_varias_coisas(items):
    ultimo_idx = len(items) - 1
    print(items[ultimo_idx])                # O(1)

    meio_idx = len(items) // 2
    idx = 0
    while idx < meio_idx:                   # O(n/2) → O(n)
        print(items[idx])
        idx += 1

    for num in range(20):                   # O(20) → O(1)
        print(num)


fazer_varias_coisas(['pizza', 'escova de dente', 'estrada de terra', 'spam',
                     'alienígena', 'o bolo é uma mentira', 'Gatorade'])


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
# Tempo: O(1 + n/2 + 20) → O(n) — constantes são descartadas.
# Espaço: O(1)
