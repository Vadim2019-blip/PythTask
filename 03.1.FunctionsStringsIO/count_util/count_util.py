import typing as tp


def count_util(text: str, flags: tp.Optional[str] = None) -> dict[str, int]:
    """
    :param text: text to count entities
    :param flags: flags in command-like format - can be:
        * -m stands for counting characters
        * -l stands for counting lines
        * -L stands for getting length of the longest line
        * -w stands for counting words
    More than one flag can be passed at the same time, for example:
        * "-l -m"
        * "-lLw"
    Ommiting flags or passing empty string is equivalent to "-mlLw"
    :return: mapping from string keys to corresponding counter, where
    keys are selected according to the received flags:
        * "chars" - amount of characters
        * "lines" - amount of lines
        * "longest_line" - the longest line length
        * "words" - amount of words
    """
    lines = text.split('\n') if text and text[-1] != "\n" else text.split('\n')[:-1]
    answer = dict()
    counter = len(lines)
    if (flags is None) or (flags == '') or ('m' in flags):
        answer['chars'] = counter + sum(map(len, lines))
        if text and not (text[-1] == "\n"):
            answer['chars'] -= 1
    if (flags is None) or (flags == '') or ('l' in flags):
        answer['lines'] = counter - 1 if text and not (text[-1] == "\n") else counter

    if (flags is None) or (flags == '') or ('w' in flags):
        answer['words'] = sum(len(it.split()) for it in lines) if lines else 0

    if (flags is None) or (flags == '') or ('L' in flags):
        answer['longest_line'] = max([len(x) for x in lines]) if lines else 0

    return answer
