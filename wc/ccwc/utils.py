from typing import List
from io import TextIOWrapper

def _split_by_lines(_input: TextIOWrapper) -> List[str]:
    """
    Given an input is able to split it by lines.

    Keyword arguments:
        _input(TextIOWrapper): Data to be split into lines.
    """
    return _input.readlines()
