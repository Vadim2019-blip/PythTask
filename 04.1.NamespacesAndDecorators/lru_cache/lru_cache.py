

from typing_extensions import Unpack

from typing import Callable, Any, TypeVar
from collections import OrderedDict

Function = TypeVar('Function', bound=Callable[..., Any])


def cache(max_size: int) -> Callable[[Function], Function]:
    """
    Returns decorator, which stores result of function
    for `max_size` most recent function arguments.
    :param max_size: max amount of unique arguments to store values for
    :return: decorator, which wraps any function passed
    """
    def decorator(func: Function) -> Function:
        cache = OrderedDict()

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (args, tuple(sorted(kwargs.items())))
            if key in cache:
                return cache[key]

            result = func(*args, **kwargs)
            if len(cache) >= max_size:
                cache.popitem(last=False)
            cache[key] = result
            return result

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.__module__ = func.__module__
        return wrapper

    return decorator
