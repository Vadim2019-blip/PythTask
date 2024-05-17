import typing as tp
import ctypes as sctructer
import struct

LONG_LEN = 8
INT_LEN = 4
CHAR_LEN = 1

ULONG_CHAR = "L" if sctructer.sizeof(sctructer.c_ulong) == 8 else "I"
LONG_CHAR = "l" if sctructer.sizeof(sctructer.c_long) == 8 else "i"

struct_unpack = sctructer.cast
struct_object = sctructer.py_object
def get_object_by_id(object_id: int) -> tp.Union[int, float, tuple, list, str, bool]:
    """
    Restores object by id.
    :param object_id: Object Id.
    :return: An object that corresponds to object_id.
    """
    ptr = struct_unpack(object_id, struct_object)
    return ptr.value

