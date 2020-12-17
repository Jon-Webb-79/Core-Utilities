# Import modules here
import sys
import os
import pytest
import numpy as np
from math import isclose
sys.path.insert(0, os.path.abspath('../src'))

from read_files import ReadTextFileKeywords, read_csv_columns_by_headers
from read_files import read_csv_columns_by_index, read_text_columns_by_headers
from read_files import read_text_columns_by_index
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
# Test read column functions


def test_read_csv_by_headers():
    """

    This function tests the read_csv_columns_by_headers function to ensure
    it properly reads in a csv file with the headers placed at the top
    of the file
    """
    file_name = '../data/test/test1.csv'
    headers = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    df = read_csv_columns_by_headers(file_name, headers, dat)
    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_csv_by_headers_below_start():
    """

    This function tests the read_csv_columns_by_headers function to ensure
    it properly reads in a csv file with the headers placed below the top
    of the file
    """
    file_name = '../data/test/test1.csv'
    headers = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    df = read_csv_columns_by_headers(file_name, headers, dat)

    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_csv_by_index():
    """

    This function tests the read_csv_columns_by_index function to ensure
    it properly reads in a csv file that has no headers and gives each
    header a name
    """
    file_name = '../data/test/test3.csv'
    headers = [0, 1, 2, 3]
    names = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    df = read_csv_columns_by_index(file_name, headers, dat, names)

    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_csv_by_index_below_start():
    """

    This function tests the read_csv_columns_by_index function to ensure
    it properly reads in a csv file that has no headers and gives each
    header a name.  This test uses a .csv file that has metadata on
    the first two lines before the beginning of the columnar data
    """
    file_name = '../data/test/test4.csv'
    headers = [0, 1, 2, 3]
    names = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    df = read_csv_columns_by_index(file_name, headers, dat,
                                   names, skip=2)

    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_text_by_header():
    """

    This function tests the read_text_columns_by_headers function to
    ensure it properly reads in a space delimited text file with
    a header in the top row
    """
    file_name = '../data/test/textcol1.txt'
    headers = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    df = read_text_columns_by_headers(file_name, headers, dat)

    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_text_by_header_below_start():
    """

    This function tests the read_text_columns_by_headers function to
    ensure it properly reads in a space delimited text file with
    a header not in the top row
    """
    file_name = '../data/test/textcol2.txt'
    headers = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    df = read_text_columns_by_headers(file_name, headers, dat, skip=2)

    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_text_by_index():
    """

    This function tests the read_text_columns_by_index function to
    ensure it properly reads in a space delimited text file with
    a header in the top row
    """
    file_name = '../data/test/textcol3.txt'
    headers = [0, 1, 2, 3]
    names= ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    df = read_text_columns_by_index(file_name, headers, dat, names)

    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_text_by_index_below_start():
    """

    This function tests the read_text_columns_by_index function to
    ensure it properly reads in a space delimited text file with
    a header not in the top row
    """
    file_name = '../data/test/textcol4.txt'
    headers = [0, 1, 2, 3]
    names= ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    df = read_text_columns_by_index(file_name, headers, dat,
                                    names, skip=2)

    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ==============================================================================
# ==============================================================================
# eof
