# Import modules here
import sys
import os
import pytest
sys.path.insert(0, os.path.abspath('../src'))

from read_files import OSUtilities
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


def test_verify_file_existence():
    """

    This function tests the OSUtilities.verify_file_existence function to
    ensure it can correctly identify that a file does exist
    """
    util = OSUtilities()
    file = '../data/test/text_file.txt'
    util.verify_file_existence(file)
# ------------------------------------------------------------------------------


def test_file_existence_not_verified():
    """

    This function tests the OSUtilities.verify_file_existence function to
    ensure that it can correctly identify when a file does not exist
    """
    util = OSUtilities()
    file = '../data/test/no_text_file.txt'
    with pytest.raises(SystemExit):
        util.verify_file_existence(file)
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
# ==============================================================================
# ==============================================================================
# eof
