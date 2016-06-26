{{sim_name}}
============

.. raw:: html

   <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
   <script type="text/javascript" src="../../scripts/slider.js"></script>
   <script>$('head').append('<link type="text/css" rel="stylesheet" href="../../slider/slider.css">');</script>
   <script>$('#dLabelLocalToc').addClass('hidden');</script>

   <h3>Click on one of the axes below to change the axis of projection.</h3>
   <ul>
{% for a in axes %}
   <li>
{% if ax != a %}
   <a href="index_{{a}}.html">
{% endif %}
   <h4>{{a}}</h4>
{% if ax != a %}
   </a>
{% endif %}
   </li>
{% endfor %}
   </ul>

   <h2 id="epoch_header"></h2>
   
   <div id='bar'></div>
   <br><br>

   <a id="epoch_link" target="_blank">
   <figure style="display: inline-block;">
   <figcaption><h4>X-ray Emissivity</h4></figcaption>
   <img id="xray" width="450" />
   </figure>
   <figure style="display: inline-block;">
   <figcaption><h4>Projected Temperature</h4></figcaption>
   <img id="temp" width="450" />
   </figure>
   <figure style="display: inline-block;">
   <figcaption><h4>Total Density</h4></figcaption>
   <img id="dens" width="450" />
   </figure>
   <figure style="display: inline-block;">
   <figcaption><h4>Compton-y</h4></figcaption>
   <img id="szy" width="450" />
   </figure>
   </a>
 
   <script>
   
   var girder_data = {};
   var epochs = {};
   
   {% for fileno, pngs in imgs.items %}
   girder_data["{{fileno}}"] = {};
   {% for key, link in pngs.items %}
   girder_data["{{fileno}}"]["{{key}}"] = "{{link}}";
   {% endfor %}
   {% endfor %}

   {% for fileno, epoch in epochs.items %}
   epochs["{{fileno}}"] = "{{epoch}}";
   {% endfor %}
   
   bar = new Slider({
       container: bar, 
       value: 0.7,
       onChange: function(value){
           console.log(value);
       }
   });
   
   $(document).ready(function () {
       set_links("0000");
   });
    
   function set_links(fileno) {
       document.getElementById("epoch_header").innerText = epochs[fileno];
       document.getElementById("epoch_link").innerText = fileno+".html";
       for (name in ["xray", "temp", "dens", "szy"]) {
           document.getElementById(name).href = girder_data[fileno]["links"][name];
       }
   }
   
   </script>

