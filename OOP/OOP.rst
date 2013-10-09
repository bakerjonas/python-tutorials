.. role:: cover

===============================================
:cover:`Introduction to Object-Oriented Python`
===============================================

.. class:: cover

    ::

        Jonas Juselius <jonas.juselius@uit.no>
    
        HPC@UiT

.. raw:: pdf

   Transition Dissolve 1
   SetPageCounter 0
   PageBreak oneColumn

Object-Oriented Programming
---------------------------------------------------------
* In *procedual programming* the focus is on operations applied to data
* *Object-oriented programming* focuses on the data, together with operations
  on the data
* OOP *can* provide nice structure to programs and make programs more readable
  and well orgainzed
* The fundamental entity in OOP is the *class*, which acts as a stencil
  for creating  *objects*  (eg. strings, files, arrays, dicts...)
* Using classes we can cleanly separate the *interfaces* and the
  *implementation* (the 'what' from the 'how')
* Classes are used to hide the *implementation* details and *data* 
* Classes can be organized in parent-chiled hierarchies, where the children
  inherit properties of their parents

Classes and objects
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: class.py

Class variables
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: class2.py

Class customization
-----------------------------------------------------------
A feature of Python classes is that they can be made to behave
like standard types: E.g. printed, added, assigned, compared, called, etc.

The customization is done using special operator methods, e.g. ``__init__``,
``__str__``. Some other interesting operators are::

    __getitem__(self, key)  # Behave like a list or dict
    __getattr__(self, key)  # Add dynamic attributes to the object
    __call__(self, ...)     # Call the object like a function
    __eq__(self, other)     # Compare objs using ==
    __add__(self, other)    # Add stuff using +
    __len__(self)           # Respond to len()
    
For a full overview, refer to the chapter on operators_ in the *Python
Language Reference*. 

.. _operators: http://docs.python.org/2/reference/datamodel.html

Inheritance
-----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: inherit.py

Iterators
---------------------------------------------------------
Iterators allow us to make objects which behave like lists, i.e. they can be
looped over.

.. code-block:: python
    :linenos:
    :include: iter.py

Functional programming 
---------------------------------------------------------
* Functional programming emphasizes programming with functions (in the
  mathematical sense)
* In functional programming, variables are not allowed!
* Instead of loops, recursion is used (or map, filter, reduce)
* Programming functionally gives robust code

.. code-block:: python
    :linenos:
    :include: state.py

Functional programming 
---------------------------------------------------------

If we avoid stateful variables, whole classes of possible bugs become
impossible.

.. code-block:: python
    :linenos:
    :include: nostate.py

Ordering of statements no longer matter.

Functional programming 
---------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: functional.py

Decorators
---------------------------------------------------------
* Decorators are special functions which take functions as input and return a
  new function
* Decorators can be seen as function transformations 
* Decorators allow you to inject or modify code in functions (or classes)

.. code-block:: python
    :linenos:
    :include: decorate.py

Zen of objects
---------------------------------------------------------

* Keep your classes small
* Keep your interfaces smaller
* Don't add unnecessary data to objects
* Explicit data is better than implcit
* Methods that don't modify or use class data are better
* Immutability rules

