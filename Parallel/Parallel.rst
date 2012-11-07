.. role:: cover

=========================================
:cover:`Parallel programming in Python`
=========================================

.. class:: cover

    ::

        Jonas Juselius <jonas.juselius@uit.no>
    
        HPC@UiT

.. raw:: pdf

   SetPageCounter 0
   Transition Dissolve 1
   PageBreak oneColumn

About writing parallel programs
---------------------------------------------------------
* It's hard, hard, hard

Parallel paradigms
---------------------------------------------------------
* Trivial parallelism
* Multi-threading and shared memory
* Message passing

Parallel Python (SMP)
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: pp_smp.py

Parallel Python (Cluster)
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: pp_cluster.py

MPI: Point-to-point 
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: ptp_py.py

MPI: Point-to-point (numpy)
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: ptp_np.py

MPI: Scatter and gather 
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: scatter_py.py

MPI: Scatter and gather (numpy)
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: scatter_np.py

MPI: Reduction 
----------------------------------------------------------
.. code-block:: python
    :linenos:
    :include: quadr.py

