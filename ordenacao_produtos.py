import random
import datetime
import time
import heapq

class Produto:
    def __init__(self, nome, preco, avaliacao, data_adicao, categoria):
        self.nome = nome
        self.preco = preco
        self.avaliacao = avaliacao
        self.data_adicao = data_adicao
        self.categoria = categoria

    def __repr__(self):
        return f"{self.nome} | R${self.preco} | {self.avaliacao}⭐ | {self.data_adicao.date()} | {self.categoria}"

def gerar_produtos(n):
    produtos = []

    for i in range(n):
        nome = f"Produto{i}"
        preco = round(random.uniform(10, 1000), 2)
        avaliacao = round(random.uniform(0, 5), 2)
        data_adicao = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365))
        categoria = f"Categoria{random.randint(1, 5)}"

        produtos.append(Produto(nome, preco, avaliacao, data_adicao, categoria))

    return produtos

def bubble_sort(lista, key=lambda x: x):
    arr = lista[:]
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if key(arr[j]) > key(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def quick_sort(lista, key=lambda x: x):
    if len(lista) <= 1:
        return lista

    pivot = lista[0]
    menores = [x for x in lista[1:] if key(x) <= key(pivot)]
    maiores = [x for x in lista[1:] if key(x) > key(pivot)]

    return quick_sort(menores, key) + [pivot] + quick_sort(maiores, key)


def merge_sort(lista, key=lambda x: x):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], key)
    direita = merge_sort(lista[meio:], key)

    return merge(esquerda, direita, key)


def merge(esq, dir, key):
    resultado = []
    i = j = 0

    while i < len(esq) and j < len(dir):
        if key(esq[i]) < key(dir[j]):
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado


def heap_sort(lista, key=lambda x: x):
    heap = [(key(item), i, item) for i, item in enumerate(lista)]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[2] for _ in range(len(heap))]

def medir_tempo(func, lista, key):
    inicio = time.time()
    func(lista, key)
    fim = time.time()
    return fim - inicio

if __name__ == "__main__":

    print("Gerando produtos...")
    produtos = gerar_produtos(1000)

    print("\nExemplo de produtos:")
    for p in produtos[:5]:
        print(p)

    criterios = {
        "Preço": lambda x: x.preco,
        "Avaliação": lambda x: x.avaliacao,
        "Data": lambda x: x.data_adicao,
        "Categoria": lambda x: x.categoria
    }

    algoritmos = {
        "Bubble": bubble_sort,
        "Quick": quick_sort,
        "Merge": merge_sort,
        "Heap": heap_sort
    }

    print("\n===== TESTE DE DESEMPENHO =====")

    for criterio_nome, criterio_func in criterios.items():
        print(f"\n--- Ordenando por {criterio_nome} ---")

        for alg_nome, alg_func in algoritmos.items():
            tempo = medir_tempo(alg_func, produtos, criterio_func)
            print(f"{alg_nome}: {tempo:.5f} segundos")

    # Verificação com sorted()
    print("\n===== VERIFICAÇÃO =====")
    python_sorted = sorted(produtos, key=lambda x: x.preco)
    merge_sorted = merge_sort(produtos, key=lambda x: x.preco)

    print("Ordenação correta?", python_sorted[:10] == merge_sorted[:10])