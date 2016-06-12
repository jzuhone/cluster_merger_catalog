.. _{{name}}:

{{set_name}}
============

Set Characteristics
-------------------

* Original paper: `{{set_journal}} <{{ads_link}}>`_
* Box size: *L* = {{box_size}} Mpc
* Finest cell size: :math:`\Delta{x}_{\rm min}` = {{cell_size}} kpc

Simulations
-----------

.. toctree::
   :maxdepth: 1
      
{% for sim_page in sim_pages %}      

   {{sim_page}}

{% endfor %}
