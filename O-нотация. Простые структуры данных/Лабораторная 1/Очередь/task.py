
"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        """
        self.my_queue = []  # TODO инициализировать список

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self.my_queue.append(elem)  # TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        # TODO реализовать метод dequeue
        if not self.my_queue:
            raise IndexError("Извлечение из пустого списка не возможно")

        return self.my_queue.pop(0)




    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        ...  # TODO реализовать метод peek
        if not isinstance(ind, int):
            raise TypeError(f"Индекс должен быть целочисленного типа, а не {type(ind).__name__}")

        if not 0 <= ind < len(self.my_queue):
            raise IndexError("Индекс все границ очереди")

        return self.my_queue[ind]
    def clear(self) -> None:
        """ Очистка очереди. """
        ...  # TODO реализовать метод clear
        self.my_queue.clear()
    def __len__(self):
        """ Количество элементов в очереди. """
        ...  # TODO реализовать метод __len__
        return len(self.my_queue)
