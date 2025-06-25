from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:


    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки пузырьком

    for i in range(len(container)):

        for j in range(len(container) - i - 1):
            if container[j] > container[j + 1]:
                container[j], container[j + 1] = container[j + 1], container[j]


    return container


if __name__ == "__main__":
    data = [5,8,3,6,2,1,9]
    print("Неотсортированный массив:", data)

    sort(data)

    print("Отсортированный массив:", data)