from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    ...  # TODO решить задачу с помощью динамического программирования

    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1  # начальная клетка

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            ways = 0
            if i > 0:
                ways += dp[i-1][j]
            if j > 0:
                ways += dp[i][j-1]
            if i > 0 and j > 0:
                ways += dp[i-1][j-1]
            dp[i][j] = ways

    return dp



if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
