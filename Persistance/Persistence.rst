.. role:: cover

===========================================
:cover:`Persistent data and serialization`
===========================================

.. class:: cover

    ::

        Jonas Juselius <jonas.juselius@uit.no>
    
        HPC@UiT

.. raw:: pdf

   SetPageCounter 0
   Transition Dissolve 1
   PageBreak oneColumn

Serialization and persistence 
----------------------------------------------------------
* Serialization is the act of converting an object into a form which can be
  stored and later resurrected
* Serialized objects can be stored on disk for later use, e.g. saving the
  state of the program so that it can re resumed later
* Serialized objects can also be transmitted over the net, e.g. http, MPI,
  mail...
* Data and objects which have been stored for later use are said to be
  persistent

Pickling
----------------------------------------------------------
Python can save more than just numbers and text: It can store whole objects!
This is known as *pickling* or *serializing* objects.

.. code-block:: python
    :linenos:
    :include: pickles.py

Shelving
----------------------------------------------------------
Shelving is a form of pickling, where the objects are stored in a
*persistent* dictionary on disk:

.. code-block:: python
    :linenos:
    :include: shelf.py

Relational databases
----------------------------------------------------------
* Data is stored in tables
* Entries in tables are stored in rows 
* Each row is uniquely identified by a *primary key*
* Columns define the structure of the table (eg. data types) 
* Columns are identified by name
* Tables can be chained by referring to each other

Basic SQL
----------------------------------------------------------

* SQL (Structured Query Language) is a *declarative* domain-specific language
* Example statements:
    - CREATE TABLE...
    - INSERT INTO <table> VALUES...
    - SELECT <values> FROM <table> (WHERE <condition>)...
    - DELETE FROM <table>

Create table
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: sqlite_create.py

Insert data into a table
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: sqlite_insert.py

Searching for data
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: sqlite_select.py

Deleting data from a table
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: sqlite_delete.py

