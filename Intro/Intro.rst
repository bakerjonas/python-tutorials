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

Writing scripts
---------------------------------------------------------
Instead of working inside the Python interpreter, we can write scripts using
our favorite editor (e.g. PyCharm) and save them. We can then execute the
scripts when we need them: 

.. code-block:: console

    $ python elderberry.py

Under UNIX we can make the scripts executable by adding a *shebang* to the
first line in the of the script, and then change the file mode:

.. code-block:: console

    $ sed -i '1i #!/usr/bin/env python' elderberry.py
    $ chmod a+x elderberry.py

.. code-block:: python

    #!/usr/bin/env python
    def hamster(): print('Your mother was a hamster.')

On Windows you don't have to do anything special, since the Python installer
registers file with a ``.py`` ending as Python programs.

Organizing your code: modules 
---------------------------------------------------------
When you organize your work in files, these files become Python modules if
they are in your ``PYTHONPATH``:

.. code-block:: pycon

    >>> import elderberry as eb
    >>> eb.hamster()

Organizing your code: packages
---------------------------------------------------------
Packages are a way of structuring Python’s module namespace by using *dotted
module names*::

    cheese/                     Top-level package
        __init__.py             Initialize the sound package
        swiss/                  Subpackage for swiss chees
            __init__.py
            emmental.py
            gruyere.py
        dutch/                  Subpackage for dutch cheese
            __init__.py
            gouda.py
            maasdam.py

Organizing your code: importing packages
---------------------------------------------------------

.. code-block:: python
    :linenos:
    :include: maasdam.py
    
Module search paths
----------------------------------------------------------

How and where Python looks for available modules can be configured using the
``PYTHONPATH`` environment variable:

.. code-block:: console

    $ export PYTHONPATH=$PYTHONPATH:/path/to/my/stuff
    $ python elderberry.py

The search path can also be configured in Python:

.. code-block:: python

    import sys
    sys.path.append('/path/to/my/stuff')
    print(sys.path)

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

The standard library
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: sys.py

.. code-block:: python
    :linenos:
    :include: os.py

The standard library: Math
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: math.py

The standard library: Compression
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: zlib.py

The standard library: A web server
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: httpd.py

The standard library: Input from urls
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: urls.py

The standard library: Sending mail
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: smtp.py

Functional programming 
---------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: functional.py

Coding style (`PEP 8`_)
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

.. _`PEP 8`: http://www.python.org/dev/peps/pep-0008/
