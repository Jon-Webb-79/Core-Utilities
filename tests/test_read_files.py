# Import modules here
import sys
import os
import pytest
import numpy as np
import shutil
from math import isclose
sys.path.insert(0, os.path.abspath('../src'))

from operating_system import OSUtilities, ReadTextFileKeywords
# ==============================================================================
# ==============================================================================
# Date:    December 11, 2020
# Purpose: This code contains functions that test the functions and classes
#          in the operating_system.py file

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2020, Jon Webb Inc."
__version__ = "1.0"
# ==============================================================================
# ==============================================================================
# Test OSUtilities class


def test_change_directory():
    """

    This function tests the ability of OSUtilities.change_directory to properly
    change a directory
    """
    current = os.getcwd()
    new = current[:-6]
    util = OSUtilities()
    util.change_directory("../")
    assert new == os.getcwd()
    util.change_directory("tests")

# ------------------------------------------------------------------------------


def test_copy_directory():
    """

    This function tests the ability of the OSUtilitiescopy_directory function to
    copy a directory
    """
    util = OSUtilities()
    directory1 = '../data/test/test_directory2'
    directory2 = '../data/test/test_directory3'
    file = '../data/test/test_directory3/test.txt'
    util.copy_directory(directory1, directory2)
    assert os.path.isdir(directory2)
    assert os.path.isfile(file)
    if os.path.isdir(directory2):
        shutil.rmtree(directory2)
# ------------------------------------------------------------------------------


def test_copy_file():
    """

    This function tests the ability of the OSUtilities.copy_file function to correctly
    copy a file
    """
    util = OSUtilities()
    file1 = '../data/test/test_file2.txt'
    file2 = '../data/test/copy_test.txt'
    util.copy_file(file1, file2)
    assert os.path.isfile(file2)
    if os.path.isfile(file2):
        os.remove(file2)
# ------------------------------------------------------------------------------


def test_count_word_occurrence():
    """

    This function tests the OSUtilities.count_occurrence_of_words_in_file
    to ensure it correctly determines the number of times a word occurs in
    a file
    """
    util = OSUtilities()
    file = '../data/test/text_file.txt'
    num_words = util.count_occurrence_of_word_in_file(file, 'file')
    assert num_words == 4
# ------------------------------------------------------------------------------


def test_create_directory():
    """

    This function tests the OSUtilitiescreate_directory command to ensure it correctly
    creates a directory
    """
    util = OSUtilities()
    directory = '../data/test/test_directory3'
    util.create_directory(directory)
    assert os.path.isdir(directory)
    if os.path.isdir(directory):
        os.rmdir(directory)
# ------------------------------------------------------------------------------


def test_create_file():
    """

    This function tests the OSUtilitiescreate_file function to ensure that it
    correctly creates an ASCII based text file
    """
    util = OSUtilities()
    file = '../data/test/create_file_test.txt'
    util.create_file(file)
    assert os.path.isfile(file)
    if os.path.isfile(file):
        os.remove(file)
# ------------------------------------------------------------------------------


def test_delete_directory():
    """

    This function tests the OSUtilitiescreate_file function to ensure that it
    correctly creates an ASCII based text file
    """
    util = OSUtilities()
    dire = '../data/test/test_directory'
    util.delete_directory(dire)
    assert not os.path.isdir(dire)
    if not os.path.isdir(dire):
        os.mkdir(dire)
# ------------------------------------------------------------------------------


def test_delete_file():
    """

    This function tests the OSUtilities.delete_file function to ensure that it correctly
    deletes a file
    """
    util = OSUtilities()
    file = '../data/test/delete_test.txt'
    util.delete_file(file)
    assert not os.path.isfile(file)
    if not os.path.isfile(file):
        util.create_file(file)
# ------------------------------------------------------------------------------


def test_remove_populated_directory():
    """

    This function tests the OSUtilities.remove_populated_directory function to determine
    if it correctly removes a populated directory
    """
    util = OSUtilities()
    directory = '../data/test/populated_dir1'
    file = '../data/test/populated_dir1/test.txt'
    util.delete_populated_directory(directory)
    assert not os.path.isdir(directory)
    if not os.path.isdir(directory):
        os.mkdir(directory)
        util.create_file(file)
# ------------------------------------------------------------------------------


def test_determine_file_size():
    """

    This function tests the OSUtilities.determine_file_size function to determine
    if it can correctly determine the size of a file
    """
    util = OSUtilities()
    file = '../data/test/size_test.jpg'
    file_size = util.determine_file_size(file)
    assert isclose(file_size, 26674.009, rel_tol=1.0e-3)
# ------------------------------------------------------------------------------


def test_determine_file_line_count():
    """

    This function tests the OSUtilities.file_line_count function to ensure
    it can correctly determine how many lines are in a file
    """
    util = OSUtilities()
    file = '../data/test/text_file.txt'
    lines = util.file_line_count(file)
    assert lines == 4
# ------------------------------------------------------------------------------


def test_file_word_count():
    """

    This function tests the OSUtilities.file_word_count function to determine
    if it can correctly determine the number of words in a file
    """
    util = OSUtilities()
    file = '../data/test/text_file.txt'
    words = util.file_word_count(file)
    assert words == 21
# ------------------------------------------------------------------------------


def test_current_working_directory():
    """

    This function tests the OSUtilities.get_current_working_directory
    function to ensure that it can correctly identify the current working
    directory
    """
    util = OSUtilities()
    cwd = util.current_working_directory()
    answer = os.getcwd()
    assert cwd == answer
# ------------------------------------------------------------------------------


def test_copy_files_everything():
    """

    This function tests the OSUtilities.copy_files function to ensure that it
    correctly copies all contents of a directory to a new directory
    """
    source = '../data/test/move_directory3'
    destination = '../data/test/move_directory2'
    util = OSUtilities()
    util.copy_files(destination, source)
    assert os.path.isfile('../data/test/move_directory2/test1.txt')
    assert os.path.isfile('../data/test/move_directory2/test2.txt')
    assert os.path.isdir('../data/test/move_directory2/test')
    shutil.rmtree('../data/test/move_directory2/test')
    os.remove('../data/test/move_directory2/test1.txt')
    os.remove('../data/test/move_directory2/test2.txt')
# ------------------------------------------------------------------------------


def test_copy_files_files():
    """

    This function tests the OSUtilities.copy_files function to ensure that it
    correctly copies text file contents of a directory to a new directory
    """
    source = '../data/test/move_directory3'
    destination = '../data/test/move_directory2'
    util = OSUtilities()
    util.copy_files(destination, source, '.txt')
    assert os.path.isfile('../data/test/move_directory2/test1.txt')
    assert os.path.isfile('../data/test/move_directory2/test2.txt')
    os.remove('../data/test/move_directory2/test1.txt')
    os.remove('../data/test/move_directory2/test2.txt')
# ------------------------------------------------------------------------------


def test_copy_files_dirs():
    """

    This function tests the OSUtilities.copy_files function to ensure that it
    correctly copies all directories of a directory to a new directory
    """
    source = '../data/test/move_directory3'
    destination = '../data/test/move_directory2'
    util = OSUtilities()
    util.copy_files(destination, source, dirs=True)
    assert os.path.isdir('../data/test/move_directory2/test')
    shutil.rmtree('../data/test/move_directory2/test')
# ------------------------------------------------------------------------------


def test_verify_file_existence():
    """

    This function tests the OSUtilities.verify_file_existence function to
    ensure it can correctly identify that a file does exist
    """
    util = OSUtilities()
    file = '../data/test/text_file.txt'
    status = util.verify_file_existence(file)
    assert status
# ------------------------------------------------------------------------------


def test_file_existence_not_verified():
    """

    This function tests the OSUtilities.verify_file_existence function to
    ensure that it can correctly identify when a file does not exist
    """
    util = OSUtilities()
    file = '../data/test/no_text_file.txt'
    status = util.verify_file_existence(file)
    assert not status
# ------------------------------------------------------------------------------


def test_verify_directory_existence():
    """

    This function tests the OSUtilities.verify_directory_existence function to
    ensure it can correctly identify that a file does exist
    """
    util = OSUtilities()
    file = '../data/test/test_directory'
    status = util.verify_directory_existence(file)
    assert status
# ------------------------------------------------------------------------------


def test_directory_existence_not_verified():
    """

    This function tests the OSUtilities.verify_directory_existence function to
    ensure it can correctly identify that a file does exist
    """
    util = OSUtilities()
    file = '../data/test/no_directory'
    status = util.verify_directory_existence(file)
    assert not status
# ------------------------------------------------------------------------------


def test_move_file():
    """

    This function test the OSUtilities.move_file_or_directory function to ensure that it
    successfully moves files between different locations
    """
    util = OSUtilities()
    file1 = '../data/test/move_test.txt'
    file2 = '../data/test/move_directory1/move_test2.txt'
    util.move_file(file1, file2)
    assert os.path.isfile(file2)
    if os.path.isfile(file2):
        util.move_file(file2, file1)
# ------------------------------------------------------------------------------


def test_list_contents():
    """

    This function tests the OSUtilities.list_contents function to ensure it returns the
    correct files and directories
    """
    util = OSUtilities()
    directory = '../data/test/list_dir'
    contents = util.list_contents(directory=directory, extension='.py')
    assert 'test.py' in contents

    contents = util.list_contents(directory=directory, extension='.txt')
    expected_result = ['test1.txt', 'test2.txt', 'test3.txt']
    for i in contents:
        assert i in expected_result

    contents = util.list_contents(directory=directory)
    expected_result = ['test1.txt', 'test2.txt', 'test3.txt', 'test', 'test.py']
    for i in contents:
        assert i in expected_result
# ------------------------------------------------------------------------------


def test_move_directory():
    """

    This function test the OSUtilities.move_file_or_directory function to ensure that it
    successfully moves directories between different locations
    """
    util = OSUtilities()
    file1 = '../data/test/populated_dir2'
    file2 = '../data/test/move_directory2/populated_dir2'
    file3 = '../data/test/move_directory2/populated_dir2/test.txt'
    util.move_directory(file1, file2)
    assert os.path.isdir(file2)
    assert os.path.isfile(file3)
    if os.path.isdir(file2):
        util.move_directory(file2, file1)
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
