.. _faqs:

Frequently Asked Questions
==========================

What software can I use to analyze this data?
---------------------------------------------

Since the primary data products are FITS images and tables, you can use the standard tools
that work with astronomical data in the FITS format, such as:

* `ds9 <http://ds9.si.edu>`_
* `HEASOFT <http://heasarc.nasa.gov/lheasoft/>`_
* `CIAO <http://cxc.cfa.harvard.edu/ciao/>`_
* `AstroPy <http://www.astropy.org>`_
* `pyregion <http://pyregion.readthedocs.io/en/latest/>`_
* `APLpy <https://aplpy.github.io/>`_
* `Glue <http://www.glueviz.org/>`_
* etc. 

`yt also has support for analyzing and visualizing FITS image and X-ray event data. <http://yt-project.org/doc/examining/loading_data.html#fits-data>`_

Why does the resolution appear to be non-uniform in many of the images?
-----------------------------------------------------------------------

This is because it actually is non-uniform. These simulations are run with
`adaptive mesh refinement (AMR) <https://en.wikipedia.org/wiki/Adaptive_mesh_refinement>`_,
a technique for solving physics equations on a mesh which allows for different parts of the
grid to be at higher resolution than others. In these simulations, the mesh is refined on
sharp jumps in the density and temperature (e.g., shocks and cold fronts), as well as on
regions of high density (e.g., the cores of clusters). In static mesh refinement (SMR) simulations,
the refinement pattern is set from the beginning of the simulation and is static in time. 
More details on how the mesh refinement in these simulations works can be found in the original 
papers associated with the simulations or in any of the method papers associated with AMR/SMR codes (e.g., 
`FLASH <http://www.sciencedirect.com/science/article/pii/S0167819109000945>`_,
`Enzo <http://adsabs.harvard.edu/abs/2014ApJS..211...19B>`_, or 
`Athena <http://adsabs.harvard.edu/abs/2008ApJS..178..137S>`_).

Why are the *Chandra* events not at the normal resolution? Where are the chips?
-------------------------------------------------------------------------------

These are not "standard" X-ray events files. The main differences with normal events files are:

* The pixel sizes correspond to the minimum resolution of the simulation, given the angular diameter
  distance to the source
* A uniform ACIS-I response has been assumed over the entire image
* No PSF smoothing has been applied, since the pixel sizes are much larger than the PSF

The idea is not to create an exact simulation, but one that approximates the statistical
properties of what the source would look like while allowing one to use standard X-ray tools
to analyze the spectral and spatial properties of the data. If you have any issues applying
standard X-ray analysis to these files,
`submit a bug report <https://github.com/jzuhone/cluster_merger_catalog/issues/>`_.

Why is background not included in the simulated X-ray event files?
------------------------------------------------------------------

Though the events have been simulated for a particular detector, *Chandra*'s ACIS-I, it 
seemed prudent to not include background events and instead let the end-user decide
what background to simulate, if any. For example, one could use background events from
the `ACIS blank-sky background files <http://cxc.harvard.edu/ciao/threads/acisbackground/>`_. 

Why do I sometimes see colored circles circling around instead of the images?
-----------------------------------------------------------------------------

This happens if the images are taking a while to load.

You didn't include projections in my favorite wavelength range. Why not?
------------------------------------------------------------------------

Mainly for lack of time, but also for lack of knowledge about the best way to go about it. If
you have some ideas of other derived data products that may be useful, do not hesitate to
`hit up the mailing list <https://groups.google.com/forum/#!forum/gcmc>`_.

I have some really cool data I'd like to include in the catalog. How can I do this?
-----------------------------------------------------------------------------------

If you have some galaxy cluster-related simulation data that fits within the goals of the catalog,
please `contact the mailing list <https://groups.google.com/forum/#!forum/gcmc>`_ and we can discuss getting it
set up. 

I downloaded one of the simulations in its entirety but I'm having some trouble unzipping the file. I'm on a Mac.
-----------------------------------------------------------------------------------------------------------------

There are known issues with opening large ZIP files on macOS. See
`this Stack Exchange note <http://superuser.com/questions/114011/extract-large-zip-file-50-gb-on-mac-os-x>`_ for
possible resolutions.

How do I cite the catalog?
--------------------------

Watch this space for a future journal reference. For now, include this text in the acknowledgments:

"This work made use of data from the Galaxy Cluster Merger Catalog (http://gcmc.hub.yt)."

Is the data licensed?
---------------------

The data is made available under `CC BY 4.0. <https://creativecommons.org/licenses/by/4.0/>`_

Where was the data generated?
-----------------------------

On each simulation set page there is an "Acknowledgments" section which details the computational resources used to
perform the simulations. At this time, most of the simulations and the mock observations were produced using `NASA's
Pleiades Supercomputer <http://www.nas.nasa.gov/hecc/resources/pleiades.html>`_.

I found a problem! How do I report it?
--------------------------------------

Please report any problems on our `Github issues page <https://github.com/jzuhone/cluster_merger_catalog/issues/>`_.

I have a question that isn't answered here. How do I get more information?
--------------------------------------------------------------------------

If you have a question related to the catalog itself, contact `the mailing list <https://groups.google.com/forum/#!forum/gcmc>`_.
If you have questions regarding yt, send mail to the `yt-users list <mailto:yt-users@lists.spacepope.org>`_.
