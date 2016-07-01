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

* Each simulation is simulated on an adaptive mesh refinement (AMR) grid, with varying resolution throughout
  the domain based, with refinement occuring on criteria such as a) sharp jumps in density and temperature, b) matter
  density, and c) selected regions such as the cluster center. Eventually, the catalog will include particle-based
  simulations as well.
* The equations of hydrodynamics or magnetohydrodynamics are modeled using a conservative finite-volume scheme (e.g.,
  PPM, `Colella & Woodward 1984 <http://adsabs.harvard.edu/abs/1984JCoPh..54..174C>`_). Magnetic fields are evolved
  such that the condition :math:`\nabla \cdot \bf{B} = 0` is met, whether by a constrained transport scheme or a
  divergence-cleaning method. Eventually, the catalog will include simulations peformed with smoothed particle
  hydrodynamics.
* Each simulation assumes an ideal gas law equation of state with :math:`\gamma = 5/3` and primordial
  abundances of H/He with trace amounts of metals, yielding a mean molecular weight of :math:`\mu = 0.6`.
* If dark matter is included, it is modeled by an N-body solver for a collection of collisionless
  massive particles, which interact with the gas component only via gravity.
* The gravity in the simulations is either modeled as a rigid gravitational potential associated with each cluster
  or by computing the self-gravity of the gas and dark matter using a Poisson solver.
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

Slices are taken along the z = 0 plane of the simulation axis, for a number of different fields. Which fields
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
