.. role:: cover

==================================
:cover:`Debugging`
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

* When your program crashes: *Read the trace carefully!*
* If you don't understand why things go wrong, or have the wrong result:
  sprinkle your code with ``print`` statements to get more information
* Alternatively::

    import pdb
    
    ...
    
    pdb.set_trace()

.. raw:: pdf

   PageBreak 
   Transition Dissolve 0

Fibonaci
----------------------------------------------------------
.. code-block:: python
   :include: fib_bug.py

File
----------------------------------------------------------
.. code-block:: python
   :include: file_bug.py

Input
----------------------------------------------------------
.. code-block:: python
   :include: input_bug.py

List
----------------------------------------------------------
.. code-block:: python
   :include: list_bug.py

Copy
----------------------------------------------------------
.. code-block:: python
   :include: list_copy_bug.py

Mutable
----------------------------------------------------------
.. code-block:: python
   :include: mutable_bug.py

Recursion
----------------------------------------------------------
.. code-block:: python
   :include: oroborous_bug.py

Range
----------------------------------------------------------
.. code-block:: python
   :include: range_bug.py

Scope
----------------------------------------------------------
.. code-block:: python
   :include: scope_bug.py

Sorting
----------------------------------------------------------
.. code-block:: python
   :include: sorting_bug.py

