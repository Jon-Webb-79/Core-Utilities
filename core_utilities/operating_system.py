# Import necessary packages here
import os
import shutil
from typing import List
# ============================================================================
# ============================================================================
# Date:    December 10, 2020
# Purpose: This file contains classes and functions that assist in maintaining
#          an operating system.  The functions are designed to be similar to
#          commands used in Linux and DOS.

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2020, Jon Webb Inc."
__version__ = "1.0"
# ============================================================================
# ============================================================================


class OSUtilities:
    """
    This set of functions were written as class methods in order
    to ensure that they can be passed in bulk via decorator patters
    or through inheritance.  This class provides file analysis
    capabilities and a user interface for file and directory management
    similar to Bash and DOS functionality, although with different
    syntax

    All code examples are predicated on the instantiation of this class
    with the following command

    .. code-block:: python

       > util = OSUtilities()
    """
    @classmethod
    def change_directory(cls, new_directory: str) -> None:
        """

        :param new_directory: The desired directory to include
                              path link
        :return None:

        This function will change the directory in the same manner as
        the `cd` DOS and Linux command.  For example, if you are
        in the `dir1` directory within the following chain;

        `home/dir1/dir2/`

        You can use the following python script to change to the `dir2`
        directory.

        .. code-block:: python

           > print(util.current_working_directory())
           '/home/dir1'
           > util.change_directory('dir2')
           > print(util.current_working_directory())
           '/home/dir1/dir2'

        You can change back to the `home` directory with the following
        command;

        .. code-block:: python

           > util.change_directory('../..')
           > print(util.current_working_directory())
           '/home'
        """
        if not os.path.isdir(new_directory):
            print('{}{}'.format(new_directory, ' does not exist'))
        os.chdir(new_directory)
# ----------------------------------------------------------------------------

    @classmethod
    def copy_directory(cls, source: str, destination: str) -> None:
        """

        :param source: The name and path-link of the directory to
                       be copied
        :param destination: The name and path-link for the directory
                            copy
        :return None:

        This function creates a copy of a directory and assigns
        it to the directory of the users choosing.  This function
        will copy populated and un-populated directories.  As
        an example lets assume the following directory structure;

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_2
              directory_3
                 |
                 another_text_file.txt

        The following command will make  copy of ``directory_2`` in
        the ``directory_3`` titled ``dir2_copy``, directory assuming
        we are in the ``directory_1`` directory

        .. code-block:: python

           > copy_directory('directory_2', 'directory_3/dir2_copy')
           > change_directory('directory_3')
           > print(list_contents())
           [''another_text_file.txt', 'dir2_copy']

        """
        if not os.path.isdir(source):
            print('{}{}'.format(source, ' does not exist'))
        elif os.path.isdir(destination):
            print('{}{}'.format(destination, ' already exists'))
        else:
            shutil.copytree(source, destination)
# ----------------------------------------------------------------------------

    @classmethod
    def copy_file(cls, source: str, destination: str) -> None:
        """

        :param source: The name and path-link of the file to be
                       copied
        :param destination: The name and path-link for the file copy
        :return None:

        This function creates a copy of a file and assigns it to the
        name and directory of the users choosing.  As
        an example lets assume the following directory structure;

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_2
              directory_3
                 |
                 another_text_file.txt

        The following command will make  copy of ``text_file.txt`` in
        the ``directory_3`` titled ``text_copy.txt``, directory assuming
        we are in the ``directory_1`` directory

        .. code-block:: python

           > copy_file('text_file.txt', 'directory_3/text_copy.txt')
           > change_directory('directory_3')
           > print(list_contents())
           [''another_text_file.txt', 'text_copy.txt']

        """
        if not os.path.isfile(source):
            print('{}{}'.format(source, ' does not exist'))
        elif os.path.isfile(destination):
            print('{}{}'.format(destination, ' already exists'))
        else:
            shutil.copy(source, destination)
# ----------------------------------------------------------------------------

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
        for commas.  As an example lets assume the file listed below,
        titled ``test.txt``;

        .. code-block:: text

           This is a text file, all
           of the information in this
           file is specifically for
           the purpose of testing file file

        The following code will count the occurrence of the word ``file``

        .. code-block:: python

           > num = util.count_occurrence_of_word_in_file('test.txt', 'file')
           > print(num)
           4
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
    def create_directory(cls, directory_name: str) -> None:
        """

        :param directory_name: The name of the directory to be created
                               to include the path-link
        :return None:

        This function creates a directory in the following manner

        .. code-block:: python

           > print(util.list_contents())
           ['data.txt', 'document.doc']
           > util.create_directory('new_directory')
           > print(util.list_contents())
           ['data.txt', 'document.doc', 'new_directory']
        """
        if os.path.isdir(directory_name):
            print('{}{}'.format(directory_name, ' already exists'))
        else:
            os.mkdir(directory_name)
# ----------------------------------------------------------------------------

    @classmethod
    def create_file(cls, file_name: str) -> None:
        """

        :param file_name: The name of the file to be created to
                          include the path link
        :return None:

        This function creates a file in a method that mimics the touch
        command in Linux.

        .. code-block:: python

           > print(util.list_contents())
           ['data.txt', 'document.doc']
           > util.create_file('new_text.txt')
           > print(util.list_contents())
           ['data.txt', 'document.doc', 'new_text.txt']
        """
        with open(file_name, 'w'):
            pass
# ----------------------------------------------------------------------------

    @classmethod
    def current_working_directory(cls) -> str:
        """

        :return cwd: A string describing the current working directory

        This function returns a string describing the current
        working directory.

        .. code-block:: python

           > print(util.current_working_directory())
           '/users/computername/Desktop/Code_Dev/Python/core_utilities'
        """
        return os.getcwd()
# ----------------------------------------------------------------------------

    @classmethod
    def delete_directory(cls, directory_name: str) -> None:
        """

        :param directory_name: The name of the directory to be deleted to
                               include path links
        :return None:

        This function deletes an  un-populated directory.  As
        an example lets assume the following directory structure;

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_2
              directory_3
                 |
                 another_text_file.txt

        .. code-block:: python

           > print(util.list_contents())
           ['text_file.txt', 'directory_2', 'directory_3']
           > util.delete_directory('directory_2')
           > print(util.list_contents())
           ['text_file.txt', 'directory_3']

        """
        if not os.path.isdir(directory_name):
            print('{}{}'.format(directory_name, ' does not exist'))
        else:
            os.rmdir(directory_name)
# ----------------------------------------------------------------------------

    @classmethod
    def delete_file(cls, file_name: str) -> None:
        """

        :param file_name: The name of the file to be deleted to include
                          the path link
        :return None:

        This function deletes a file.

        .. code-block:: python

           > print(util.list_contents())
           ['test_file.txt', 'test2.txt', 'word_document.doc']
           > util.delete_file('word_document.doc')
           print(util.list_contents())
           ['test_file.txt', 'test2.txt']

        """
        if not os.path.isfile(file_name):
            print('{}{}'.format(file_name, ' does not exist'))
        else:
            os.remove(file_name)
# ----------------------------------------------------------------------------

    @classmethod
    def delete_populated_directory(cls, directory_name: str) -> None:
        """

        :param directory_name: The name of the directory to be deleted to
                               include path links
        :return None:

        This function deletes a directory that is populated with files
        and other directories.  As an example lets assume the following
        directory structure;

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_2
              directory_3
                 |
                 another_text_file.txt

        .. code-block:: python

           > print(util.list_contents())
           ['text_file.txt', 'directory_2', 'directory_3']
           > util.delete_directory('directory_3')
           > print(util.list_contents())
           ['text_file.txt', 'directory_2']

        """
        if not os.path.isdir(directory_name):
            print('{}{}'.format(directory_name, ' does not exist'))
        else:
            shutil.rmtree(directory_name)
# ----------------------------------------------------------------------------

    @classmethod
    def determine_file_size(cls, file_name: str) -> float:
        """

        :param file_name: The file name to include path length
        :return kb_size: The size of a file in kilo-bites

        This function returns the size of a file in units of kb.

        .. code-block:: python

           > num = util.determine_file_size('photo.jpg')
           > print(num)
           3450.5
        """
        byte_size = os.stat(file_name).st_size
        return byte_size / 1024.0
# ----------------------------------------------------------------------------

    @classmethod
    def file_line_count(cls, file_name: str) -> int:
        """

        :param file_name: The file name to include the path-link
        :return lines: The number of lines in a file

        This function returns the number of lines in an ASCII
        based file.  As an example lets assume the file listed below,
        titled ``test.txt``;

        .. code-block:: text

           This is a text file, all
           of the information in this
           file is specifically for
           the purpose of testing file file

        The following code will count the occurrence of the word ``file``

        .. code-block:: python

           > num = util.file_line_count('test.txt')
           > print(num)
           4
        """
        return len(open(file_name).readlines())
# ----------------------------------------------------------------------------

    @classmethod
    def file_word_count(cls, file_name: str) -> int:
        """

        :param file_name: The file name to include the path link
        :return words: The number of words in a file.  A word is defined
                       as a continuous string of characters with no empty
                       spaces in the string.

        This function returns the number of words in an ASCII based document.
        As an example lets assume the file listed below, titled ``test.txt``;

        .. code-block:: text

           This is a text file, all
           of the information in this
           file is specifically for
           the purpose of testing file file

        The following code will count the occurrence of the word ``file``

        .. code-block:: python

           > num = util.file_word_count('test.txt')
           > print(num)
           21

        """
        file = open(file_name, "rt")
        data = file.read()
        return len(data.split())
# ----------------------------------------------------------------------------

    @classmethod
    def list_contents(cls, directory: str = '.',
                      extension: str = 'NULL') -> List[str]:
        """

        :param directory: The directory where the contents are
                          desired
        :param extension: A file extension such as `.txt` or `.csv`
        :return None:

        This function will return a list containing the contents of
        a specific directory.  The user can enter the directory of
        interest or default to the current working directory.  The
        user can also specify the type of file they wish listed.

        .. code-block:: python

           > print(util.list_contents())
           ['Files', 'Code_Dev', 'word_document.doc']
        """

        if extension != 'NULL':
            data = os.listdir(directory)
            length = len(extension)
            new_data = [i for i in data if extension in i[-length:]]
            return new_data
        else:
            return os.listdir(directory)
# ----------------------------------------------------------------------------

    @classmethod
    def move_directory(cls, source: str, destination: str) -> None:
        """

        :param source: The name of the file being moved to include the
                       path-link
        :param destination: The name of the file at its new destination
                            to include the path link
        :return None:

        This function will move a file to a new location and give it a
        different or identical user define name.  The original file
        and location will be deleted.  As an example lets assume the
        following directory structure;

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_2
              directory_3
                 |
                 another_text_file.txt

        The following command will create the updated directory structure.

        .. code-block:: python

           > util.move_directory('directory_2', 'directory_3/new_dir')

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_3
                 |
                 new_dir
                 another_text_file.txt
        """
        if not os.path.isdir(source):
            print('{}{}'.format(source, ' does not exist'))
        elif os.path.isdir(destination):
            print('{}{}'.format(destination, ' already exists'))
        else:
            shutil.move(source, destination)
# ----------------------------------------------------------------------------

    @classmethod
    def move_file(cls, source: str, destination: str) -> None:
        """

        :param source: The name of the file being moved to include the
                       path-link
        :param destination: The name of the file at its new destination
                            to include the path link
        :return None:

        This function will move a file to a new location and give it a
        different or identical user define name.  The original file
        and location will be deleted. As an example lets assume the
        following directory structure;

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_2
              directory_3
                 |
                 another_text_file.txt

        The following command will create the updated directory structure.

        .. code-block:: python

           > util.move_file('text_file.txt', 'directory_2')

        .. code-block:: text

           directory_1
              |
              directory_2
                 |
                 text_file.txt
              directory_3
                 |
                 another_text_file.txt
        """
        if not os.path.isfile(source):
            print('{}{}'.format(source, ' does not exist'))
        elif os.path.isfile(destination):
            print('{}{}'.format(destination, ' already exists'))
        else:
            shutil.move(source, destination)
# ----------------------------------------------------------------------------

    @classmethod
    def copy_files(cls, destination: str, source: str = os.getcwd(),
                   extension: str = 'NULL', dirs: bool = False) -> None:
        """

        :param destination: The destination directory to include
                            path-links
        :param source: The source directory to include path-links,
                       defaulted to current working directory
        :param extension: Specific file extension to be copied.
        :param dirs: `True` if user only wants to copy directories,
                     `False` otherwise

        :return None:

        This function will copy all of the contents of a directory
        to another directory, or all of a specific type of file to
        another directory, or all directories to another directory.
        As an example lets assume the following directory structure;

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_2
              directory_3
                 |
                 another_text_file.txt
                 more_data.doc
                 new_dir

        assuming we are in ``directory_3``

        .. code-block:: python

           > # Copies everything
           > util.copy_files('../directory_2')

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_2
                 |
                 another_text_file.txt
                 more_data.doc
                 new_dir
              directory_3
                 |
                 another_text_file.txt
                 more_data.doc
                 new_dir

        .. code-block:: python

           > # Copies text files
           > util.copy_files('../directory_2', extension='.txt')

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_2
                 |
                 another_text_file.txt
              directory_3
                 |
                 another_text_file.txt
                 more_data.doc
                 new_dir

        .. code-block:: python

           > # Copies directories
           > util.copy_files('../directory_2', dirs=True)

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_2
                 |
                 new_dir
              directory_3
                 |
                 another_text_file.txt
                 more_data.doc
                 new_dir
        """
        if dirs and extension != 'NULL':
            print('{}'.format('extension must be null when dirs is True'))
        files = OSUtilities.list_contents(source, extension)
        directories = [i for i in files if '.' not in i]
        fls = [i for i in files if '.' in i]
        if not dirs:
            for i in fls:
                src = source + "/" + i
                OSUtilities.copy_file(src, destination)
        for j in directories:
            src = source + "/" + j
            OSUtilities.copy_directory(src, destination + "/" + j)
# ----------------------------------------------------------------------------

    @classmethod
    def move_files(cls, destination: str, source: str = os.getcwd(),
                   extension: str = 'NULL', dirs: bool = False) -> None:
        """

        :param destination: The destination directory to include
                            path-links
        :param source: The source directory to include path-links,
                       defaulted to current working directory
        :param extension: Specific file extension to be copied.
        :param dirs: `True` if user only wants to copy directories,
                     `False` otherwise

        :return None:

        This function will move all of the contents of a directory
        to another directory, or all of a specific type of file to
        another directory, or all directories to another directory
        As an example lets assume the following directory structure;

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_2
              directory_3
                 |
                 another_text_file.txt
                 more_data.doc
                 new_dir

        assuming we are in ``directory_3``

        .. code-block:: python

           > # Moves everything
           > util.move_files('../directory_2')

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_2
                 |
                 another_text_file.txt
                 more_data.doc
                 new_dir
              directory_3

        .. code-block:: python

           > # Moves text files
           > util.move_files('../directory_2', extension='.txt')

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_2
                 |
                 another_text_file.txt
              directory_3
                 |
                 more_data.doc
                 new_dir

        .. code-block:: python

           > # Moves directories
           > util.move_files('../directory_2', dirs=True)

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_2
                 |
                 new_dir
              directory_3
                 |
                 another_text_file.txt
                 more_data.doc
        """
        if dirs and extension != 'NULL':
            print('{}'.format('extension must be null when dirs is True'))
        files = OSUtilities.list_contents(source, extension)
        directories = [i for i in files if '.' not in i]
        fls = [i for i in files if '.' in i]
        if not dirs:
            for i in fls:
                src = source + "/" + i
                OSUtilities.move_file(src, destination)
        for j in directories:
            src = source + "/" + j
            OSUtilities.move_directory(src, destination + "/" + j)
# ----------------------------------------------------------------------------

    @classmethod
    def verify_directory_existence(cls, directory_name: str) -> bool:
        """

        :param directory_name: The directory name to include the path-link
        :return status: True or false if the directory does or does not
                        exist

        This function verifies whether or not a directory exists.

        .. code-block:: python

           > print(util.verify_directory_existence('directory'))
           True
        """
        return os.path.isdir(directory_name)
# ----------------------------------------------------------------------------

    @classmethod
    def verify_file_existence(cls, file_name: str) -> bool:
        """

        :param file_name: The file name to include the path-link
        :return status: True or false if the file does or does not
                        exist

        This function verifies whether or not a file exists

        .. code-block:: python

           > print(util.verify_file_existence('new_file.txt'))
           False
        """
        return os.path.isfile(file_name)
# ============================================================================
# ============================================================================
# eof
