# Лабораторная работа №9 (Вариант 21)
# Поиск наибольшего паросочетания

from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

# Список рёбер
edges = [
    (7, 13), (2, 13), (6, 11), (2, 4), (3, 13), (4, 6), (15, 16), (8, 14), (2, 16),
    (14, 16), (8, 14), (2, 16), (14, 16), (6, 8), (3, 11), (7, 11), (4, 15),
    (5, 8), (3, 4), (6, 16), (10, 13), (4, 12), (8, 9), (11, 15), (4, 10),
    (10, 16), (10, 11), (2, 11),(4, 9), (5, 11), (5, 16), (11, 12), (13, 15), (4, 7), (11, 14), (2, 8), (12, 13), (8, 12)
]

# Построение графа
def build_graph(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

# Проверка на двудольность и получение долей
def check_bipartite(G):
    is_bipartite = nx.is_bipartite(G)
    if is_bipartite:
        X, Y = nx.bipartite.sets(G)
        return True, X, Y
    return False, None, None

# Реализация алгоритма Куна для двудольного графа
def kuhn(G, left):
    match_to = {}
    used = set()

    def try_kuhn(v):
        if v in used:
            return False
        used.add(v)
        for u in G[v]:
            if u not in match_to or try_kuhn(match_to[u]):
                match_to[u] = v
                return True
        return False

    for v in left:
        used.clear()
        try_kuhn(v)

    return [(v, u) for u, v in match_to.items()]

# Алгоритм Форда-Фалкерсона с помощью максимального потока
def ford_fulkerson_max_matching(G, X, Y):
    FG = nx.DiGraph()
    FG.add_node("s")
    FG.add_node("t")
    for x in X:
        FG.add_edge("s", x, capacity=1)
        for y in G[x]:
            if y in Y:
                FG.add_edge(x, y, capacity=1)
    for y in Y:
        FG.add_edge(y, "t", capacity=1)

    flow_value, flow_dict = nx.maximum_flow(FG, "s", "t")
    matching = []
    for x in X:
        for y in G[x]:
            if y in flow_dict.get(x, {}) and flow_dict[x][y] == 1:
                matching.append((x, y))
    return matching

# Визуализация графа и паросочетания
def draw_matching(G, matching, title):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, edgelist=matching, edge_color='red', width=2)
    plt.title(title)
    plt.show()

# Основная программа
G = build_graph(edges)
bipartite, X, Y = check_bipartite(G)

if not bipartite:
    print("Граф не является двудольным. Необходимо удалить рёбра вручную для получения двудольного.")
else:
    print("Граф двудольный.")
    # Алгоритм Куна
    matching_kuhn = kuhn(G, X)
    print("Паросочетание (Кун):", matching_kuhn)
    draw_matching(G, matching_kuhn, "Максимальное паросочетание (Кун)")

    # Алгоритм Форда-Фалкерсона
    matching_ff = ford_fulkerson_max_matching(G, X, Y)
    print("Паросочетание (Форд-Фалкерсон):", matching_ff)
    draw_matching(G, matching_ff, "Максимальное паросочетание (Форд-Фалкерсон)")
