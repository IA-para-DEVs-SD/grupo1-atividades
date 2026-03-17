import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10, 12]
y = [v ** 2 for v in x]

plt.plot(x, y, 'b')
plt.xlabel('Entradas')
plt.ylabel('Passos')
plt.title('Complexidade Quadrática — O(n²)')
plt.show()
