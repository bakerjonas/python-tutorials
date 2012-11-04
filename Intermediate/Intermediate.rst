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

Dynamic nature of Python
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: dynamic.py

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

Virtual Python environments
----------------------------------------------------------

reStructuredText
----------------------------------------------------------

Sphinx
----------------------------------------------------------

