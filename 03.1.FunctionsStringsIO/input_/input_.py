import sys
import typing as tp


def input_(prompt: tp.Optional[str] = None,
           inp: tp.Optional[tp.IO[str]] = None,
           out: tp.Optional[tp.IO[str]] = None) -> tp.Optional[str]:
    """Read a string from `inp` stream. The trailing newline is stripped.

    The `prompt` string, if given, is printed to `out` stream without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), return None.

    `inp` and `out` arguments are optional and should default to `sys.stdin`
    and `sys.stdout` respectively.
    """
    inp = inp if inp is not None else sys.stdin
    out = out if out is not None else sys.stdout
    prompt = prompt if prompt is not None else ""

    out.write(prompt)
    out.seek(0)
    try:
        input_str = inp.readline()
        if input_str == '':
            return None
    except KeyboardInterrupt:
        return None
    input_str = input_str.rstrip("\n")

    return input_str
