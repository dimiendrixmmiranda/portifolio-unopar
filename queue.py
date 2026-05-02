# =========================================
# IMPORTS
# =========================================
import heapq
import itertools

REMOVED = '<removido>'  # marcador para tarefas removidas

# =========================================
# CLASSE PRIORITY QUEUE
# =========================================
class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}  # rastrear tarefas
        self.counter = itertools.count()

    # Inserir tarefa
    def add_task(self, task, priority=0):
        if task in self.entry_finder:
            self.remove_task(task)

        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.heap, entry)

    # Remover tarefa
    def remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = REMOVED

    # Pegar menor prioridade
    def pop_task(self):
        while self.heap:
            priority, count, task = heapq.heappop(self.heap)
            if task is not REMOVED:
                del self.entry_finder[task]
                return task, priority
        raise KeyError("Fila vazia")

    # Alterar prioridade
    def update_priority(self, task, priority):
        self.add_task(task, priority)

    # Mostrar fila (debug)
    def mostrar(self):
        print("\nFila atual:")
        for item in self.heap:
            if item[2] != REMOVED:
                print(f"Tarefa: {item[2]} | Prioridade: {item[0]}")

# =========================================
# TESTES
# =========================================
def test_priority_queue():
    pq = PriorityQueue()

    print("Adicionando tarefas...")
    pq.add_task("Estudar", 3)
    pq.add_task("Trabalhar", 1)
    pq.add_task("Dormir", 5)
    pq.mostrar()

    print("\nInserindo nova tarefa...")
    pq.add_task("Academia", 2)
    pq.mostrar()

    print("\nRemovendo tarefa de menor prioridade...")
    tarefa, prioridade = pq.pop_task()
    print(f"Removido: {tarefa} ({prioridade})")
    pq.mostrar()

    print("\nAlterando prioridade de 'Dormir'...")
    pq.update_priority("Dormir", 0)
    pq.mostrar()

    print("\nRemovendo todas as tarefas:")
    while True:
        try:
            tarefa, prioridade = pq.pop_task()
            print(f"Removido: {tarefa} ({prioridade})")
        except KeyError:
            break

# =========================================
# MAIN
# =========================================
if __name__ == "__main__":
    test_priority_queue()