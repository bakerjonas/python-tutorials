.. role:: cover

==================================
:cover:`Introduction to Python`
==================================

.. class:: cover

    ::

        Jonas Juselius <jonas.juselius@uit.no>
    
        HPC@UiT

.. raw:: pdf

   SetPageCounter 0
   Transition Dissolve 1
   PageBreak oneColumn

About Python
----------------------------------------------------------

* Python is simple to use, but it is a real programming language.
* Python enables programs to be written compactly and readably. 
* Python comes with a large collection of standard modules.
* Python is an interpreted language.
* Python allows you to split your program into modules that can be reused in
  other Python programs.
* Python is extensible
* Python is just the language for you.
* Python is just great!

.. raw:: pdf

   PageBreak 
   Transition Dissolve 0

Using the Python interpreter
----------------------------------------------------------
The default Python interpreter is called ``python``. It is used to run
scripts and for simple interactive work:

.. code-block:: shell

    $ python
    Python 2.7.3 (default, Sep 26 2012, 21:51:14) 
    >>> 1 + 2
    3
    >>> ^D
    $

Using the iPython interpreter
----------------------------------------------------------
For interactive work, iPython (``ipython``) provides a more elaborate
interface with many enhancements:

.. code-block:: shell

    $ ipython 
    IPython 0.13.1.rc2 -- An enhanced Interactive Python.

    In [1]: "Hello" + " " + "World!"
    Out[1]: 'Hello World!'

    In [2]: ^D
    Do you really want to exit ([y]/n)? y
    $

The iPython web notebook
----------------------------------------------------------

iPython also comes with an incredibly cool interactive web notebook:

.. code-block:: shell

    $ ipython notebook
    [NotebookApp] The IPython Notebook is running at: http://127.0.0.1:8888/
    [NotebookApp] Use Control-C to stop this server and shut down all kernels.
    Created new window in existing browser session.

The notebook allows you to use work cells, save and load files, plot
functions, much like in Matlab or Mathematica. 

You can drag and drop Python files on disk straight into the notebook and
execute the file.

Numbers 
----------------------------------------------------------
.. code-block:: pycon
    :include: nums.py

Variables 
----------------------------------------------------------
.. code-block:: pycon
    :include: vars.py

Strings 
----------------------------------------------------------
.. code-block:: pycon
    :include: strings.py

String operations
----------------------------------------------------------
.. code-block:: pycon
    :include: string_ops.py

String methods
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: string_methods.py

Lists 
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: lists.py

Flow control
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: ifelse.py

Repeating things
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: while.py

The ``for`` loop
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: for.py

Tuples and sets
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: tuples.py

Dictionaries  
----------------------------------------------------------
Dictionaries are powerful data containers. They behave like an
unordered set of ``key:value`` pairs, with the requirement that the keys are
unique.

.. code-block:: python
    :include: dicts.py

Looping techniques
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: looptricks.py

Function definition
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: funcdef.py

Function definition
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: funcdef2.py

Function definition
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: funcdef3.py

Recursive functions
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: recursion.py

Zen of functions
----------------------------------------------------------
* Functions should be short. 
* Functions should do only one thing, and do it well.
* Functions should have a docstring.
* Document *what* a function does, not *how* it does it.

Input and output
----------------------------------------------------------

.. code-block:: python
    :linenos:
    :include: writefile.py

Input and output
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: readfile.py

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

Modules and namespaces
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: import.py

Getting help
----------------------------------------------------------
In iPython:

.. code-block:: pycon
    
    >>> dir?
    >>> dir()             # dir() is a Python builtin function
    >>> dir(__builtin__)
    >>> dir("foo")
    >>> dir(42)

Using ``pydoc``:

.. code-block:: console

    $ pydoc dir
    $ pydoc -p 8080
    pydoc server ready at http://localhost:8080/

| Least but not last: 
|   http://docs.python.org
|   http://google.com 

