"""
Comparação visual de todas as complexidades Big O comuns.
Execução: pipenv run python viz_comparison.py
"""

import math
import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 25)

complexities = {
    "O(1)":        np.ones_like(n, dtype=float),
    "O(log n)":    np.log2(n),
    "O(√n)":       np.sqrt(n),
    "O(n)":        n.astype(float),
    "O(n log n)":  n * np.log2(np.maximum(n, 1)),
    "O(n²)":       n ** 2.0,
    "O(2^n)":      2.0 ** n,
}

fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# --- Gráfico 1: todas as curvas (escala limitada para visualizar as menores) ---
ax1 = axes[0]
for label, y in complexities.items():
    ax1.plot(n, y, linewidth=2, label=label)

ax1.set_ylim(0, 80)
ax1.set_xlabel("Tamanho da entrada (n)", fontsize=12)
ax1.set_ylabel("Operações", fontsize=12)
ax1.set_title("Comparação Big O (escala limitada)", fontsize=14)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# --- Gráfico 2: escala logarítmica para ver o impacto real ---
ax2 = axes[1]
for label, y in complexities.items():
    ax2.plot(n, y, linewidth=2, label=label)

ax2.set_yscale("log")
ax2.set_xlabel("Tamanho da entrada (n)", fontsize=12)
ax2.set_ylabel("Operações (escala log)", fontsize=12)
ax2.set_title("Comparação Big O (escala logarítmica)", fontsize=14)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3, which="both")

plt.tight_layout()
plt.savefig("big_o_comparison.png", dpi=150, bbox_inches="tight")
print("Gráfico salvo em big_o_comparison.png")
plt.show()
