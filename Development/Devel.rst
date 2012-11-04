.. role:: cover

===============================================
:cover:`Python development and good practices`
===============================================

.. class:: cover

    ::

        Jonas Juselius <jonas.juselius@uit.no>
    
        HPC@UiT

.. raw:: pdf

   Transition Dissolve 1
   SetPageCounter 0
   PageBreak oneColumn


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

