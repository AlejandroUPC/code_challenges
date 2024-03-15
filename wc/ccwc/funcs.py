import os
from io import TextIOWrapper
from functools import reduce

from .utils import _split_by_lines
def count_lines(_input: TextIOWrapper) -> int:
    """
    Given an input is able to return the count the lines using as new lines None, '', '\n', '\r' and '\r\n'. For more details check TextIOWrapper class.

    Keyword arguments:
        _input(TextIOWrapper): Input of data to have the lines counted on.

    """
    return len(_split_by_lines(_input))

def count_bytes(file_path: str) -> int:
    """
    Given a path to a file it returns the size in bytes of the given file.
    
    Keyword arguments:
        file_path(str): Path to the file to be analyzed.
    """
    return os.stat(file_path).st_size

def count_words(_input: TextIOWrapper) -> int:
    """
    Given an input is able to return the count of words using '\s' as separator.

    Keyword arguments:
         _input(TextIOWrapper): Input of data to have the words counted on.
    """
    return len(_input.read().split())

def count_characters(_input: TextIOWrapper) -> int:
    """
    Given an input is able to return the count of characters splitting every word into single characters.
    
    Keyword arguments:
         _input(TextIOWrapper): Input of data to have the characters counted on.
    """
    
    return len(_input.read()) 
