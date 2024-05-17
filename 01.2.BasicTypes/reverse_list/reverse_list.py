def reverse_iterative(lst: list[int]) -> list[int]:
    """
    Return reversed list. You can use only iteration
    :param lst: input list
    :return: reversed list
    """
    ans = []
    for i in range(len(lst)):
        ans.append(lst[len(lst) - i - 1])
    return ans


def reverse_inplace_iterative(lst: list[int]) -> None:
    """
    Revert list inplace. You can use only iteration
    :param lst: input list
    :return: None
    """
    lenght = len(lst)
    for i in range(lenght // 2):
        lst[i], lst[lenght - 1 - i] = lst[lenght - 1 - i], lst[i]



def reverse_inplace(lst: list[int]) -> None:
    """
    Revert list inplace with reverse method
    :param lst: input list
    :return: None
    """
    return lst.reverse()


def reverse_reversed(lst: list[int]) -> list[int]:
    """
    Revert list with `reversed`
    :param lst: input list
    :return: reversed list
    """
    answ = list(reversed(lst))
    return answ


def reverse_slice(lst: list[int]) -> list[int]:
    """
    Revert list with slicing
    :param lst: input list
    :return: reversed list
    """
    answ = lst[::-1]
    return answ
