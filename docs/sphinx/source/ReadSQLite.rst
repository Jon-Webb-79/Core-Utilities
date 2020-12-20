ReadSQLite Data
===============
This section documents the ``ManageSQLiteDB`` class encoded in the
``read_files.py`` file.  This class opens a database, queries the database
and closes the database at the user discretion.


.. autoclass:: read_files.ManageSQLiteDB
   :members:

If a user only needs to execute one query, they can use the ``simple_sqlite_query``
Function that will handle database opening and closing for them.

.. autofunction:: read_files.simple_sqlite_query


