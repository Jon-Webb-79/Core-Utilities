# Import modules here
import sys
import os
import pytest
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


def test_create_file():
    """

    This function tests the create_file function to ensure that it
    correctly creates an ASCII based text file
    """
    util = FileUtilities()
    file = '../data/test/create_file_test.txt'
    util.create_file(file)
    assert os.path.isfile(file)
    if os.path.isfile(file):
        os.remove(file)
# ------------------------------------------------------------------------------


def test_delete_directory():
    """

    This function tests the create_file function to ensure that it
    correctly creates an ASCII based text file
    """
    util = FileUtilities()
    dir = '../data/test/test_directory'
    util.delete_directory(dir)
    assert not os.path.isdir(dir)
    if not os.path.isdir(dir):
        os.mkdir(dir)
# ------------------------------------------------------------------------------


def test_delete_file():
    """

    This function tests the delete_file function to ensure that it correctly
    deletes a file
    """
    util = FileUtilities()
    file = '../data/test/delete_test.txt'
    util.delete_file(file)
    assert not os.path.isfile(file)
    if not os.path.isfile(file):
        util.create_file(file)
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
# ------------------------------------------------------------------------------


def test_verify_directory_existence():
    """

    This function tests the FileUtilities.verify_directory_existence function to
    ensure it can correctly identify that a file does exist
    """
    util = FileUtilities()
    file = '../data/test/test_directory'
    status = util.verify_directory_existence(file)
    assert status
# ------------------------------------------------------------------------------


def test_directory_existence_not_verified():
    """

    This function tests the FileUtilities.verify_directory_existence function to
    ensure it can correctly identify that a file does exist
    """
    util = FileUtilities()
    file = '../data/test/no_directory'
    status = util.verify_directory_existence(file)
    assert not status
# ==============================================================================
# ==============================================================================
# Test ReadTextFileKeywords


def test_file_not_found():
    """

    This function ensures that the ReadTextFileKeywords class fails
    correctly when the file cannot be found
    """
    file = '../data/test/not_file_found.txt'
    with pytest.raises(SystemExit):
        ReadTextFileKeywords(file)
# ------------------------------------------------------------------------------


def test_read_double():
    """

    This function tests the ReadTextFileKeywords.read_float function to
    determine if it correctly reads in a variable as a numpy.float32
    variable.
    """
    file = '../data/test/keywords.txt'
    key = ReadTextFileKeywords(file)
    value = key.read_double('double:')
    assert isclose(value, 3.141596235941, rel_tol=1.0e-3)
    assert isinstance(value, np.float64)
# ------------------------------------------------------------------------------


def test_read_double_list():
    """

    This function tests the ReadTextFileKeywords.read_double_list
    function to determine if it can properly read a variable
    as a list of double precision values
    """
    file = '../data/test/keywords.txt'
    key = ReadTextFileKeywords(file)
    double_value = key.read_double_list('double list:')
    expected = [1.12321, 344.3454453, 21.434553]
    for i in range(len(double_value)):
        assert isclose(double_value[i], expected[i], rel_tol=1.0e-3)
        assert isinstance(double_value[i], np.float64)
# ------------------------------------------------------------------------------


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


def test_float_list():
    """

    This function tests the ReadTextFileKeywords.read_float_list
    function to determine if it can properly read a variable
    as a list of float values
    """
    file = '../data/test/keywords.txt'
    key = ReadTextFileKeywords(file)
    float_value = key.read_float_list('float list:')
    expected = [1.2, 3.4, 4.5, 5.6, 6.7]
    for i in range(len(float_value)):
        assert isclose(float_value[i], expected[i], rel_tol=1.0e-3)
        assert isinstance(float_value[i], np.float32)
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


def test_read_integer_list():
    """

    This function tests the ReadTextFileKeywords.read_float_list
    function to determine if it can properly read a variable
    as a list of float values
    """
    file = '../data/test/keywords.txt'
    key = ReadTextFileKeywords(file)
    int_value = key.read_integer_list('integer list:')
    expected = [1, 2, 3, 4, 5, 6, 7]
    for i in range(len(int_value)):
        assert isclose(int_value[i], expected[i], rel_tol=1.0e-3)
        assert isinstance(int_value[i], np.int32)
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
# ------------------------------------------------------------------------------


def test_read_string():
    """

    This function tests the ReadTextFileKeywords.read_string
    function to determine if it can properly read a variable
    as a single string
    """
    file = '../data/test/keywords.txt'
    key = ReadTextFileKeywords(file)
    sentence = key.read_string('String:')
    assert sentence == "test"
    assert isinstance(sentence, str)
# ------------------------------------------------------------------------------


def test_read_string_list():
    """

    This function tests the ReadTextFileKeywords.read_string_list
    function to determine if it can properly read a variable
    as a list of string values
    """
    file = '../data/test/keywords.txt'
    key = ReadTextFileKeywords(file)
    sentence = key.read_string_list('sentence:')
    assert sentence == ['This', 'is', 'a', 'short', 'sentence!']
    for i in sentence:
        assert isinstance(i, str)
# ==============================================================================
# ==============================================================================
# eof
