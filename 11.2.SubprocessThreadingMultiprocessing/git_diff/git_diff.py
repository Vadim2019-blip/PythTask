import subprocess
from pathlib import Path

def get_changed_files(git_path, from_commit_hash, to_commit_hash):

    git_command = f'git --git-dir="{git_path}/.git" diff --name-only {from_commit_hash} {to_commit_hash}'

    output = subprocess.check_output(git_command, shell=True, cwd=git_path).decode('utf-8')

    changed_files = [Path(git_path).joinpath(file) for file in output.strip().split('\n')]

    return changed_files

def get_changed_dirs(git_path, from_commit_hash, to_commit_hash):
    """
    Get directories which content was changed between two specified commits
    :param git_path: path to git repo directory
    :param from_commit_hash: hash of commit to do diff from
    :param to_commit_hash: hash of commit to do diff to
    :return: sequence of changed directories between specified commits
    """


    changed_files = get_changed_files(git_path, from_commit_hash, to_commit_hash)
    changed_dirs = {file.parent for file in changed_files}

    return changed_dirs
