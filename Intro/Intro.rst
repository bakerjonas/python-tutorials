.. role:: cover

==================================
:cover:`Introduction to Python`
==================================

.. class:: cover

    ::

        Jonas Juselius <jonas.juselius@uit.no>
    
        HPC@UiT

.. raw:: pdf

   Transition Dissolve 1
   SetPageCounter 0
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
* Document *what* a function does, not *how** it does it.

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

Some important built-in functions
----------------------------------------------------------
.. code-block:: python

    abs(x)          # Return absolute values of x
    all(list)       # True if all elements are True
    any(list)       # True if any element is True
    cmp(a, b)       # Compare a and b
    dir()           # Return a list of "members"
    eval(str)       # Evaluate a string as a Python experssion
    filter(f, list) # Return elements for which f evaluates true
    map(f, list)    # Apply f to every element in list
    max(), min()    # Minimum and maximum of values
    pow(x, y)       # x^y
    reduce(f, list) # Reduce list with f
    str(o)          # Generate a string from an object
    sum(list)       # Sum all elements


Working with files
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: writefile.py

.. code-block:: python
    :linenos:
    :include: readfile.py

Modules and namespaces
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: import.py

The standard library
----------------------------------------------------------

OMG!

Exceptions and errors
----------------------------------------------------------


Classes
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: class.py

Python objects
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: object.py


Coding style (PEP 8)
----------------------------------------------------------
* Use 4-space indentation, and no tabs.
* Wrap lines so that they don’t exceed 79 characters.
* Use blank lines to separate functions and classes, and larger blocks of code
  inside functions.
* When possible, put comments on a line of their own.
* Use docstrings.
* Use spaces around operators and after commas, but not directly inside
  bracketing constructs: a = f(1, 2) + g(3, 4).
* Name your classes and functions consistently; the convention is to use
  CamelCase for classes and lower_case_with_underscores for functions and
  methods. Always use self as the name for the first method argument 
* Don’t use fancy encodings if your code is meant to be used in international
  environments. Plain ASCII works best in any case.

The Zen of (Python) programing
----------------------------------------------------------
:: 

    $ python -c "import this"

#.   Beautiful is better than ugly.
#.   Explicit is better than implicit.
#.   Simple is better than complex.
#.   Complex is better than complicated.
#.   Flat is better than nested.
#.   Sparse is better than dense.
#.   Readability counts.
#.   Special cases aren't special enough to break the rules.
#.   Although practicality beats purity.

The Zen of (Python) programing
----------------------------------------------------------
10.   Errors should never pass silently.
#.   Unless explicitly silenced.
#.   In the face of ambiguity, refuse the temptation to guess.
#.   There should be one-- and preferably only one --obvious way to do it.
#.   Although that way may not be obvious at first unless you're Dutch.
#.   Now is better than never.
#.   Although never is often better than *right* now.
#.   If the implementation is hard to explain, it's a bad idea.
#.   If the implementation is easy to explain, it may be a good idea.
#.   Namespaces are one honking great idea -- let's do more of those!

Sphinx
----------------------------------------------------------

Virtual Python environments
----------------------------------------------------------

Dynamic nature of Python
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: dynamic.py

