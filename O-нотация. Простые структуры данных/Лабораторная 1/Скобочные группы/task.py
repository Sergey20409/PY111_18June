def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    ...  # TODO реализовать проверку скобочной группы
    list_ = []
    for n in brackets_row:
        if n == '(':
            list_.append(n)
        elif n == ')':
            if not list_:
                return False
            list_.pop()
    return len(list_) == 0

if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False