from typing import Hashable, Mapping, Union
import networkx as nx
import heapq

from typing import Any

from collections import deque


class PriorityQueue:
    HIGH_PRIORITY = 0  # наивысший приоритет
    LOW_PRIORITY = 100  # наименьший приоритет

    def __init__(self):
        ...  # TODO использовать deque для реализации очереди с приоритетами
        # self.data = {}
        # for pr in range(self.HIGH_PRIORITY, self.LOW_PRIORITY + 1):
        #     self.data[pr] = deque()
        self._len = 0
        self.data = {pr: deque() for pr in range(self.HIGH_PRIORITY, self.LOW_PRIORITY + 1)}

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Добавление элемент в конец очереди c учетом приоритета

        :param elem: Элемент, который должен быть добавлен
        :param priority: Приоритет добавляемого элемента
        """
        if not self.HIGH_PRIORITY <= priority <= self.LOW_PRIORITY:
            raise ValueError('...')

        self.data[priority].appendleft(elem)
        self._len += 1
        ...  # TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """

        ...  # TODO реализовать метод dequeue
        for pr, deq in self.data.items():
            if deq:
                self._len -= 1
                return pr, deq.pop()

        raise IndexError('Ошибка, если очередь пуста')


    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди с указанным приоритетом, и т.д.)
        :param priority: Приоритет очереди

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError
        if not 0 <= ind <= len(self.data[priority]):
            raise IndexError

        return self.data[priority][-1 - ind]
        ...  # TODO реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди. """
        self.__init__()  # TODO реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди. """
        return self._len
        len_ = 0
        for deq in self.data:
            len_ += len(deq)
        return len_

        ...  # TODO реализовать метод __len__




def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Функция с помощью алгоритма Дейкстры из модуля NetworkX находит кратчайшие пути до всех достижимых вершин графа.
    Если вершина не достижима, то стоимость пути до неё должна быть равно float("inf")

    :param g: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :param starting_node: Стартовый узел, откуда нужно начать обход
    :return: словарь как {'node1': 0, 'node2': 10, '3': 33, ...} со стоимостью путей, где node1, node2 - это узлы из графа g
    """
    # _, coasts = nx.dijkstra_predecessor_and_distance(g, starting_node)
    # for node in g.nodes:
    #     if node not in coasts:
    #         coasts[node] = float("inf")

    # return coasts

    distances = {node: float('inf') for node in g.nodes}
    distances[starting_node] = 0
    predecessors = {node: None for node in g.nodes}

    queue = PriorityQueue()
    queue.enqueue(starting_node, 0)
    # queue = [(0, starting_node)]

    # while queue:
    while len(queue):

        # cur_dist, cur_node = heapq.heappop(queue)
        cur_dist, cur_node = queue.dequeue()
        if cur_dist > distances[cur_node]:
            continue

        for ng, w in g[cur_node].items():
            distance = cur_dist + w['weight']
            if distance < distances[ng]:
                distances[ng] = distance
                predecessors[ng] = cur_node
                # heapq.heappush(queue, (distance, ng))
                queue.enqueue(ng, distance)

    return distances #, predecessors

if __name__ == '__main__':
    graph = nx.DiGraph()
    graph.add_weighted_edges_from([
        (1, 2, 7),
        (1, 3, 9),
        (1, 6, 14),
        (2, 3, 10),
        (2, 4, 15),
        (3, 4, 11),
        (3, 6, 2),
        (4, 5, 6),
        # (6, 5, 9),
        (5, 6, 9),
    ])

    print(dijkstra_algo(graph, 1))  # {1: 0, 2: 7, 3: 9, 6: 11, 4: 20, 5: 26}

    # graph = nx.DiGraph()
    # graph.add_weighted_edges_from([
    #     ('A', 'B', 1),
    #     ('D', 'A', 2),
    #     ('G', 'D', 1),
    #     ('D', 'E', 2),
    #     ('E', 'F', 3),
    #     ('B', 'D', 2),
    #     ('B', 'C', 3),
    #     ('B', 'E', 8),
    #     ('C', 'E', 4),
    #     ('C', 'D', 1),
    # ])
    #
    # print(dijkstra_algo(graph, 'A'))