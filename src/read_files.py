# Import necessary packages here
import os
import sys
import numpy as np
from typing import List
# ============================================================================
# ============================================================================
# Date:    December 10, 2020
# Purpose: This file contains classes and functions that assist in reading
#          ASCII based text files and databases

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2020, Jon Webb Inc."
__version__ = "1.0"
# ============================================================================
# ============================================================================


class FileUtilities:
    """
    This set of functions were written as class methods in order
    to ensure that they can be passed via decorator patters or
    through inheritance.
    """
    @classmethod
    def count_occurrence_of_word_in_file(cls, file_name: str, word: str) -> int:
        """

        :param file_name: The file name to include the path link
        :param word: the word for which the number of occurrences in
                     a file is desired.
        :return num: The number of times a specific word occurs in a
                     file.

        This function excludes the effects of punctuation.  For example
        if the user defined word is `book` and the file contains the
        word `book.` with a period following it indicating the end of a
        sentence, this function will count that word.  The same is true
        for commas.
        """
        file = open(file_name, "rt")
        data = file.read().split()
        counter = 0
        for i in range(len(data)):
            if data[i] == word:
                counter += 1
            if data[i] == word + ',':
                counter += 1
            if data[i] == word + '.':
                counter += 1
        return counter
# ----------------------------------------------------------------------------

    @classmethod
    def current_working_directory(cls) -> str:
        """

        :return cwd: A string describing the current working directory
        """
        return os.getcwd()
# ----------------------------------------------------------------------------

    @classmethod
    def determine_file_size(cls, file_name: str) -> float:
        """

        :param file_name: The file name to include path length
        :return kb_size: The size of a file in kilo-bites
        """
        byte_size = os.stat(file_name).st_size
        return byte_size / 1024.0
# ----------------------------------------------------------------------------

    @classmethod
    def file_line_count(cls, file_name: str) -> int:
        """

        :param file_name: The file name to include the path-link
        :return lines: The number of lines in a file
        """
        return len(open(file_name).readlines())
# ----------------------------------------------------------------------------

    @classmethod
    def file_word_count(cls, file_name: str) -> int:
        """

        :param file_name: The file name to include the path link
        :return words: The number of words in a file.  A word is defined
                       as a continuous string of characters with no empty
                       spaces in the string
        """
        file = open(file_name, "rt")
        data = file.read()
        return len(data.split())
# ----------------------------------------------------------------------------

    @classmethod
    def verify_file_existence(cls, file_name: str) -> bool:
        """

        :param file_name: The file name to include the path-link
        :return status: True or false if the file does or does not
                        exist
        """
        return os.path.isfile(file_name)
# ============================================================================
# ============================================================================


class ReadTextFileKeywords(FileUtilities):
    """
    A class to find keywords in a text file and the the variable(s)
    to the right of the key word.


    :param file_name: The name of the file being read to include the
                      path-link

    For the purposes of demonstrating the use of this class, assume
    a text file titled `test_file.txt` with the following contents.


    .. code-block:: text

        sentence: This is a short sentence!
        float: 3.1415 # this is a float comment
        double: 3.141596235941 # this is a double comment
        String: test # this is a string comment
        Integer Value: 3 # This is an integer comment
        float list: 1.2 3.4 4.5 5.6 6.7
        double list: 1.12321 344.3454453 21.434553
        integer list: 1 2 3 4 5 6 7
    """
    def __init__(self, file_name: str):
        self.file_name = file_name
        if not self.verify_file_existence(file_name):
            sys.exit('{}{}{}'.format('FATAL ERROR: ', file_name, ' does not exist'))
# ----------------------------------------------------------------------------

    def read_double(self, key_words: str) -> np.float64:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The float value following the **key_word** on the
                      text file.  This variable is returned as a
                      np.float64 data type

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the first data point following the key word(s) on the text file as a float value.
        The text file can also contain a comment line following the variable
        being read.  For example we could use this class to read the double
        value 3.141596235941 in the following manner.

        .. code-block:: python

            > dat = ReadTextFileKeywords('test_file.txt')
            > double_data = dat.read_double('double:')
            > print(double_data)
            3.141596235941
        """
        values = self.read_sentence(key_words)
        values = values.split()
        return np.float64(values[0])
# ----------------------------------------------------------------------------

    def read_float(self, key_words: str) -> np.float32:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The float value following the **key_word** on the
                      text file.  This variable is returned as a
                      np.float32 data type

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the first data point following the key word(s) on the text file as a float value.
        The text file can also contain a comment line following the variable
        being read.  For example we could use this class to read the float
        value 3.1415 in the following manner.

        .. code-block:: python

           > dat = ReadTextFileKeywords('test_file.txt')
           > float_data = dat.read_float('float data:')
           > print(float_data)
           3.1415
        """
        values = self.read_sentence(key_words)
        values = values.split()
        return np.float32(values[0])
# ----------------------------------------------------------------------------

    def read_integer(self, key_words: str) -> np.int32:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The integer value following the **key_word** on the
                      text file.  This variable is returned as a np.int32
                      data type

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the the first data point following the key word(s) on the text file as a
        integer value. The text file can also contain a comment line following
        the variable being read.  For example we could use this class to
        read the integer value 3 in the following manner.

        .. code-block:: python

           > dat = ReadTextFileKeywords('test_file.txt')
           > int_data = dat.read_float('Integer Value')
           > print(int_data)
           3
        """
        values = self.read_sentence(key_words)
        values = values.split()
        return np.int32(values[0])
# ----------------------------------------------------------------------------

    def read_sentence(self, key_words: str) -> str:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The data following the **key_word** on the text file.
                      The data is returned as a continuous string value

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the data following the key word(s) on the text file as a continuous string.
        The text file can also contain a comment line following the variable
        being read.  For example we could use this class to read the integer
        value `This is a short sentence!` in the following manner.

        .. code-block:: python

           > dat = ReadTextFileKeywords('test_file.txt')
           > str_data = dat.read_float('sentence:')
           > print(str_data)
           'This is a short sentence!'
        """
        input_words = key_words.split()
        with open(self.file_name) as Input_File:
            lines = Input_File.readlines()
            for line in lines:
                variable = line.split()
                counter = 0
                for i in range(len(input_words)):
                    if input_words[i] != variable[i]:
                        break
                    else:
                        counter += 1
                if counter == len(input_words):
                    start = len(input_words)
                    end = len(variable)
                    word = ''
                    for i in range(start, end):
                        word = word + ' ' + variable[i]
                    return word.lstrip()
        sys.exit('{}{}{}'.format(key_words, " Keywords not found in ", self.file_name))
# ----------------------------------------------------------------------------

    def read_string(self, key_words: str) -> str:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The string value following the **key_word** on the
                      text file.  This variable is returned as a str
                      data type

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the the first data point following the key word(s) on the text file as a
        string value. The text file can also contain a comment line following
        the variable being read.  For example we could use this class to
        read the string value `test` in the following manner.

        .. code-block:: python

           > dat = ReadTextFileKeywords('test_file.txt')
           > str_data = dat.read_float('String:')
           > print(str_data)
           'test'
        """
        values = self.read_sentence(key_words)
        values = values.split()
        return str(values[0])
# ----------------------------------------------------------------------------

    def read_string_list(self, key_words: str) -> List[str]:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The string values following the **key_word** on the
                      text file.  This variable is returned as a List of
                      string values

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the the first data point following the key word(s) on the text file as a
        string value. The text file can also contain a comment line following
        the variable being read.  For example we could use this class to
        read the string value `test` in the following manner.

        .. code-block:: python

            > dat = ReadTextFileKeywords('test_file.txt')
            > str_data = dat.read_string_list('sentence:')
            > print(str_data)
            ['This', 'is', 'a', 'short', 'sentence!']
        """
        values = self.read_sentence(key_words)
        values = values.split()
        values = [str(value) for value in values]
        return values
# ============================================================================
# ============================================================================
# TODO Add read_float_list function
# TODO Add read_double_list function
# TODO Add read_integer_list function
# eof
