from typing import Hashable, List
import networkx as nx
from collections import deque


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в глубину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    ...  # TODO реализовать обход в глубину
    visited = {node: False for node in g.nodes}
    path = []
    # d = deque()

    #
    # d.append(start_node)
    # visited[start_node] = True
    # while d:
    #     current_node = d.pop()
    #     path.append(current_node)
    #     for ng in g.neighbors(current_node):
    #         if not visited[ng]:
    #             d.append(ng)
    #             visited[ng] = True

    def rec_f(current_node):
        visited[current_node] = True
        path.append(current_node)
        for ng in g.neighbors(current_node):
            if not visited[ng]:
                rec_f(ng)

    rec_f(start_node)

    return path


graph = nx.Graph()
graph.add_nodes_from("ABCDEFG")
graph.add_edges_from([
    ('A', 'C'),
    ('C', 'F'),
    ('A', 'B'),
    ('B', 'D'),
    ('B', 'E'),
    ('G', 'E'),
])

print(dfs(graph, 'A'))