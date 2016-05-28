{{sim_name}}
============

.. raw:: html
   
   <script>
      function get_files(fileno, sim, timestr) {
         window.open("get_files.html?sim="+sim+"&fileno="+fileno,"_blank");
      }
   </script>
   
{% for fileno, time, imgs in info %}

{{time}}
------------

.. raw:: html

   <a href="" onclick="get_files('{{fileno}}', '{{sim}}', '{{time}}', '{{sim_name}}')">
   <img src={{imgs.xray_emissivity}} width="350" />
   </a>
   <a href="" onclick="get_files('{{fileno}}', '{{sim}}', '{{time}}', '{{sim_name}}')">
   <img src={{imgs.kT}} width="350" />
   </a>
   <a href="" onclick="get_files('{{fileno}}', '{{sim}}', '{{time}}', '{{sim_name}}')">
   <img src={{imgs.total_density}} width="350" />
   </a>

{% endfor %}
