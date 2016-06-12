{{sim_name}}
============

.. raw:: html
   
   <script>
      function get_files(fileno, sim) {
         window.open("get_files.html?sim="+sim+"&fileno="+fileno,"_blank");
      }
   </script>
   <script>$('#dLabelLocalToc').addClass('hidden');</script>

{% for fileno, time, imgs in info %}

{{time}}
------------

.. raw:: html

   <a href="" onclick="get_files('{{fileno}}', '{{sim}}')">
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
