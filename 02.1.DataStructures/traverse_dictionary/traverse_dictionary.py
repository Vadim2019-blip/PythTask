import typing as tp
from queue import Queue

def traverse_dictionary_immutable(
        dct: tp.Mapping[str, tp.Any],
        prefix: str = "") -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param prefix: prefix for key used for passing total path through recursion
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    result = []
    for k in dct:
        if type(dct[k]) == dict:
            result += traverse_dictionary_immutable(dct[k], prefix + k + '.')
        else:
            result.append((prefix + k, dct[k]))
    return result

def traverse_dictionary_mutable(
        dct: tp.Mapping[str, tp.Any],
        result: list[tuple[str, int]],
        prefix: str = "") -> None:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param result: list with pairs: (full key from root to leaf joined by ".", value)
    :param prefix: prefix for key used for passing total path through recursion
    :return: None
    """
    for k in dct:
        tp = type(dct[k])
        if tp == dict:
            traverse_dictionary_mutable(dct[k], result, prefix + k + '.')
        else:
            result.append((prefix + k, dct[k]))


def traverse_dictionary_iterative(
        dct: tp.Mapping[str, tp.Any]
        ) -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    result = []
    q = Queue()
    q.put((dct, ''))
    while q.qsize() > 0:
        current = q.get()
        start, prefix = current[0], current[1]
        for k in start:
            tp = type(start[k])
            if tp == dict:
                q.put((start[k], prefix + k + "."))
            else:
                start1 = prefix + k
                result.append((start1, start[k]))
    return result