import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10, 12]
y = [2, 2, 2, 2, 2, 2]

plt.plot(x, y, 'b')
plt.xlabel('Entradas')
plt.ylabel('Passos')
plt.title('Complexidade Constante — O(1)')
plt.show()
