.. raw:: html

   <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
   <script>$('#dLabelLocalToc').addClass('hidden');</script>
      
.. _{{name}}:

{{set_name|safe}}
============

Set Characteristics
-------------------

* Original paper: `{{set_journal|safe}} <{{ads_link}}>`_
* Code: {{code}}
* Simulation type: {{sim_type}}
* Box size: *L* = {{box_size}} Mpc
* Finest cell size: :math:`\Delta{x}_{\rm min}` = {{cell_size}} kpc
* Primary cluster mass: :math:`{{primary_mass}}`

Cosmology
---------

.. note::

   For non-cosmological simulations such as this one, a cosmology is assumed for the
   purposes of calculating distance and redshift-dependent quantities.
   
* :math:`\Lambda{\rm CDM}` cosmology
* :math:`z = 0.05` for all epochs
* :math:`H_0 = 71~{\rm km~s^{-1}~Mpc^{-1}}`
* :math:`\Omega_m = 0.27`
* :math:`\Omega_\Lambda = 0.73`

Simulations
-----------

For the following simulations, :math:`R` is the mass ratio betwen the two clusters and :math:`b` is the initial
impact parameter in kpc.

.. toctree::
   :maxdepth: 1
      
{% for sim_page in sim_pages %}      

   {{sim_page}}/index_z

{% endfor %}
