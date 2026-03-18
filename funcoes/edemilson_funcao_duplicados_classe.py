from numpy.random import randint


class VerificadorDuplicados:
    def __init__(self, lista):
        self.lista = lista

    def tem_duplicados(self):
        return len(self.lista) != len(set(self.lista))

    def resultado(self):
        if self.tem_duplicados():
            return 'A lista possui duplicados'
        else:
            return 'A lista não possui duplicados'


if __name__ == '__main__':
    # numeros = randint(1, 1000, size=10)
    numeros = [1, 2, 3, 3, 2, 1]

    verificador = VerificadorDuplicados(numeros)
    print(verificador.resultado())
