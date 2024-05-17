from types import FunctionType
from typing import Any
import collections
CO_VARARGS = 4
CO_VARKEYWORDS = 8

ERR_TOO_MANY_POS_ARGS = 'Too many pos arguments'
ERR_TOO_MANY_KW_ARGS = 'Too many keyword arguments'
ERR_MULT_VALUES_FOR_ARG = 'Multiple values for arguments'
ERR_MISSING_POS_ARGS = 'Missing pos arguments'
ERR_MISSING_KWONLY_ARGS = 'Missing keyword-only arguments'
ERR_POSONLY_PASSED_AS_KW = 'Positional-only argument passed as keyword argument'


def bind_args(func: FunctionType, *args: Any, **kwargs: Any) -> dict[str, Any]:
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