import typing as tp


def reformat_git_log(inp: tp.IO[str], out: tp.IO[str]) -> None:
    """Reads git log from `inp` stream, reformats it and prints to `out` stream

    Expected input format: `<sha-1>\t<date>\t<author>\t<email>\t<message>`
    Output format: `<first 7 symbols of sha-1>.....<message>`
    """
    full = inp.getvalue().strip().split("\n")
    for line in full:
        info = line.split("\t")
        sh = info[0][:7]
        message = info[-1]
        out.write(sh + '.' * (80 - len(sh) - len(message)) + message + '\n')
