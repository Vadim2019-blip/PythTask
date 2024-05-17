from collections import UserList
import typing as tp


# https://github.com/python/mypy/issues/5264#issuecomment-399407428
if tp.TYPE_CHECKING:
    BaseList = UserList[tp.Optional[tp.Any]]
else:
    BaseList = UserList


class ListTwist(BaseList):
    """
    List-like class with additional attributes:
        * reversed, R - return reversed list
        * first, F - insert or retrieve first element;
                     Undefined for empty list
        * last, L -  insert or retrieve last element;
                     Undefined for empty list
        * size, S -  set or retrieve size of list;
                     If size less than list length - truncate to size;
                     If size greater than list length - pad with Nones
    """
    @property
    def reversed(self):
        return list(reversed(self))
    R = reversed

    @property
    def first(self):
        return self[0] if self else None
    @first.setter
    def first(self, value):
        self[0] = value

    F = first
    @property
    def last(self):
        return self[-1]
    @last.setter
    def last(self, value):
        self[-1] = value
    L = last
    @property
    def size(self):
        return len(self)
    @size.setter
    def size(self, value):
        if value > len(self):
            for i in range(value - len(self)):
                self.append(None)
        else:
            del self[value:]
    S = size