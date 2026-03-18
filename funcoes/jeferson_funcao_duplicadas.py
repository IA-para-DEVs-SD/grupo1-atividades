def duplicado(lista):
    return len(lista) != len(set(lista))

def encontrar_duplicatas(numeros):
    vistos = set()
    duplicatas = set()
    for n in numeros:
        if n in vistos:
            duplicatas.add(n)
        vistos.add(n)
    return duplicatas
    
numeros = [1,2,3,4,4,4]
if duplicado(numeros):
    print(encontrar_duplicatas(numeros))
    print('Existe duplicado')
else:
    print('Não duplicados')


