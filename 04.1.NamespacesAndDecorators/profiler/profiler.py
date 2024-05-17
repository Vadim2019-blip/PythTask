import time
def profiler(func):  # type: ignore
    """
    Returns profiling decorator, which counts calls of function
    and measure last function execution time.
    Results are stored as function attributes: `calls`, `last_time_taken`
    :param func: function to decorate
    :return: decorator, which wraps any function passed
    """

    def wraps(*args, **kwargs):
        start_time = time.time()
        if hasattr(wraps, 'calls_counter') == False:
            wraps.calls_counter = 0
        start_calls = wraps.calls_counter
        result = func(*args, **kwargs)
        end_time = time.time()
        wraps.last_time_taken = end_time - start_time
        wraps.calls_counter += 1
        wraps.calls = wraps.calls_counter - start_calls
        return result
    wraps.__name__ = func.__name__
    wraps.__doc__ = func.__doc__
    wraps.__module__ = func.__module__
    return wraps