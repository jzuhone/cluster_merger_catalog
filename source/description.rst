.. _description:

Description of the Data
=======================

This page describes the physics and setup of the simulations, and the types of data that can be found in the
catalog. 

General Simulation Physics and Algorithms
-----------------------------------------

The galaxy cluster merger simulation data presented here comes from state-of-the-art N-body and hydrodynamics
codes such as `FLASH <http://flash.uchicago.edu>`_ and `Athena <https://trac.princeton.edu/Athena/>`_. The
exact physics and algorithms employed by the simulations vary, but in general:

* Each simulation is simulated using an adaptive or static mesh refinement (AMR/SMR) grid 
  (`Berger and Colella 1989 <http://adsabs.harvard.edu/abs/1989JCoPh..82...64B>`_), with varying resolution 
  throughout the domain, with refinement occuring on criteria such as a) sharp jumps in density and temperature, 
  b) matter density, and c) selected regions such as the cluster center. Eventually, the catalog will include 
  particle-based simulations as well.
* The equations of hydrodynamics or magnetohydrodynamics are modeled using a conservative finite-volume scheme,
  employing Riemann solvers for evolving the flux of physical quantities and using high-order reconstruction
  schemes such as PPM (`Colella & Woodward 1984 <http://adsabs.harvard.edu/abs/1984JCoPh..54..174C>`_). Magnetic
  fields are evolved such that the condition :math:`\nabla \cdot \bf{B} = 0` is met, typically by a constrained
  transport scheme (CT, `Evans & Hawley 1988 <http://adsabs.harvard.edu/abs/1988ApJ...332..659E>`_). Eventually, 
  the catalog will include simulations peformed with smoothed particle hydrodynamics.
* Each simulation assumes an ideal gas law equation of state with :math:`\gamma = 5/3` and primordial
  abundances of H/He with trace amounts of metals, yielding a mean molecular weight of :math:`\mu = 0.6`.
* If dark matter is included, it is modeled by an N-body solver for a collection of collisionless
  massive particles, which interact with the gas component only via gravity.
* The gravity in the simulations is either modeled as a rigid gravitational potential associated with each cluster
  or by computing the self-gravity of the gas and dark matter using a Poisson solver (e.g., 
  `Ricker 2008 <http://adsabs.harvard.edu/abs/2008ApJS..176..293R>`_).
* Depending on the goals of the simulation study, other physics, such as viscosity, thermal conduction, radiative
  cooling, etc., may be included.
  
More information on the particular physical and algorithmic characteristics of the simulations can be found
in the accompanying papers, the links to which are given on each simulation set's page.

Types of Simulations
--------------------

The simulations presented here are of a number of different types. We describe each of these types in turn.

N-body/Hydrodynamic Binary Mergers
++++++++++++++++++++++++++++++++++

In these simulations, the two galaxy clusters are set up as two spherically symmetric, self-gravitating
collections of gas and dark matter. The thermodynamic gas profiles are set up in hydrostatic equilibrium
with the gravitational potential defined by both the dark matter and the gas mass. The dark matter particle
radii and speeds are set up such that the dark matter is in virial equilibrium with the gravitational
potential defined by both the dark matter and the gas mass. The particle position vectors are set assuming
spherical symmetry, and the velocity vectors are set assuming isotropy. 

The two clusters are situated in a large simulation domain, separated by a distance that is typically on the
order of the sum of their virial radii. They are given a relative velocity such that the clusters are moving
toward each other at the beginning of the simulation. They may or may not be on a bound orbit, and the impact
parameter may be nonzero.

If a magnetic field is included in the simulation, it is typically set up as a turbulent, tangled field with
using a power spectrum of fluctuations with minimum and maximum length scales. The field strength is such that
the magnetic pressure is a small fraction of the thermal pressure, and the average strength of the magnetic
field declines with radius from the cluster center.

The specific details of the simulations, including the initial radial profiles of the gas and dark matter, 
the initial masses, bulk velocities, and impact parameters, and other information can be found in the 
accompanying papers, the links to which are given on each simulation set's page. 

Hydrodynamic Binary Mergers with Rigid Gravitational Potentials
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This type of simulation is set up in much the same way as the previous kind, except that there is no dark matter,
the gas is not self-gravitating, and the gravitational potential is modeled by a sum of two rigid gravitational
potentials representing the dark matter halos which are evolved on a mutual orbit. This approximation is used when
a) computational speed is desired and b) the relevant characteristics of the simulations do not depend on accurately
modeling the effects of dynamical friction, mass loss, and tidal forces on the dark matter.

Cluster Mergers in Cosmological Simulations
+++++++++++++++++++++++++++++++++++++++++++

Coming soon! Watch this space.

FITS Files
----------

The data presented here consists of FITS image and table files, either slices or projections of the original
3D data along particular lines of sight. The various types of files that make up the data are
described below. The pixel scale of each FITS file is equivalent to the finest cell size of the
simulation, which is given on each simulation set's page. The fields which are stored in each file are files
are listed on the page for a particlar epoch's files.

Slices
++++++

Slices are taken along the merger plane for a number of different fields. Which fields
are in the FITS file depends on the simulation, but most of them contain fields such as density, temperature,
velocity, etc.

Projections
+++++++++++

Projections are taken along several lines of sight. Currently, these include the three 
major axes of the simulation domain: x, y, and z. In the future, projections along off-axis 
directions will be added. Distance/redshift dependent quantitie are determined by
the redshift and the given cosmology, which is given in the notes for the simulation. If the simulation
is not cosmological (such as the binary merger simulations), a standard cosmology and constant redshift is assumed.
Projected quantities typically include X-ray emissivity, total matter density, projected temperature, etc.

Fields related to the Sunyaev-Zeldovich (S-Z) effect are also computed for some simulations, using the
`SZpack library <http://www.cita.utoronto.ca/~jchluba/Science_Jens/SZpack/SZpack.html>`_
(`Chluba et al. 2012 <http://adsabs.harvard.edu/abs/2012MNRAS.426..510C>`_,
`Chluba et al. 2013 <http://adsabs.harvard.edu/abs/2013MNRAS.430.3054C>`_) to compute the S-Z signal,
including thermal and kinetic contributions as well as relativistic corrections. More details on how these projections
were computed can be found `here <http://yt-project.org/doc/analyzing/analysis_modules/sunyaev_zeldovich.html>`_.
They are stored in separate FITS files from the other projections. 

Galaxies
++++++++

Some of the simulations with dark matter particles have mock "galaxies". These are dark matter particles which have been
randomly drawn from the simulation, with a number per halo given by the mass-richness relation of
`Ford et al. 2014 <http://adsabs.harvard.edu/abs/2014MNRAS.439.3755F>`_. The galaxies are contained in FITS binary tables,
which include sky positions, line-of-sight velocities, an identifier for which halo each galaxy originally belonged to, and
unique IDs for every galaxy. These particles provide a way of measuring the kinematics of the merger from the perspective of
the collisionless material with a statistical significance that is comparable to that obtained from measured redshifts of
galaxies in real clusters. No redshift errors have been applied to the galaxy velocities, which is an exercise left to the end-user.

A ds9 region file is provided for each epoch and line-of-sight in addition to the FITS file, which allows the galaxy positions
to be plotted over the projections of the other fields. 

X-ray Events
++++++++++++

The X-ray events files are standard events files which can be manipulated and analyzed with standard
X-ray analysis tools, such as `ds9 <http://ds9.si.edu>`_, `CIAO <http://cxc.cfa.harvard.edu/ciao/>`_, and the 
`HEASOFT software suite <http://heasarc.nasa.gov/lheasoft/>`_. The events have been generated using the
`pyXSIM package <http://hea-www.cfa.harvard.edu/~jzuhone/pyxsim>`_ and have been convolved with the ACIS-I
on-axis responses, assuming an exposure time of 50 ks. The pixel size corresponds to the width of the finest
simulation cell size, instead of the pixel scale of the detector. These files can be used to produce images
and spectra. Eventually, event files for other instruments and exposure times will be included.

Important Things to Know About the Data
---------------------------------------

Coordinate Systems
++++++++++++++++++

The FITS image and table files contain one or more `WCS coordinate systems <http://fits.gsfc.nasa.gov/fits_wcs.html>`_.
The two most common are:

* Linear coordinates: This is a simple linear coordinate system which corresponds to the coordinate
  system of the original dataset. The length units are in kpc. For most of the FITS files, this is the
  first and primary WCS (i.e., the one that appears by default in ds9).
* Celestial coordinates: This is a celestial coordinate system in RA and Dec using the tangential
  projection. The angle units are in degrees. For most of the FITS files, this is the secondary WCS
  (i.e., "WCS a" in ds9).

For example, a header for one of the FITS images corresponding to a projected quantity may look like
this (only showing some keywords for clarity):

.. code::

   # HDU 4 in AM06_beta200_hdf5_plt_cnt_0130_proj_z.fits:
   NAXIS   =                    2 / number of array dimensions
   NAXIS1  =                 2048
   NAXIS2  =                 2048
   EXTNAME = 'KT      '           / extension name
   BTYPE   = 'kT      '
   BUNIT   = 'keV     '
   WCSAXES =                    2
   CRPIX1  =               1024.5
   CRPIX2  =               1024.5
   CDELT1  =     0.97653794699453
   CDELT2  =     0.97653794699453
   CUNIT1  = 'kpc     '
   CUNIT2  = 'kpc     '
   CTYPE1  = 'LINEAR  '
   CTYPE2  = 'LINEAR  '
   CRVAL1  =                  0.0
   CRVAL2  =                  0.0
   LATPOLE =                 90.0
   WCSNAME = 'yt      '
   WCSAXESA=                    2
   CRPIX1A =               1024.5
   CRPIX2A =               1024.5
   CDELT1A = -0.00028118222874698
   CDELT2A =  0.00028118222874698
   CUNIT1A = 'deg     '
   CUNIT2A = 'deg     '
   CTYPE1A = 'RA---TAN'
   CTYPE2A = 'DEC--TAN'
   CRVAL1A =                 30.0
   CRVAL2A =                 45.0
   LONPOLEA=                180.0
   LATPOLEA=                 45.0
   WCSNAMEA= 'celestial'
   RADESYSA= 'ICRS    '
   TIME    =    1.300254073176463

It can be seen here that the default WCS, ``WCSNAME = 'yt'``, is in linear coordinates, and the second
WCS, ``WCSNAMEA = 'celestial'``, is in celestial coordinates. The relationship between the two depends
on the angular diameter distance to the source, which depends on the redshift and the given cosmology.
This information is shown on each simulation set page.

To select a particular WCS in the JS9 interface, Use the "WCS" drop-down menu item and choose
the "alternate wcs" option to show the different options.
