class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def adicionar_aresta(self, u, v, peso):
        self.grafo.append([u, v, peso])

    def encontrar(self, pai, i):
        if pai[i] == i:
            return i
        return self.encontrar(pai, pai[i])

    def unir(self, pai, rank, x, y):
        raiz_x = self.encontrar(pai, x)
        raiz_y = self.encontrar(pai, y)

        if rank[raiz_x] < rank[raiz_y]:
            pai[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            pai[raiz_y] = raiz_x
        else:
            pai[raiz_y] = raiz_x
            rank[raiz_x] += 1

    def kruskal(self):
        resultado = []
        i = 0
        e = 0
        self.grafo = sorted(self.grafo, key=lambda item: item[2])
        pai = []
        rank = []

        for node in range(self.V):
            pai.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, peso = self.grafo[i]
            i += 1
            x = self.encontrar(pai, u)
            y = self.encontrar(pai, v)

            if x != y:
                e += 1
                resultado.append([u, v, peso])
                self.unir(pai, rank, x, y)

        return resultado


# Entrada de dados
V = int(input("Digite o número de nós (zonas): "))
E = int(input("Digite o número de arestas (estradas): "))

g = Grafo(V)

print("Digite as arestas e seus respectivos pesos:")
for i in range(E):
    u, v, peso = input(f"Aresta {i+1}: ").split()
    u = int(u)
    v = int(v)
    peso = int(peso)
    g.adicionar_aresta(u, v, peso)

# Cálculo da árvore de expansão mínima
arvore_expansao_minima = g.kruskal()

# Saída dos resultados
print("Arestas na árvore de expansão mínima:")
for u, v, peso in arvore_expansao_minima:
    print(f"{u} -- {v} : {peso}")
