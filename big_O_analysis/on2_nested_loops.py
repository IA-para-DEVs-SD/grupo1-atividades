# O(n²) - Tempo Quadrático
# Laços aninhados sobre a mesma entrada produzem n * n = n² operações.


def lacos_aninhados(items):
    """Laço aninhado simples — todos os pares de elementos."""
    for item in items:
        for item2 in items:
            print(item, ' ', item2)


def termo_dominante(items):
    """O(n + n²) simplifica para O(n²) — mantemos apenas o termo dominante."""
    print('Parte linear:')
    for item in items:
        print(item)

    print('\nParte quadrática:')
    for item_um in items:
        for item_dois in items:
            print(item_um, item_dois)


lacos_aninhados([1, 2, 3])
termo_dominante(['a', 'b', 'c'])


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
# lacos_aninhados: Tempo O(n²), Espaço O(1)
# termo_dominante: Tempo O(n + n²) → O(n²), Espaço O(1)
