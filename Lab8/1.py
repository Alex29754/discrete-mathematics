import random
from collections import deque
import copy

# ===== 1. Исходный граф из задания =====
original_edges = [
    ('S', 'A', 14), ('S', 'B', 12),
    ('A', 'C', 37), ('B', 'D', 7),
    ('C', 'E', 30), ('C', 'F', 23),
    ('D', 'F', 31),
    ('E', 'G', 16), ('F', 'G', 22), ('F', 'H', 20),
    ('G', 'T', 24), ('H', 'T', 25)
]

# ===== Вспомогательные функции =====

# Построение графа
def build_graph(edges):
    graph = {}
    for u, v, capacity in edges:
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = capacity
        graph[v][u] = 0  # Обратное ребро
    return graph

# BFS для нахождения пути
def bfs(graph, s, t, parent):
    visited = set()
    queue = deque([s])
    visited.add(s)
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in visited and graph[u][v] > 0:
                visited.add(v)
                parent[v] = u
                if v == t:
                    return True
                queue.append(v)
    return False

# Алгоритм Эдмондса-Карпа
def edmonds_karp(graph, source, sink):
    parent = {}
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
        max_flow += path_flow
    return max_flow

# Поиск достижимых вершин
def find_reachable(graph, source):
    visited = set()
    queue = deque([source])
    visited.add(source)
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if graph[u][v] > 0 and v not in visited:
                visited.add(v)
                queue.append(v)
    return visited

# Поиск минимального разреза
def find_min_cut(graph, residual_graph, source):
    reachable = find_reachable(residual_graph, source)
    min_cut = []
    for u in reachable:
        for v in graph[u]:
            if v not in reachable and graph[u][v] > 0:
                min_cut.append((u, v))
    return min_cut

# ======= 2. Решение для ИСХОДНЫХ ДАННЫХ =======

print("=== Исходный граф ===")
graph1 = build_graph(original_edges)
residual1 = copy.deepcopy(graph1)
max_flow1 = edmonds_karp(residual1, 'S', 'T')
min_cut1 = find_min_cut(graph1, residual1, 'S')

print("Максимальный поток:", max_flow1)
print("Минимальный разрез:", min_cut1)

# ======= 3. Решение для СЛУЧАЙНЫХ ВЕСОВ =======

print("\n=== Граф со случайными пропускными способностями ===")
random_edges = [(u, v, random.randint(100, 1000)) for (u, v, _) in original_edges]
for edge in random_edges:
    print(f"{edge[0]} → {edge[1]}: {edge[2]}")

graph2 = build_graph(random_edges)
residual2 = copy.deepcopy(graph2)
max_flow2 = edmonds_karp(residual2, 'S', 'T')
min_cut2 = find_min_cut(graph2, residual2, 'S')

print("\nМаксимальный поток (случайный граф):", max_flow2)
print("Минимальный разрез (случайный граф):", min_cut2)