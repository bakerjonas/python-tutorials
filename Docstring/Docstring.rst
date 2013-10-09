.. role:: cover

==================================
:cover:`Docstrings and Sphinx`
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

* Documenting your code is important!
* Python has ``docstrings`` for this purpose: They allow you to document the
  file, classes and functions
* Sphinx is a Python program which extracts docstrings from your source code
  and produces nice documentation from it (pdf, html)

.. raw:: pdf

   PageBreak 
   Transition Dissolve 0

Example 
----------------------------------------------------------
.. code-block:: python
    :include: world.py

Using sphinx
----------------------------------------------------------
* For the complete story, see http://sphinx-doc.org
* To automatically generate documentation from you source code::

    $ sphinx-apidoc -F -o doc .
