.. raw:: html

   <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
   <script>$('#dLabelLocalToc').addClass('hidden');</script>
   <script>$('.navbar-nav').first().append('<li><a href="../simulations.html">&#10094; Simulation Data</a></li>');</script>
   
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
