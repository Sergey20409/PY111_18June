from typing import Union, Sequence
from functools import lru_cache


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO реализовать ленивую динамику

    def cost_star(n):
        if n in (0, 1):
            return stairway[n]

        return stairway[n] + min(cost_star(n-1), cost_star(n-2))
    return cost_star(len(stairway)-1)


if __name__ == '__main__':
    print(stairway_path((1, 3, 1, 5)))  # 7
