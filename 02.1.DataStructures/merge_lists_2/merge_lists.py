import typing as tp
import itertools
import heapq

def merge(seq: tp.Sequence[tp.Sequence[int]]) -> list[int]:
    """
    :param seq: sequence of sorted sequences
    :return: merged sorted list
    """
    merged = list(heapq.merge(*seq))
    return merged
