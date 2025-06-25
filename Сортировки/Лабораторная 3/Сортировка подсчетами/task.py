from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки подсчетами
    if not container:
        return container

    # Находим минимальное и максимальное значения
    min_val = min(container)
    max_val = max(container)

    # Создаём массив для подсчёта
    count = [0] * (max_val - min_val + 1)

    # Подсчитываем количество каждого элемента
    for num in container:
        count[num - min_val] += 1

    # Восстанавливаем отсортированный массив
    sorted_container = []
    for i in range(len(count)):
        sorted_container.extend([i + min_val] * count[i])

    return sorted_container
