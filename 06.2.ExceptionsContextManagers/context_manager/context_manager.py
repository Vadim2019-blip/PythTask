import sys
from contextlib import contextmanager
from typing import Iterator, Optional, TextIO, Type


@contextmanager
def supresser(*types_: Type[BaseException]) -> Iterator[None]:
    try:
        yield None
    except Exception as e:
        if type(e) not in types_:
            raise e

@contextmanager
def retyper(type_from: Type[BaseException], type_to: Type[BaseException]) -> Iterator[None]:
    try:
        yield
    except Exception as e:
        if type(e) == type_from:
            new_e = type_to(e)
            new_e.args = e.args
            new_e.__traceback__ = e.__traceback__
            raise new_e
        else:
            raise e


@contextmanager
def dumper(stream: Optional[TextIO] = None) -> Iterator[None]:
    try:
        yield None
    except Exception as e:
        if stream is not None:
            stream.write(str(e))
            raise e
        if stream is None:
            stream = sys.stderr
            stream.write(str(e))
            raise e
