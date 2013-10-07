.. role:: cover

==================================
:cover:`Introduction`
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
* Python is great!

.. raw:: pdf

   PageBreak 
   Transition Dissolve 0

About this workshop
----------------------------------------------------------

Day 1:
    * Focus will be on developing essential problem solving skills and
      familarity with useful libraries
    * Text and file processing skills are essential for day-to-day work
    * Working with numeric data is imperative to many scientists

Day 2:
    * Focus will be on program development, and strategies for writing longer
      programs
    * Techniques for avoiding messing (everything) up
    * Python as a replacement for Excel, Matlab and Mathematica


Installing missing library components
----------------------------------------------------------

* Canopy has a nice installer where you can install missing components
* Access to large parts of the repository is restricted (unless you pay 199$)
* Instead we shall use the standard Python installer
  
Open a terminal: ``xterm || cmd.exe || Terminal.app``  

.. code-block:: shell

    $ easy_install pip  # pip is better than easy_install
    $ pip install docopt
    $ pip install pp

Downloading the examples
----------------------------------------------------------

# Start SmartGit
# Solmeny swear that your use is non-commericial
# Select ``Project -> Clone``
# Fill in the URL: http://github.com/bakerjonas/python-tutorials.git
# Save the project where you can find it easily (eg. Desktop)

Getting help
----------------------------------------------------------
In iPython:

.. code-block:: pycon
    
    >>> dir?
    >>> dir()             # dir() is a Python builtin function
    >>> dir(__builtin__)
    >>> dir("foo")
    >>> dir(42)

| Least but not last: 
|   http://docs.python.org
|   http://google.com 

Finally
----------------------------------------------------------

* You have completed the syntax traning, now we'll put your new skills to use!
* Learning pogramming is a livelong endeavour

