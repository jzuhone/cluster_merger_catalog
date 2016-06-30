.. raw:: html

   <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
   <script>$('#dLabelLocalToc').addClass('hidden');</script>
      
.. _{{name}}:

{{set_name|safe}}
============

Set Characteristics
-------------------

* Original paper: `{{set_journal|safe}} <{{ads_link}}>`_
* Simulation type: {{sim_type}}
* Box size: *L* = {{box_size}} Mpc
* Finest cell size: :math:`\Delta{x}_{\rm min}` = {{cell_size}} kpc
* Primary cluster mass: :math:`{{primary_mass}}`

For the following simulations, :math:`R` is the mass ratio betwen the two clusters and :math:`b` is the initial
impact parameter in kpc. 

Simulations
-----------

.. toctree::
   :maxdepth: 1
      
{% for sim_page in sim_pages %}      

   {{sim_page}}/index_z

{% endfor %}
