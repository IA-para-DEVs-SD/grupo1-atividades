import matplotlib.pyplot as plt
import math

x = [2, 4, 6, 8, 10, 12]
y = [v * math.log2(v) for v in x]

plt.plot(x, y, 'b')
plt.xlabel('Entradas')
plt.ylabel('Passos')
plt.title('Complexidade Linearítmica — O(n log n)')
plt.show()
