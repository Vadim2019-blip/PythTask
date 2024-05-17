from typing import Iterable, Sized


class RangeIterator:
    """Итератор для класса Range"""

    def __init__(self, start: int, stop: int, step: int):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.current >= self.stop or self.step < 0 and self.current <= self.stop:
            raise StopIteration
        result = self.current
        self.current += self.step
        return result


class Range(Sized, Iterable[int]):
    """The range-like type, which represents an immutable sequence of numbers"""

    def __init__(self, *args: int) -> None:
        """
        :param args: either it's a single `stop` argument
            or sequence of `start, stop[, step]` arguments.
        If the `step` argument is omitted, it defaults to 1.
        If the `start` argument is omitted, it defaults to 0.
        If `step` is zero, ValueError is raised.
        """
        if len(args) == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
            if self.step == 0:
                raise ValueError("step cannot be zero")
        else:
            raise TypeError("Invalid number of arguments")

    def __iter__(self) -> 'RangeIterator':
        return RangeIterator(self.start, self.stop, self.step)


    def __str__(self) -> str:
        if self.step == 1:
            return f"range({self.start}, {self.stop})"
        else:
            return f"range({self.start}, {self.stop}, {self.step})"

    def __contains__(self, key: int) -> bool:
        if (key - self.start) % self.step == 0 and (
            self.step > 0 and self.start <= key < self.stop or
            self.step < 0 and self.start >= key > self.stop
        ):
            return True
        return False

    def __getitem__(self, key: int) -> int:
        if key < 0 or key >= len(self):
            raise IndexError("Index out of range")
        return self.start + key * self.step

    def __len__(self) -> int:
        if self.step > 0:
            return max(0, (self.stop - self.start + self.step - 1) // self.step)
        else:
            return max(0, (self.stop - self.start + self.step + 1) // self.step)