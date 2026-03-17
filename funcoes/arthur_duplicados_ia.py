from collections import Counter

def funcao_ia(lista):
    contagem = Counter(lista)
    duplicados = sorted(k for k, v in contagem.items() if v > 1)
    sem_duplicados = sorted(contagem)
    tem = bool(duplicados)
    return tem, duplicados, sem_duplicados


tem, duplicados, sem_duplicados = funcao_ia(
    [14, 287, 33, 91, 156, 399, 22, 14, 88, 312, 45, 198, 276, 33, 102, 5, 388, 21, 156, 49, 301, 224, 11, 367, 89, 142, 33, 290, 111, 400, 56, 78, 22, 190, 311, 25, 67, 142, 9, 334, 212, 45, 177, 88, 203, 31, 156, 390, 12, 88, 254, 331, 19, 44, 276, 101, 8, 355, 22, 167, 198, 45, 300, 122, 54, 231, 388, 91, 14, 221, 309, 15, 77, 287, 33, 11, 190, 254, 38, 210, 5, 367, 122, 89, 45, 312, 276, 18, 99, 301, 142, 224, 33, 11, 67, 287, 399, 156, 22, 88]
)

print("Tem duplicados" if tem else "Não tem duplicados")
print("Duplicados:", duplicados)
print("Sem duplicados:", sem_duplicados)