# FAQ — Notação Big O

---

**P: Por que focamos na taxa de crescimento em vez do tempo exato de execução?**

R: O tempo exato depende do hardware, sistema operacional e ambiente onde o código roda — portanto não pode ser usado para comparar algoritmos de forma justa. A taxa de crescimento descreve como um algoritmo *escala* independentemente da máquina, tornando-se uma medida universal de eficiência.

---

**P: Por que o tempo de execução é expresso em relação ao tamanho da entrada?**

R: Precisamos de um ponto de referência. Expressar a velocidade em termos do tamanho da entrada `n` nos permite ver como o desempenho muda conforme os dados crescem — que é o que importa na prática.

---

**P: Por que nos preocupamos com entradas grandes?**

R: Para entradas pequenas, a maioria dos algoritmos é rápida o suficiente e as diferenças são negligenciáveis. O custo real aparece em escala. Um algoritmo O(n²) em 100 itens funciona bem; em 1.000.000 de itens torna-se inutilizável.

---

**P: Por que descartamos constantes? (ex: O(2n) → O(n))**

R: Big O descreve a *forma* do crescimento, não a contagem exata. À medida que `n` tende ao infinito, um multiplicador constante tem impacto cada vez menor na comparação relativa entre algoritmos. O(n) e O(2n) crescem linearmente — a forma é a mesma.

---

**P: As constantes importam na prática?**

R: Sim — mesmo que Big O as ignore, constantes podem importar em sistemas reais. O(n) e O(n/6) são ambos escritos como O(n), mas se um script leva 1 hora para rodar, otimizá-lo para rodar em 10 minutos vale muito a pena. Big O diz *qual algoritmo escolher*; as constantes dizem *o quanto vale otimizá-lo*.

---

**P: Qual é a diferença entre complexidade de tempo e complexidade de espaço?**

R: Complexidade de tempo mede como o número de *operações* cresce com o tamanho da entrada. Complexidade de espaço mede quanta *memória adicional* é necessária (além da própria entrada) conforme a entrada cresce. Ambas usam a notação Big O.

---

**P: O que significa "pior caso"?**

R: Big O tipicamente descreve o cenário de pior caso — o número máximo de passos que um algoritmo pode executar para um dado tamanho de entrada. Por exemplo, a busca binária é O(log n) no pior caso (alvo na extremidade ou não encontrado), mas O(1) no melhor caso (alvo encontrado na primeira comparação).

---

**P: O que é O(√n)?**

R: Um algoritmo O(√n) executa um número de operações proporcional à raiz quadrada da entrada. Um exemplo clássico é o teste de primalidade: para verificar se `n` é primo, basta checar divisores até `√n`, pois se `n` tem um fator maior que `√n`, necessariamente tem um menor.

---

**P: Qual é a diferença entre melhor caso, caso médio e pior caso?**

R: São três formas de analisar o desempenho de um algoritmo:

- **Melhor caso (best case):** o cenário mais favorável — menor número de operações. Ex: busca linear encontra o alvo no primeiro elemento → O(1).
- **Caso médio (average case):** o desempenho esperado considerando todas as entradas possíveis. Ex: busca linear em média percorre metade da lista → O(n/2) → O(n).
- **Pior caso (worst case):** o cenário mais desfavorável — maior número de operações. Ex: busca linear percorre toda a lista sem encontrar o alvo → O(n).

Big O tipicamente descreve o pior caso, a menos que se diga o contrário.

---

**P: Qual é a ordem das complexidades comuns, da mais rápida para a mais lenta?**

```
O(1) < O(log n) < O(√n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2^n) < O(n!)
```

---

**P: Como determino o Big O de um algoritmo?**

R: Algumas regras práticas:

- Um único laço sobre `n` itens → O(n)
- Um laço que divide/multiplica o problema a cada passo → O(log n)
- Dois laços aninhados sobre `n` itens → O(n²)
- Algoritmo que divide o problema e combina resultados (ex: merge sort) → O(n log n)
- Função recursiva que se ramifica em `k` chamadas de tamanho `n-1` → O(k^n)
- Descarte constantes: O(3n) → O(n)
- Descarte termos não dominantes: O(n² + n) → O(n²)

---

---

Veja também o [README](README.md) para exemplos práticos de cada classe de complexidade.

---

**Referências**

- Tabela Big O: https://www.bigocheatsheet.com/
- Complexidade das estruturas de dados do Python: https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
