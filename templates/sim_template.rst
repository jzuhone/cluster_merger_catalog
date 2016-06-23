{{sim_name}}
============

.. raw:: html
   
   <script>$('#dLabelLocalToc').addClass('hidden');</script>

   <h2>Click a link below to change the axis of projection.</h2>
{% if ax == "x" %}
   <h3>x  <a href="index_y.html">y</a>  <a href="index_z.html">z</a></h3>
{% elif ax == "y" %}
   <h3><a href="index_x.html">x</a>  y  <a href="index_z.html">z</a></h3>
{% elif ax == "z" %}
   <h3><a href="index_x.html">x</a>  <a href="index_y.html">y</a>  z</h3>
{% endif %}
 
{% for fileno, time, imgs in info %}

{{time}}
------------

.. raw:: html

   <a href="{{fileno}}.html" target="_blank">
   <figure style="display: inline-block;">
   <figcaption><h4>X-ray Emissivity</h4></figcaption>
   <img src={{imgs.xray_emissivity}} width="450" />
   </figure>
   <figure style="display: inline-block;">
   <figcaption><h4>Projected Temperature</h4></figcaption>
   <img src={{imgs.kT}} width="450" />
   </figure>
   <figure style="display: inline-block;">
   <figcaption><h4>Total Density</h4></figcaption>
   <img src={{imgs.total_density}} width="450" />
   </figure>
   <figure style="display: inline-block;">
   <figcaption><h4>Compton-y</h4></figcaption>
   <img src={{imgs.szy}} width="450" />
   </figure>
   </a>

{% endfor %}
