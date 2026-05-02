# =========================================
# IMPORTS
# =========================================
import heapq

# =========================================
# CLASSE GRAPH
# =========================================
class Graph:
    def __init__(self):
        self.grafo = {}

    # Adicionar aresta
    def adicionar_aresta(self, origem, destino, peso):
        if origem not in self.grafo:
            self.grafo[origem] = []
        if destino not in self.grafo:
            self.grafo[destino] = []

        self.grafo[origem].append((destino, peso))
        self.grafo[destino].append((origem, peso))  # grafo não direcionado

    # Dijkstra
    def dijkstra(self, inicio):
        distancias = {no: float('inf') for no in self.grafo}
        predecessores = {no: None for no in self.grafo}

        distancias[inicio] = 0
        fila = [(0, inicio)]

        while fila:
            distancia_atual, no_atual = heapq.heappop(fila)

            for vizinho, peso in self.grafo[no_atual]:
                nova_distancia = distancia_atual + peso

                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = no_atual
                    heapq.heappush(fila, (nova_distancia, vizinho))

        return distancias, predecessores

    # Reconstruir caminho
    def menor_caminho(self, inicio, destino):
        distancias, predecessores = self.dijkstra(inicio)

        caminho = []
        atual = destino

        while atual is not None:
            caminho.insert(0, atual)
            atual = predecessores[atual]

        if distancias[destino] == float('inf'):
            return None, float('inf')

        return caminho, distancias[destino]

    # Mostrar grafo
    def mostrar_grafo(self):
        print("\nGrafo:")
        for no in self.grafo:
            print(f"{no} -> {self.grafo[no]}")


# =========================================
# TESTES
# =========================================
if __name__ == "__main__":

    g = Graph()

    # Criando grafo de exemplo
    g.adicionar_aresta('A', 'B', 4)
    g.adicionar_aresta('A', 'C', 2)
    g.adicionar_aresta('B', 'C', 1)
    g.adicionar_aresta('B', 'D', 5)
    g.adicionar_aresta('C', 'D', 8)
    g.adicionar_aresta('C', 'E', 10)
    g.adicionar_aresta('D', 'E', 2)
    g.adicionar_aresta('D', 'F', 6)
    g.adicionar_aresta('E', 'F', 3)

    g.mostrar_grafo()

    print("\n===== MENOR CAMINHO =====")

    inicio = 'A'
    destino = 'F'

    caminho, distancia = g.menor_caminho(inicio, destino)

    if caminho:
        print(f"\nCaminho de {inicio} até {destino}: {' -> '.join(caminho)}")
        print(f"Distância total: {distancia}")
    else:
        print("Não existe caminho entre os nós.")