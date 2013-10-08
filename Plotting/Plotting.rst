.. role:: cover

=====================================
:cover:`Visualization and plotting`
=====================================

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

* Plotting data
* Plotting images
* Plotting maps
* 3D visualization

.. raw:: pdf

   PageBreak 
   Transition Dissolve 0

Introduction
----------------------------------------------------------

Python has many powerful and easy to use plotting libraries. We will look at
the following libraries:

Matplotlib:
    Matplotlib has a large collection of 2D and 3D plotting functions. The
    general recipe for working with matplotlib is modifying examples from 
    http://matplotlib.org/gallery.html
Basemap:
    Flexible plotting library for plotting data on map backgrounds. Based on
    matplotlib.
Mayavi:
    Powerful 3D plotting library based on VTK. Very similar interfaces as
    matplotlib.

Matplotlib principles
----------------------------------------------------------
* matplotlib has two major interfaces: pyplot and pylab
* matplotlib is a state machine: plots exist somewhere in some global state
* matplotlib operates with primary concepts:
    Figure: figures are like a canvas, eg. the complete "plot" 
    Axes: plots are build from axes, eg. the stuff to be plotted
* Plots can be subdivided with::

    subplot(nrows, ncols, plotnum)
* Some important procedures::

    plot(), figure(), subfigure(), gca(), gcf(), cla(), clf()
* Plots can be drawn on the screen with ``show()`` saved to disk ``savefig()``

Simple plotting
----------------------------------------------------------
.. code-block:: python
    :include: oneline.py

Multiple lines
----------------------------------------------------------
.. code-block:: python
    :include: twolines.py

Multiple figures
----------------------------------------------------------
.. code-block:: python
    :include: twofigs.py

Subplots 
----------------------------------------------------------
.. code-block:: python
    :include: subplots.py

Piechart 
----------------------------------------------------------
.. code-block:: python
    :include: piechart.py

Images
----------------------------------------------------------
.. code-block:: python
    :include: lena.py

3D plots 
----------------------------------------------------------
.. code-block:: python
    :include: 3dplot.py

Plotting data on a map
----------------------------------------------------------
.. code-block:: python
    :include: map_contour.py

Interactice 3D-plotting with Mayavi
----------------------------------------------------------
.. code-block:: python
    :include: boy.py


