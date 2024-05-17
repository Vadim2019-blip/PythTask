import time
from contextlib import contextmanager


class TimeoutException(Exception):
    """Базовое исключение таймаута."""
    pass


class SoftTimeoutException(TimeoutException):
    """Исключение превышения мягкого таймаута."""
    pass


class HardTimeoutException(TimeoutException):
    """Исключение превышения жесткого таймаута."""
    pass


class TimeCatcher:
    """Контекстный менеджер для измерения времени выполнения кода."""

    def __init__(self, soft_timeout=None, hard_timeout=None):
        if soft_timeout is not None and soft_timeout < 0:
            raise AssertionError("soft_timeout должен быть неотрицательным")
        if hard_timeout is not None and hard_timeout < 0:
            raise AssertionError("hard_timeout должен быть неотрицательным")

        self.soft_timeout = soft_timeout
        self.hard_timeout = hard_timeout
        self.start_time = None
        self.elapsed_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time = float(time.time() - self.start_time)

        if self.soft_timeout is not None and self.elapsed_time > self.soft_timeout:
            raise SoftTimeoutException(f"Превышен мягкий таймаут ({self.soft_timeout} сек)")

        if self.hard_timeout is not None and self.hard_timeout > 0 and self.elapsed_time > self.hard_timeout:
            raise HardTimeoutException(f"Превышен жесткий таймаут ({self.hard_timeout} сек)")

        return False

    def __float__(self):
        return self.elapsed_time if self.elapsed_time is not None else 0.0

    def __str__(self):
        return f"Time consumed: {self.elapsed_time:.4f}"
