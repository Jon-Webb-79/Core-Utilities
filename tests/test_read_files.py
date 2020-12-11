# Import modules here
import sys
import os
import pytest
from math import isclose
sys.path.insert(0, os.path.abspath('../src'))

from read_files import FileUtilities
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
    util.verify_file_existence(file)
# ------------------------------------------------------------------------------


def test_file_existence_not_verified():
    """

    This function tests the FileUtilities.verify_file_existence function to
    ensure that it can correctly identify when a file does not exist
    """
    util = FileUtilities()
    file = '../data/test/no_text_file.txt'
    with pytest.raises(SystemExit):
        util.verify_file_existence(file)
# ==============================================================================
# ==============================================================================
# eof
