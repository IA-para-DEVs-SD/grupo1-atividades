def duplicado(lista):
    vistos = set()
    duplicados = set()
    for item in lista:
        if item in vistos:
            duplicados.add(item)
        vistos.add(item)
    return duplicados

numeros = [1, 2, 3, 4, 2, 3]
duplicados = duplicado(numeros)
if duplicados:
    print(f'Números duplicados: {duplicados}')
else:
    print('Não há duplicados')
