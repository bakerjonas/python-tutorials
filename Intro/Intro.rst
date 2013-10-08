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

About this workshop
----------------------------------------------------------

Day 1:
    * Focus will be on developing essential problem solving skills and
      familiarity with useful libraries
    * Text and file processing skills are essential for day-to-day work
    * Working with numeric data is imperative to many scientists

Day 2:
    * Focus will be on program development, and strategies for writing longer
      programs
    * Techniques for avoiding messing (everything) up
    * Python as a replacement for Excel, Matlab and Mathematica


.. raw:: pdf

   PageBreak 
   Transition Dissolve 0

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

#. Start SmartGit
#. Solemnly swear that your use is non-commercial
#. Select ``Project -> Clone``
#. Fill in the URL: http://github.com/bakerjonas/python-tutorials.git
#. Save the project where you can find it easily (eg. Desktop)

About Python
----------------------------------------------------------

* Python is easy to learn
* Python is a real programming language
* Python programs can be written compactly and readably
* Python has a large collection of standard modules
* Python is an interpreted language
* Python is a dynamic language
* Python is extensible
* Python programs can be split into modules and reused in other Python programs
* Python is the language for you!

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

* By now you should have completed the basic Python course. 
  Now we'll put your new skills to use!
* Programming is about problem solving
* Learning programming is a lifelong endeavour

