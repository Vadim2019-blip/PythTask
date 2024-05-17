import types
import dis
from collections import Counter

def count_operations(source_code: types.CodeType) -> dict[str, int]:
    """Count byte code operations in given source code.

    :param source_code: the bytecode operation names to be extracted from
    :return: operation counts
    """
    cnt_op = Counter()
    for instr in dis.get_instructions(source_code):
        cnt_op[instr.opname] += 1
        if isinstance(instr.argval, types.CodeType):
            cnt_op.update(count_operations(instr.argval))
    return dict(cnt_op)