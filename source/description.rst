.. _description:

Description of the Data
=======================

This page describes the physics and setup of the simulations, and the types of data that can be found in the
catalog. 

General Simulation Physics and Algorithms
-----------------------------------------

The binary merger simulation data presented here comes from simulations performed using the
`FLASH code <http://flash.uchicago.edu>`_, an N-body/hydrodynamics adaptive mesh refinement
astrophysical simulation code. In general, each simulation employs the following physics and 
algorithms:

* Each simulation is simulated on an adaptive mesh refinement (AMR) grid, with varying resolution throughout
  the domain based on the refinement criteria of a) sharp jumps in density and temperature and b) matter
  density. 
* The hydrodynamics of the simulations are modeled using the Piecewise-Parabolic Method (PPM, 
  `Colella & Woodward 1984 <http://adsabs.harvard.edu/abs/1984JCoPh..54..174C>`_). 
* Each simulation assumes an ideal gas law equation of state with :math:`\gamma = 5/3` and primordial
  abundances of H/He with trace amounts of metals, yielding a mean molecular weight of :math:`\mu = 0.6`.
* The dark matter in the simulations is modeled by an N-body solver for a collection of collisionless
  massive particles, which have their masses mapped onto the grid cells for interaction with the gas. 
* The self-gravity of the gas and dark matter in the simulations is computed using a multigrid solver.
* The simulations do not include non-adiabatic processes such as heating or cooling. 

More information on the particular physical and algorithmic characteristics of the simulations can be found
in the accompanying papers, the links to which are given on each simulation set's page.

General Simulation Initial Conditions
-------------------------------------

Generally, the simulations are set up as two spherically symmetric galaxy clusters. The thermodynamic gas 
profiles are set up in hydrostatic equilibrium with the gravitational potential defined by both the dark 
matter and the gas mass. The dark matter particle radii and speeds are set up such that the dark matter
is in virial equilibrium with the gravitational potential defined by both the dark matter and the gas mass. 
The particle position vectors are set assuming spherical symmetry, and the velocity vectors are set assuming
isotropy. 

The two clusters are situated in a large simulation domain, separated by roughly the sum of their virial
radii, on a mutual bound orbit, with a relative velocity roughly equivalent to their free-fall velocity 
from infinity. Where the initial profiles of the gas quantities overlap, per-volume quantities such as
density and pressure are simply summed in each cell, whereas per-mass quantities such as velocity and
temperature are computed by mass-weighting. 

The specific details of the simulations, including the initial radial profiles of the gas and dark matter, 
the initial masses, bulk velocities, and impact parameters, and other information can be found in the 
accompanying papers, the links to which are given on each simulation set's page. 

FITS Files
----------

The data presented here consists of FITS image and table files, either slices or projections of the original
3D data along particular lines of sight. The various types of files that make up the data are
described below. The pixel scale of each FITS file is equivalent to the finest cell size of the
simulation, which is given on each simulation set's page. The fields which are stored in each file are files
are listed on the page for a particlar epoch's files.

Slices
++++++

Slices are taken along the z = 0 plane of the simulation axis, for a number of different fields. Which fields
are in the FITS file depends on the simulation, but most of them contain fields such as density, temperature,
velocity, etc.

Projections
+++++++++++

Projections are taken along several lines of sight. Currently, these include the three 
major axes of the simulation domain: x, y, and z. In the future, projections along off-axis 
directions will be added. For distance/redshift dependent quantities, the angular scale is determined by
the redshift and the given cosmology, which is in the notes for the simulation. Projected quantities typically
include X-ray emissivity, total matter density, projected temperature, etc.

Fields related to the (S-Z) effect are also computed, using the `SZpack library <http://www.cita.utoronto.ca/~jchluba/Science_Jens/SZpack/SZpack.html>`_
to compute the S-Z signal, including thermal and kinetic contributions as well as relativistic
corrections. More details on how these projections were computed can be found `here <http://yt-project.org/doc/analyzing/analysis_modules/sunyaev_zeldovich.html>`_.
They are stored in separate FITS files from the other projections. 

.. |photon_simulator| replace:: ``photon_simulator`` analysis module of yt
.. _photon_simulator: http://yt-project.org/doc/analyzing/analysis_modules/photon_simulator.html

X-ray Events
++++++++++++

The X-ray events files are standard events files which can be manipulated and analyzed with standard
X-ray analysis tools, such as `ds9 <http://ds9.si.edu>`_, `CIAO <http://cxc.cfa.harvard.edu/ciao/>`_, and the 
`HEASOFT software suite <http://heasarc.nasa.gov/lheasoft/>`_. The events have been generated using the
|photon_simulator|_ and have been convolved with the ACIS-I on-axis responses, assuming an exposure time of
50 ks. The pixel size corresponds to the width of the finest simulation cell size, instead of the pixel scale of
the detector. These files can be used to produce images and spectra. 
