from pathlib import Path
import subprocess

def python_sort(file_in: Path, file_out: Path) -> None:
    """
    Sort tsv file using python built-in sort
    :param file_in: tsv file to read from
    :param file_out: tsv file to write to
    """
    with open(file_in, 'r') as f_in, open(file_out, 'w') as f_out:
        lines = f_in.readlines()
        sorted_lines = sorted(lines, key=lambda x: (int(x.split()[1]), x.split()[0]))
        f_out.writelines(sorted_lines)

def util_sort(file_in: Path, file_out: Path) -> None:
    """
    Sort tsv file using sort util
    :param file_in: tsv file to read from
    :param file_out: tsv file to write to
    """
    subprocess.run(["sort", "-t", "\t", "-k2,2n", "-k1,1", "-o", file_out, file_in])
