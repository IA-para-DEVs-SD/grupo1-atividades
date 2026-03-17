# O(1) - Tempo e Espaço Constante
# O número de operações não muda conforme o tamanho da entrada cresce.


def par_ou_impar(n):
    return "Par" if n % 2 == 0 else "Ímpar"


def imprimir_primeiro_ao_quadrado(items):
    resultado = items[0] * items[0]
    print(resultado)


print(par_ou_impar(11))                    # Ímpar
print(imprimir_primeiro_ao_quadrado([4, 5, 6, 8]))  # 16


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
# Tempo: O(1) — sem laços nem recursão; sempre o mesmo número de passos.
# Espaço: O(1)
