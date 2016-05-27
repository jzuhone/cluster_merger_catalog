{{sim_name}}
============

.. raw:: html
   
   <script>
      function get_files(fileno, sim) {
         sessionStorage.setItem("fileno", fileno);
         sessionStorage.setItem("sim", sim);
         window.open("get_files.html","_blank");
      }
   </script>
   
{% for fileno, time, imgs, target in info %}

{{time}}
------------

.. raw:: html

   <a href="" onclick="get_files('{{fileno}}', '{{sim}}')">
   <img src={{imgs.xray_emissivity}} width="350" />
   </a>
   <a href="" onclick="get_files('{{fileno}}', '{{sim}}')">
   <img src={{imgs.kT}} width="350" />
   </a>
   <a href="" onclick="get_files('{{fileno}}', '{{sim}}')">
   <img src={{imgs.total_density}} width="350" />
   </a>

{% endfor %}
