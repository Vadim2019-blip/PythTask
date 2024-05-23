"""
Simplified VM code which works for some cases.
You need extend/rewrite code to pass all cases.
"""

import builtins
import dis
import importlib
import types
import typing as tp
from types import FunctionType
from typing import Any
CO_VARARGS = 4
CO_VARKEYWORDS = 8

ERR_TOO_MANY_POS_ARGS = 'Too many positional arguments'
ERR_TOO_MANY_KW_ARGS = 'Too many keyword arguments'
ERR_MULT_VALUES_FOR_ARG = 'Multiple values for arguments'
ERR_MISSING_POS_ARGS = 'Missing positional arguments'
ERR_MISSING_KWONLY_ARGS = 'Missing keyword-only arguments'
ERR_POSONLY_PASSED_AS_KW = 'Positional-only argument passed as keyword argument'


def bind_args1(func: FunctionType, *args: Any, **kwargs: Any) -> dict[str, Any]:
    """Bind values from `args` and `kwargs` to corresponding arguments of `func`

        :param func: function to be inspected
        :param args: pos arguments to be bound
        :param kwargs: keyword arguments to be bound
        :return: `dict[argument_name] = argument_value` if binding was successful,
            raise TypeError with one of `ERR_*` error descriptions otherwise
    """
    pos = func.__code__.co_varnames[:func.__code__.co_argcount]

    cnt = func.__code__.co_posonlyargcount

    keyword_only_count = func.__code__.co_kwonlyargcount
    keyword_only = func.__code__.co_varnames[func.__code__.co_argcount:func.__code__.co_argcount + keyword_only_count]

    if func.__defaults__ is not None:
        has_arg = func.__defaults__
    else:
        has_arg = ()
    if func.__kwdefaults__ is not None:
        kw_has_arg = func.__kwdefaults__
    else:
        kw_has_arg = {}

    if func.__code__.co_flags & CO_VARARGS:
        star_name = func.__code__.co_varnames[func.__code__.co_argcount + keyword_only_count]
    else:
        star_name = None
    strname = None
    if func.__code__.co_flags & CO_VARKEYWORDS:
        index = func.__code__.co_argcount + keyword_only_count
        if func.__code__.co_flags & CO_VARARGS:
            index += 1
        strname = func.__code__.co_varnames[index]

    answer = {}

    star_args = []
    double_star_args = {}

    for i, arg_val in enumerate(args):
        if i < func.__code__.co_argcount:
            var = pos[i]
            answer[var] = arg_val
        elif star_name is not None:
            star_args.append(arg_val)
        elif strname is not None:
            double_star_args[arg_val] = None  # Заглушка для дальнейшего заполнения
        else:
            raise TypeError(ERR_TOO_MANY_POS_ARGS)

    if star_name is not None:
        answer[star_name] = star_args

    if strname is not None:
        answer[strname] = double_star_args

    for keyword in kwargs:
        if keyword in pos:
            if pos.index(keyword) < cnt:
                if keyword not in answer:
                    if strname is None:
                        raise TypeError(ERR_POSONLY_PASSED_AS_KW)
                    else:
                        raise TypeError(ERR_MISSING_POS_ARGS)

                if strname is None:
                    raise TypeError(ERR_POSONLY_PASSED_AS_KW)

                answer[strname][keyword] = kwargs[keyword]
                continue

        if keyword in keyword_only or keyword in pos:
            if keyword in answer:
                raise TypeError(ERR_MULT_VALUES_FOR_ARG)
            answer[keyword] = kwargs[keyword]
        elif strname is not None:
            answer[strname][keyword] = kwargs[keyword]
        else:
            raise TypeError(ERR_TOO_MANY_KW_ARGS)

    # Обработка значений по умолчанию
    for i, default_val in enumerate(reversed(has_arg)):
        arg = pos[-i - 1]
        answer[arg] = default_val if arg not in answer else answer[arg]

    for keyword in kw_has_arg:
        answer[keyword] = kw_has_arg[keyword] if keyword not in answer else answer[keyword]

    # Проверка на недостающие аргументы
    for arg in pos:
        if arg not in answer:
            raise TypeError(ERR_MISSING_POS_ARGS)

    for arg in keyword_only:
        if arg not in answer:
            raise TypeError(ERR_MISSING_KWONLY_ARGS)

    # Обработка изменяющихся позиционных аргументов
    if star_name is not None:
        answer[star_name] = tuple(answer[star_name])

    return answer

def bind_args(code: types.CodeType, defaults: tuple[tp.Any],
              kwdefaults: dict[str, tp.Any],
              *args: tp.Any,
              **kwargs: tp.Any) -> dict[str, tp.Any]:
    """Bind values from `args` and `kwargs` to corresponding arguments of `func`
    :param code: function's code
    :param args: positional arguments to be bound
    :param kwargs: keyword arguments to be bound
    :return: `dict[argument_name] = argument_value` if binding was successful,
             raise TypeError with one of `ERR_*` error descriptions otherwise
    """
    has_varargs = code.co_flags & CO_VARARGS == CO_VARARGS
    has_varkwargs = code.co_flags & CO_VARKEYWORDS == CO_VARKEYWORDS

    # Extract argument names
    arg_names = code.co_varnames[:(code.co_argcount + has_varargs + has_varkwargs + code.co_kwonlyargcount)]

    # Initialize argument names for *args and **kwargs
    varargs_name = None
    varkwargs_name = None

    # Assign *args and **kwargs names if present
    if has_varargs:
        varargs_name = code.co_varnames[(code.co_argcount + code.co_kwonlyargcount)]
    if has_varkwargs:
        varkwargs_name = code.co_varnames[(code.co_argcount + code.co_kwonlyargcount + has_varargs)]

    # Initialize result dictionary for bound arguments
    bound_args = {}

    # Bind positional arguments
    for i in range(len(args)):
        if i < code.co_argcount:
            bound_args[arg_names[i]] = args[i]
        elif varargs_name is not None:
            # If *args is present, add the argument to it
            bound_args[varargs_name] = bound_args.get(varargs_name, ()) + (args[i],)
        else:
            # Too many positional arguments
            raise TypeError(ERR_TOO_MANY_POS_ARGS)

    # Bind keyword arguments
    for kwarg_name, kwarg_value in kwargs.items():
        # Check if keyword argument is positional-only
        if kwarg_name in arg_names[:code.co_posonlyargcount]:
            if varkwargs_name is not None:
                # If **kwargs is present, add the argument to it
                bound_args[varkwargs_name][kwarg_name] = kwarg_value
            else:
                # Positional-only argument passed as keyword argument
                raise TypeError(ERR_POSONLY_PASSED_AS_KW)
        # Check if keyword argument is a regular argument
        elif kwarg_name in arg_names:
            # Check for duplicate keyword arguments
            if kwarg_name in bound_args:
                raise TypeError(ERR_MULT_VALUES_FOR_ARG)
            bound_args[kwarg_name] = kwarg_value
        # Check if keyword argument is a keyword-only argument
        else:
            if varkwargs_name is None:
                # Too many keyword arguments
                raise TypeError(ERR_TOO_MANY_KW_ARGS)
            else:
                # Add keyword-only argument to **kwargs
                bound_args[varkwargs_name][kwarg_name] = kwarg_value

    # Apply keyword-only default arguments
    if kwdefaults is not None:
        for name, value in kwdefaults.items():
            if name not in bound_args:
                bound_args[name] = value

    # Apply positional default arguments
    if defaults is not None:
        for i in range(-len(defaults), 0):
            # Check if positional default argument is not yet bound
            if arg_names[:code.co_argcount][i] not in bound_args:
                bound_args[arg_names[:code.co_argcount][i]] = defaults[i]

    # Check for missing positional arguments
    for name in arg_names[:code.co_argcount]:
        if name not in bound_args:
            raise TypeError(ERR_MISSING_POS_ARGS)

    # Check for missing keyword-only arguments
    for name in arg_names[code.co_argcount:code.co_argcount + code.co_kwonlyargcount]:
        if name not in bound_args:
            raise TypeError(ERR_MISSING_KWONLY_ARGS)

    return bound_args

class Frame:
    """
    Frame header in cpython with description
        https://github.com/python/cpython/blob/3.9/Include/frameobject.h#L17

    Text description of frame parameters
        https://docs.python.org/3/library/inspect.html?highlight=frame#types-and-members
    """

    def __init__(self,
                 frame_code: types.CodeType,
                 frame_builtins: dict[str, tp.Any],
                 frame_globals: dict[str, tp.Any],
                 frame_locals: dict[str, tp.Any]) -> None:
        self.code = frame_code
        self.builtins = frame_builtins
        self.globals = frame_globals
        self.locals = frame_locals
        self.data_stack: tp.Any = []
        self.return_value = None
        self.index: int = 0
        self.instructions = list(dis.get_instructions(self.code))

    def top(self) -> tp.Any:
        return self.data_stack[-1]

    def pop(self) -> tp.Any:
        return self.data_stack.pop()

    def push(self, *values: tp.Any) -> None:
        self.data_stack.extend(values)

    def popn(self, n: int) -> tp.Any:
        """
        Pop a number of values from the value stack.
        A list of n values is returned, the deepest value first.
        """
        if n:
            ret = self.data_stack[-n:]
            self.data_stack[-n:] = []
            return ret
        else:
            return []

    def run(self) -> tp.Any:

        while self.index < len(self.instructions):
            instruction = self.instructions[self.index]
            getattr(self, instruction.opname.lower() + "_op")(instruction.argval)
            self.index += 1

        return self.return_value

    def call_function_op(self, arg: int) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-CALL_FUNCTION

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L3496
        """
        arguments = self.popn(arg)
        f = self.pop()
        self.push(f(*arguments))

    def call_function_kw_op(self, arg_count: int) -> None:

        arg_names = self.pop()

        arg_names_count = len(arg_names)

        arg_values = self.popn(arg_names_count)

        pos_args = self.popn(arg_count - arg_names_count)

        kw_args = dict(zip(arg_names, arg_values))

        func = self.pop()

        ret_val = func(*pos_args, **kw_args)

        self.push(ret_val)

    def load_name_op(self, arg: str) -> None:
        """
        Partial realization

        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-LOAD_NAME

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L2416
        """
        # TODO: parse all scopes
        if arg not in self.locals.keys():
            self.push(self.builtins[arg])
        else:
            self.push(self.locals[arg])

    load_fast_op = load_name_op

    def load_global_op(self, arg: str) -> None:

        if arg in self.globals:
            self.push(self.globals[arg])
        elif arg in self.locals:
            self.push(self.locals[arg])
        elif arg in self.builtins:
            self.push(self.builtins[arg])



    def load_const_op(self, arg: tp.Any) -> None:
        self.push(arg)

    def load_closure_op(self, arg: str) -> None:
        self.load_name_op(arg)

    def return_value_op(self, arg: tp.Any) -> None:

        self.return_value = self.pop()
        self.index = len(list(dis.get_instructions(self.code)))

    def pop_top_op(self, arg: tp.Any) -> None:
        self.pop()

    def make_function_op(self, arg: int) -> None:
        """
                Operation description:
                    https://docs.python.org/release/3.9.7/library/dis.html#opcode-MAKE_FUNCTION

                Operation realization:
                    https://github.com/python/cpython/blob/3.9/Python/ceval.c#L3571

                Parse stack:
                    https://github.com/python/cpython/blob/3.9/Objects/call.c#L671

                Call function in cpython:
                    https://github.com/python/cpython/blob/3.9/Python/ceval.c#L4950
                """

        name = self.pop()
        code = self.pop()
        kwdefaults = {}
        if arg & 2 == 2:
            kwdefaults = self.pop()
        defaults = ((),)
        if arg & 1 == 1:
            defaults = self.pop()


        def f(*args: tp.Any, **kwargs: tp.Any) -> tp.Any:

            parsed_args: dict[str, tp.Any] = bind_args(code, defaults, kwdefaults, *args, **kwargs)

            f_globals = dict(self.globals)
            f_globals.update(self.locals)
            frame = Frame(code, self.builtins, f_globals, parsed_args)  # Run code in prepared environment
            res = frame.run()
            self.globals.update(f_globals)
            return res

        self.push(f)

    def unary_positive_op(self, arg):
        pass

    def unary_negative_op(self, arg):
        a = self.pop()
        self.push(-a)

    def unary_not_op(self, arg):
        a = self.pop()
        self.push(not a)

    def unary_invert_op(self, arg):
        a = self.pop()
        self.push(~a)

    def dup_top_two_op(self, arg: tp.Any) -> None:
        self.push(self.top(), self.data_stack[-2])

    def dup_top_op(self, arg: tp.Any) -> None:
        self.push(self.top())

    def rot_two_op(self, arg: tp.Any) -> None:
        st2, st1 = self.popn(2)
        self.push(st1, st2)

    def rot_three_op(self, arg: tp.Any) -> None:
        st3, st2, st1 = self.popn(3)
        self.push(st1, st3, st2)

    def rot_four_op(self, arg: tp.Any) -> None:
        st4, st3, st2, st1 = self.popn(4)
        self.push(st1, st4, st3, st2)

    def store_name_op(self, arg: str) -> None:
        self.locals[arg] = self.pop()

    def store_fast_op(self, arg: tp.Any) -> None:
        self.locals[arg] = self.pop()

    def delete_fast_op(self, arg):
        self.load_name_op(arg)
        a = self.pop()
        del a

    def load_attr_op(self, arg: str) -> None:
        self.push(getattr(self.pop(), arg))

    def store_attr_op(self, arg: str) -> None:
        second = self.pop()
        value = self.pop()
        if second is not None:
            if arg:
                setattr(second, arg, value)
            else:
                raise ValueError
        else:
            raise TypeError

    def delete_attr_op(self, arg: str) -> None:
        second = self.pop()
        if second is not None:
            if arg:
                delattr(second, arg)
            else:
                raise ValueError
        else:
            raise TypeError

    def extended_arg_op(self, arg: tp.Any) -> None:
        pass

    def jump_forward_op(self, arg: tp.Any) -> None:
        self.index = arg // 2 - 1

    def jump_absolute_op(self, arg: tp.Any) -> None:
        self.index = arg // 2 - 1

    def pop_jump_if_false_op(self, arg: tp.Any) -> None:
        if not self.pop():
            self.jump_absolute_op(arg)

    def pop_jump_if_true_op(self, arg: tp.Any) -> None:
        if self.pop():
            self.jump_absolute_op(arg)

    def jump_if_true_or_pop_op(self, arg: tp.Any) -> None:
        indexis = self.top()
        if indexis:
            self.jump_absolute_op(arg)
        else:
            self.pop()

    def jump_if_false_or_pop_op(self, arg: tp.Any) -> None:
        if not self.top():
            self.jump_absolute_op(arg)
        else:
            self.pop()

    def jump_if_not_exc_match_op(self, arg: tp.Any) -> None:
        top_value = self.top()
        second_from_top = self.data_stack[-2]
        if not isinstance(second_from_top, Exception):
            self.jump_absolute_op(arg)
            self.pop()
            self.pop()

    def unpack_sequence_op(self, arg: int) -> None:
        seq = self.pop()
        for i in reversed(range(arg)):
            self.push(seq[i])

    def build_tuple_op(self, arg: int) -> None:
        self.push(tuple(self.popn(arg)))

    def build_set_unpack_op(self, arg):
        self.push(set().union(*self.popn(arg)))

    def build_list_op(self, arg: int) -> None:
        self.push(list(self.popn(arg)))

    def build_set_op(self, arg: int) -> None:
        self.push(set(self.popn(arg)))

    def build_map_op(self, arg: int) -> None:
        # items = self.popn(2 * arg)
        # map_ = {}
        # for i in range(0, len(items), 2):
        #     map_[items[i]] = items[i + 1]
        # self.push(map_)
        # self.push(self.data_stack[-1])
        # self.push(self.data_stack[-1])
        # self.push(self.data_stack[-1])
        # self.push(self.data_stack[-1])
        self.push({k: v for k, v in zip(*[iter(self.popn(2 * arg))] * 2)})

    def build_const_key_map_op(self, arg: int) -> None:
        key = self.pop()
        values = self.popn(arg)
        map_ = {}
        for i in range(len(values)):
            map_[key[i]] = values[i]
        self.push(map_)
    def format_value_op(self, arg: tp.Any) -> None:
        pass

    def build_string_op(self, arg):
        self.push("".join(self.popn(arg)))

    def list_to_tuple_op(self, arg: int) -> None:
        self.push(tuple(self.pop()))

    def set_update_op(self, arg: tp.Any) -> None:
        target_set = self.pop()
        update_set = self.pop()
        for item in target_set:
            update_set.add(item)
        self.push(update_set)

    def list_extend_op(self, arg: tp.Any) -> None:
        first = self.pop()
        second = self.pop()
        for item in first:
            second.append(item)
        self.push(second)

    def dict_update_op(self, arg: tp.Any) -> None:
        first, second = self.popn(2)
        dict.update(first, second)
        self.push(first)

    def dict_merge_op(self, arg: tp.Any) -> None:
        base_dict = self.pop()
        merge_dict = self.pop()
        for key, value in merge_dict.items():
            if key not in base_dict:
                base_dict[key] = value
        self.push(base_dict)

    def load_method_op(self, arg: str) -> None:
        item = self.pop()
        try:
            self.push(getattr(item, arg))
        except AttributeError:
            self.push(ValueError(f"Attribute '{arg}' not found on object {item}"))

    def call_method_op(self, arg):
        args = self.popn(arg)
        callable_obj = self.pop()

        if isinstance(callable_obj, str):
            second = self.pop()
            self.push(getattr(second, callable_obj)(*args))
        else:
            self.push(callable_obj(*args))

    def get_iter_op(self, arg):
        a = self.pop()
        self.push(iter(a))


    def build_map_unpack_op(self, arg):
        items = self.popn(arg)
        res = {}
        for item in items:
            if not isinstance(item, dict):
                raise TypeError(f"Expected a dictionary, got {type(item)}")
            res.update(item)
        self.push(res)

    def build_slice_op(self, arg: int) -> None:
        self.push(slice(*self.popn(arg)))

    def store_subscr_op(self, arg: tp.Any) -> None:
        first, second, indexis = self.popn(3) 
        second.__setitem__(indexis, first)
        self.push(second)
    def setup_loop_op(self, arg):
        pass

    def set_add_op(self, arg: int) -> None:
        element = self.pop()
        set_to_modify = self.data_stack[-arg]
        set_to_modify.add(element)
        self.push(set_to_modify)

    def map_add_op(self, arg):
        a = self.pop()
        b = self.pop()
        dict.__setitem__(self.data_stack[-arg], a, b)

    def list_append_op(self, arg: int) -> None:
        element = self.pop()
        list_to_modify = self.data_stack[-arg]
        list_to_modify.append(element)
        self.push(list_to_modify)

    def delete_subscr_op(self, arg: tp.Any) -> None:
        sequence, index = self.popn(2)
        del sequence[index]
        self.push(sequence)

    def raise_varargs_op(self, arg: int) -> None:
        if arg == 1:
            raise self.pop()

    def compare_op_op(self, arg):
        b = self.pop()
        a = self.pop()
        if arg == "==":
            self.push(a == b)
        elif arg == "<=":
            self.push(a <= b)
        elif arg == ">=":
            self.push(a >= b)
        elif arg == "in":
            self.push(a in b)
        elif arg == "not in":
            self.push(a not in b)
        elif arg == "<":
            self.push(a < b)
        elif arg == ">":
            self.push(a > b)
        elif arg == "!=":
            self.push(a != b)


    def is_op_op(self, arg: int) -> None:
        x, y = self.popn(2)
        if arg:
            self.push(x is not y)
        else:
            self.push(x is y)

    def contains_op_op(self, arg: int) -> None:
        x, y = self.popn(2)
        if arg:
            self.push(x not in y)
        else:
            self.push(x in y)

    def binary_op(self, op: str) -> None:
        x, y = self.popn(2)
        if op == '+':
            self.push(x + y)
        elif op == '*':
            self.push(x * y)
        elif op == '-':
            self.push(x - y)
        elif op == '/':
            self.push(x / y)
        elif op == '//':
            self.push(x // y)
        elif op == 'and':
            self.push(x & y)
        elif op == 'or':
            self.push(x | y)
        elif op == '**':
            self.push(x ** y)
        elif op == '@':
            self.push(x @ y)
        elif op == '%':
            self.push(x % y)
        elif op == '[]':
            self.push(x[y])
        elif op == '<<':
            self.push(x << y)
        elif op == '>>':
            self.push(x >> y)
        elif op == '^':
            self.push(x ^ y)

    def binary_add_op(self, arg: tp.Any) -> None:
        self.binary_op('+')

    def binary_subtract_op(self, arg: tp.Any) -> None:
        self.binary_op('-')

    def binary_multiply_op(self, arg: tp.Any) -> None:
        self.binary_op('*')

    def binary_true_divide_op(self, arg: tp.Any) -> None:
        self.binary_op('/')

    def binary_power_op(self, arg: tp.Any) -> None:
        self.binary_op('**')

    def binary_floor_divide_op(self, arg: tp.Any) -> None:
        self.binary_op('//')

    def binary_modulo_op(self, arg: tp.Any) -> None:
        self.binary_op('%')

    def binary_and_op(self, arg: tp.Any) -> None:
        self.binary_op('and')

    def binary_or_op(self, arg: tp.Any) -> None:
        self.binary_op('or')

    def binary_xor_op(self, arg: tp.Any) -> None:
        self.binary_op('^')

    def binary_matrix_multiply_op(self, arg: tp.Any) -> None:
        self.binary_op('@')

    def binary_subscr_op(self, arg: tp.Any) -> None:
        self.binary_op('[]')

    def binary_lshift_op(self, arg: tp.Any) -> None:
        self.binary_op('<<')

    def binary_rshift_op(self, arg: tp.Any) -> None:
        self.binary_op('>>')
    def inplace_add_op(self, arg) -> None:
        right = self.pop()
        left = self.pop()
        self.push(left + right)

    def inplace_power_op(self, arg):
        a = self.pop()
        b = self.pop()
        self.push(b ** a)

    def inplace_multiply_op(self, arg):
        a = self.pop()
        b = self.pop()
        self.push(a * b)

    def inplace_floor_divide_op(self, arg):
        b = self.pop()
        a = self.pop()
        self.push(a // b)

    def inplace_modulo_op(self, arg):
        b = self.pop()
        a = self.pop()
        self.push(a % b)

    def inplace_subtract_op(self, arg):
        b = self.pop()
        a = self.pop()
        self.push(a - b)


    def inplace_lshift_op(self, arg):
        b = self.pop()
        a = self.pop()
        self.push(a << b)

    def inplace_rshift_op(self, arg):
        b = self.pop()
        a = self.pop()
        self.push(a >> b)

    def inplace_and_op(self, arg):
        b = self.pop()
        a = self.pop()
        self.push(a & b)

    def inplace_or_op(self, arg):
        b = self.pop()
        a = self.pop()
        self.push(a | b)

    def inplace_xor_op(self, arg):
        b = self.pop()
        a = self.pop()
        self.push(a ^ b)

    def inplace_true_divide_op(self, arg):
        b = self.pop()
        a = self.pop()
        self.push(a / b)


class VirtualMachine:
    def run(self, code_obj: types.CodeType) -> None:
        """
        :param code_obj: code for interpreting
        """
        globals_context: dict[str, tp.Any] = {}
        frame = Frame(code_obj, builtins.globals()['__builtins__'], globals_context, globals_context)
        return frame.run()