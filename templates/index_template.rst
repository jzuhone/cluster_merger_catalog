.. cluster_catalog documentation master file, created by
   sphinx-quickstart on Thu May 26 15:30:53 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to cluster_catalog's documentation!
===========================================

Contents:

.. toctree::
   :maxdepth: 1
      
{% for sim_page in sim_pages %}      

   {{sim_page}}

{% endfor %}

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

