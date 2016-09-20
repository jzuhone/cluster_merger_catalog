.. raw:: html

   <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
   <script>$('#dLabelLocalToc').addClass('hidden');</script>
      
.. _{{name}}:

{{set_name|safe}}
============

Relevant Papers
---------------

{% for set_journal in set_journals %}
* `{{set_journal.0|safe}} <{{set_journal.1}}>`_
{% endfor %}

Set Characteristics
-------------------

* Code: {{code}}
* Simulation type: {{sim_type}}
* Box size: *L* = {{box_size}}
* Finest cell size: :math:`\Delta{x}_{\rm min}` = {{cell_size}}
* Primary cluster mass: :math:`{{primary_mass}}`

Notes
-----

{% for note in notes %}
* {{note|safe}}
{% endfor %}

Cosmology
---------

{% if cosmo_warning %}

.. note::

   For non-cosmological simulations such as this one, a cosmology and redshift
   are assumed for the purposes of calculating distance and redshift-dependent quantities.

{% endif %}

* :math:`\Lambda{\rm CDM}` cosmology
* :math:`H_0 = 71~{\rm km~s^{-1}~Mpc^{-1}}`
* :math:`\Omega_m = 0.27`
* :math:`\Omega_\Lambda = 0.73`	  
{% if cosmo_warning %}
* :math:`z = {{redshift}}` for all epochs
{% endif %}

Simulations
-----------

{{sim_notes|safe}}

.. toctree::
   :maxdepth: 1
      
{% for sim_page in sim_pages %}      

   {{sim_page|safe}}/index

{% endfor %}

Acknowledgements
----------------

{{acks|safe}}
