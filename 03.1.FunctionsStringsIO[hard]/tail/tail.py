import sys
import typing as tp
from pathlib import Path


def tail(filename: Path, lines_amount: int = 10, output: tp.Optional[tp.IO[bytes]] = None) -> None:
    """
    :param filename: file to read lines from (the file can be very large)
    :param lines_amount: number of lines to read
    :param output: stream to write requested amount of last lines from file
                   (if nothing specified stdout will be used)
    """
    if output is None:
        output = sys.stdout

    with open(filename, 'rb') as f:
        f.seek(0, 2)  # Переместить курсор в конец файла
        file_size = f.tell()

        block_size = 4096
        current_position = file_size
        lines = []
        while len(lines) < lines_amount:
            current_position -= block_size
            if current_position < 0:
                current_position = 0
            f.seek(current_position)
            block = f.read(block_size)
            new_lines = block.splitlines(True)
            if len(lines) + len(new_lines) > lines_amount:
                lines = new_lines[-lines_amount:]
            else:
                lines.extend(new_lines)

    output.writelines(lines)