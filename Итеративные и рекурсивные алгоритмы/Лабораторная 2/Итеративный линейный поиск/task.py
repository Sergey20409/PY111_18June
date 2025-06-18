"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    ...  # TODO реализовать итеративный линейный поиск
    if not arr:
        raise ValueError ("Пустой список")

    min_value = []
    min_value_ind = []

    for i in range(0, len(arr)):
        if i == 0:
            min_value = arr[i]
            min_value_ind = int(i)
        if arr[i] < min_value:
            min_value = arr[i]
            min_value_ind = int(i)
        else:
            continue
    return min_value_ind