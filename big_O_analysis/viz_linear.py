import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10, 12]
y = [2 * v for v in x]  # y = 2x

plt.plot(x, y, 'b')
plt.xlabel('Entradas')
plt.ylabel('Passos')
plt.title('Complexidade Linear — O(n)')
plt.show()
