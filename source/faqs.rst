.. _faqs:

Frequently Asked Questions
==========================

Why are you giving this data away?
----------------------------------

What software can I use to analyze this data?
---------------------------------------------

Why does the resolution appear to change in many of the images?
---------------------------------------------------------------

This is because it actually is changing. These simulations are run with
`adaptive mesh refinement (AMR) <https://en.wikipedia.org/wiki/Adaptive_mesh_refinement>`_,
a technique for solving physics equations on a mesh which allows for different parts of the
grid to be at higher resolution than others. In these simulations, the mesh is refined on
sharp jumps in the density and temperature (e.g., shocks and cold fronts), as well as on
regions of high density (e.g., the cores of clusters). More details on how the AMR in these
simulations works can be found in the original papers associated with the simulations or
in the `most recent FLASH code paper <http://www.sciencedirect.com/science/article/pii/S0167819109000945>`_.

Why is background not included in the simulated X-ray event files?
------------------------------------------------------------------

Though the events have been simulated for a particular detector, *Chandra*'s ACIS-I, it 
seemed prudent to not include background events and instead let the end-user decide
what background to simulate, if any. For example, one could use background events from
the `ACIS blank-sky background files <http://cxc.harvard.edu/ciao/threads/acisbackground/>`_. 

You didn't include projections in my favorite wavelength range. Why not?
------------------------------------------------------------------------

Mainly for lack of time, but also for lack of knowledge about the best way to go about it. If
you have some ideas of other derived data products that may be useful, do not hesitate to contact
`John ZuHone <mailto:jzuhone@gmail.com>`_.

I have some really cool data I'd like to include in the catalog. How can I do this?
-----------------------------------------------------------------------------------

If you have some galaxy cluster-related simulation data that fits within the goals of the catalog,
pease get in touch with `John ZuHone <mailto:jzuhone@gmail.com>`_ and we can discuss getting it
set up. 

How do I cite the catalog?
--------------------------

I found a problem! How do I report it?
--------------------------------------

Please report any problems on our `Bitbucket issues page <https://bitbucket.org/jzuhone/cluster_merger_catalog/issues/>`_.

I have a question that isn't answered here. How do I get more information?
--------------------------------------------------------------------------

If you have a question related to the catalog itself, contact `John ZuHone <mailto:jzuhone@gmail.com>`_.
If you have questions regarding yt, send mail to the `yt-users list <mailto:yt-users@lists.spacepope.org>`_.
