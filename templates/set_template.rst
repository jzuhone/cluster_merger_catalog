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
  
Simulations
-----------

.. toctree::
   :maxdepth: 1
      
{% for sim_page in sim_pages %}      

   {{sim_page}}/index_z

{% endfor %}
