# Import necessary packages here
import os
import sys
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


class OSUtilities:
    @classmethod
    def verify_file_existence(cls, file_name: str) -> None:
        """

        :param file_name: The file name to include the path-link
        :return None:

        This function determines if a file does or does not exist.  If the
        file does not exist, the function will halt execution and inform
        the user
        """
        if os.path.isfile(file_name):
            return
        sys.exit('{}{}{}'.format('FATAL ERROR: ', file_name, ' does not exist'))
# ----------------------------------------------------------------------------

    @classmethod
    def current_working_directory(self) -> str:
        """

        :return cwd: A string describing the current working directory
        """
        return os.getcwd()
# ----------------------------------------------------------------------------
# TODO create function to make a directory
# TODO create d function to delete a directory
# TODO create a function to create a file
# TODO create a function to delete a file
# TODO create a function to determine the size of a file
# TODO create a function to determine how many lines are in a file
# ============================================================================
# ============================================================================
# eof
