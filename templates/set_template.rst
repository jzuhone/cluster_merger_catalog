.. _{{name}}:

{{set_name|safe}}
============

Set Characteristics
-------------------

* Original paper: `{{set_journal|safe}} <{{ads_link}}>`_
* Box size: *L* = {{box_size}} Mpc
* Finest cell size: :math:`\Delta{x}_{\rm min}` = {{cell_size}} kpc

Simulations
-----------

.. toctree::
   :maxdepth: 1
      
{% for sim_page in sim_pages %}      

   {{sim_page}}/index

{% endfor %}
