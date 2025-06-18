from typing import Sequence


def binary_search(
        value: int, seq: Sequence[int],
        left_border: int = 0, right_border: int = None
) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск
    :param left_border: Левая граница массива, нужна для рекурсивного алгоритма
    :param right_border: Правая граница массива, нужна для рекурсивного алгоритма

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    if right_border is None:
        right_border = len(seq) - 1

    if left_border > right_border:
        raise ValueError('')

    ind_pivot = (right_border + left_border) // 2
    current_value = seq[ind_pivot]

    if current_value == value:
        while True:
            if ind_pivot - 1 >= 0 and seq[ind_pivot - 1] == value:
                ind_pivot -= 1
            else:
                return ind_pivot

        # while True:
        #     if not 0 <= ind_pivot - 1 < len(seq) or seq[ind_pivot - 1] != value:
        #         return ind_pivot
        #     else:
        #         ind_pivot -= 1

    if current_value > value:
        right_border = ind_pivot - 1
    else:
        left_border = ind_pivot + 1
    # print(ind_a, ind_b)
    return binary_search(value, seq,  left_border, right_border)

    ...  # TODO реализовать алгоритм бинарного поиска
