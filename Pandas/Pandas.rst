.. role:: cover

==================================
:cover:`Introduction to Pandas`
==================================

.. class:: cover

    ::

        Dan Jonsson <dan.jonsson@uit.no>

        HPC@UiT

.. raw:: pdf

   SetPageCounter 0
   Transition Dissolve 1
   PageBreak oneColumn

About Pandas
----------------------------------------------------------

* Pandas was started by Wes McKinney in 2008, because he was
  frustrated with working in R.
* Pandas is a data manipulation tool built on top of NumPy.
* Pandas focus on fast, intuitive data structures and data
  manipulation capabilities.
* Pandas aims to be the ultimate data tool for Python.
* Pandas is designed to enable Python to become a competitive
  statistical computing platform.
* Pandas is licensed using the New BSD Licence.
* Pandas home page: http://pandas.pydata.org

.. raw:: pdf

   PageBreak
   Transition Dissolve 0

Pandas features
----------------------------------------------------------

* A set of labeled array data structures, the primary of which are
  Series/TimeSeries and DataFrame
* Index objects enabling both simple axis indexing and multi-level /
  hierarchical axis indexing
* An integrated group by engine for aggregating and transforming data
  sets
* Date range generation (date_range) and custom date offsets enabling
  the implementation of customized frequencies
* Input/Output tools: loading tabular data from flat files (CSV,
  delimited, Excel 2003), and saving and loading pandas objects from
  the fast and efficient PyTables/HDF5 format.
* Memory-efficent sparse versions of the standard data structures
  for storing data that is mostly missing or mostly constant (some
  fixed value)
* Moving window statistics (rolling mean, rolling standard deviation, etc.)
* Static and moving window linear and panel regression


------


==========  ==================================================
Pandas data structures
--------------------------------------------------------------
Name       	Description
==========  ==================================================
Series      1D labeled homogeneously-typed array
TimeSeries  Series with index containing datetimes
DataFrame   General 2D labeled, size-mutable tabular structure
            with potentially heterogeneously-typed columns
Panel       General 3D labeled, also size-mutable array
==========  ==================================================

.. raw:: pdf

   PageBreak
   Transition Dissolve 0
