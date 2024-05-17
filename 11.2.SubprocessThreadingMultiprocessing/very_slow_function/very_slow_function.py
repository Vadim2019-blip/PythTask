import time
import typing as tp
from multiprocessing import Pool
from threading import Thread


def very_slow_function(x: int) -> int:
    """Function which calculates square of given number really slowly
    :param x: given number
    :return: number ** 2
    """
    time.sleep(0.3)
    return x ** 2


def calc_squares_simple(bound: int) -> tp.List[int]:
    """Function that calculates squares of numbers in range [0; bound)
    :param bound: positive upper bound for range
    :return: list of squared numbers
    """
    return [very_slow_function(x) for x in range(bound)]


def calc_squares_multithreading(bound: int) -> tp.List[int]:
    """Function that calculates squares of numbers in range [0; bound) using threading.Thread
    :param bound: positive upper bound for range
    :return: list of squared numbers
    """
    results = []
    threads = []
    for i in range(bound):
        thread = Thread(target=lambda x: results.append(very_slow_function(x)), args=(i,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return results


def calc_squares_multiprocessing(bound: int) -> tp.List[int]:
    """Function that calculates squares of numbers in range [0; bound) using multiprocessing.Pool
    :param bound: positive upper bound for range
    :return: list of squared numbers
    """
    with Pool() as pool:
        results = pool.map(very_slow_function, range(bound))
    return results
