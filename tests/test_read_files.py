# Import modules here
import sys
import os
import numpy as np
from math import isclose
sys.path.insert(0, os.path.abspath('../src'))

from read_files import FileUtilities, ReadTextFileKeywords
# ==============================================================================
# ==============================================================================
# Date:    December 11, 2020
# Purpose: This code contains functions that test the functions and classes
#          in the read_files.py file

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2020, Jon Webb Inc."
__version__ = "1.0"
# ==============================================================================
# ==============================================================================
# Test OSUtilities class


def test_count_word_occurrence():
    """

    This function tests the FileUtilities.count_occurrence_of_words_in_file
    to ensure it correctly determines the number of times a word occurs in
    a file
    """
    util = FileUtilities()
    file = '../data/test/text_file.txt'
    num_words = util.count_occurrence_of_word_in_file(file, 'file')
    assert num_words == 4
# ------------------------------------------------------------------------------


def test_determine_file_size():
    """

    This function tests the FileUtilities.determine_file_size function to determine
    if it can correctly determine the size of a file
    """
    util = FileUtilities()
    file = '../data/test/size_test.jpg'
    file_size = util.determine_file_size(file)
    assert isclose(file_size, 26674.009, rel_tol=1.0e-3)
# ------------------------------------------------------------------------------


def test_determine_file_line_count():
    """

    This function tests teh FileUtilities.file_line_count function to ensure
    it can correctly determine how many lines are in a file
    """
    util = FileUtilities()
    file = '../data/test/text_file.txt'
    lines = util.file_line_count(file)
    assert lines == 4
# ------------------------------------------------------------------------------


def test_file_word_count():
    """

    This function tests the FileUtilities.file_word_count function to determine
    if it can correctly determine the number of words in a file
    """
    util = FileUtilities()
    file = '../data/test/text_file.txt'
    words = util.file_word_count(file)
    assert words == 21
# ------------------------------------------------------------------------------


def test_current_working_directory():
    """

    This function tests the FileUtilities.get_current_working_directory
    function to ensure that it can correctly identify the current working
    directory
    """
    util = FileUtilities()
    cwd = util.current_working_directory()
    answer = os.getcwd()
    assert cwd == answer
# ------------------------------------------------------------------------------


def test_verify_file_existence():
    """

    This function tests the FileUtilities.verify_file_existence function to
    ensure it can correctly identify that a file does exist
    """
    util = FileUtilities()
    file = '../data/test/text_file.txt'
    status = util.verify_file_existence(file)
    assert status
# ------------------------------------------------------------------------------


def test_file_existence_not_verified():
    """

    This function tests the FileUtilities.verify_file_existence function to
    ensure that it can correctly identify when a file does not exist
    """
    util = FileUtilities()
    file = '../data/test/no_text_file.txt'
    status = util.verify_file_existence(file)
    assert not status
# ==============================================================================
# ==============================================================================
# Test ReadTextFileKeywords


def test_read_float():
    """

    This function tests the ReadTextFileKeywords.read_float function to
    determine if it correctly reads in a variable as a numpy.float32
    variable.
    """
    file = '../data/test/keywords.txt'
    key = ReadTextFileKeywords(file)
    value = key.read_float('float:')
    assert isclose(value, 3.1415, rel_tol=1.0e-3)
    assert isinstance(value, np.float32)
# ------------------------------------------------------------------------------


def test_read_integer():
    """

    This function tests the ReadTextFileKeywords.read_float function to
    determine if it correctly reads in a variable as a numpy.int32
    variable.
    """
    file = '../data/test/keywords.txt'
    key = ReadTextFileKeywords(file)
    value = key.read_integer('Integer Value:')
    assert value == 3
    assert isinstance(value, np.int32)
# ------------------------------------------------------------------------------


def test_read_sentence():
    """

    This function tests the ReadTextFileKeywords.read_sentence
    function to determine if it can properly read a sentence as
    a string
    """
    file = '../data/test/keywords.txt'
    key = ReadTextFileKeywords(file)
    sentence = key.read_sentence('sentence:')
    assert sentence == "This is a short sentence!"
    assert isinstance(sentence, str)
# ==============================================================================
# ==============================================================================
# eof
