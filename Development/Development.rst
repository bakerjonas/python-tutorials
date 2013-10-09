.. role:: cover

==================================
:cover:`Writing programs`
==================================

.. class:: cover

    ::

        Jonas Juselius <jonas.juselius@uit.no>
    
        HPC@UiT

.. raw:: pdf

   SetPageCounter 0
   Transition Dissolve 1
   PageBreak oneColumn

Overview
----------------------------------------------------------
* Simplicity
* Using git
* Don't mess up your data
* Keep you functions lean
* Keep your object clean
* Zen of programming
* How to write readable code
* Be organized


Simplicity
----------------------------------------------------------

::
    
    Simplicity is the prerequisite for reliability
      -- Edsger W. Dijkstra

::

    Simplicity is the ultimate sophistication
      -- Leonardo da Vinci

::

    All programs suck
      -- Jonas Juselius

Zen of manging source code
----------------------------------------------------------

::

    1. Use git
    2. Use git

* Git is a snapshot manager for text files
* Add files to a snapshot, and press "snap"
* Repeat (often)
* Git allows you to communicate snapshots, and to combine snapshots:
  collaboration
* Git allows you to go back in time: no more backup copies
* With git, you can easily work on separate versions without losing your head
* Git happens: http://vimeo.com/46010208

Zen of data
----------------------------------------------------------
* Data is simple
* Functions are complex
* Objects are even more complex

::

    Data is simple, don't complect it!
    
* Use dictionaries whenever you can!

Zen of Data
----------------------------------------------------------
.. code-block:: python
    :include: dicts.py

Zen of functions
----------------------------------------------------------
* Functions should be short. 
* Functions should do only one thing, and do it well.
* Functions should have a docstring.
* Document *what* a function does, not *how* it does it.
* Functions should avoid *state* as much as possible!

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
        __init__.py             Initialize the cheese package
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
    :include: cheeseboard.py
    
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

Writing scripts
---------------------------------------------------------
Instead of working inside the Python interpreter, we can write scripts using
our favorite editor and save them. We can then execute the
scripts when we need them: 

.. code-block:: console

    $ python elderberry.py

Under UNIX we can make the scripts executable by adding a *shebang* to the
first line in the of the script, and then change the file mode:

.. code-block:: python

    #!/usr/bin/env python
    def hamster(): print('Your mother was a hamster.')

.. code-block:: console

    $ chmod a+x elderberry.py

On Windows you don't have to do anything special, since the Python installer
registers file with a ``.py`` ending as Python programs.

.. .. include:: Libs.rst

