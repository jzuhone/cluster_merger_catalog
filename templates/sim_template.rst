{{sim_name}}
============

.. raw:: html

   <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
   <script type="text/javascript" src="../../scripts/bootstrap-slider.js"></script>
   <script>$('head').append('<link type="text/css" rel="stylesheet" href="../../scripts/bootstrap-slider.css">');</script>
   <script>$('#dLabelLocalToc').addClass('hidden');</script>
   <script>$('.navbar-nav').first().append('<li><a href="../index.html">&#10094;  {{set_name}} Simulations</a></li>');</script>
   
   <h3>Click on one of the axes below to change the axis of projection.</h3>
{% for a in axes %}
{% if ax != a %}
   <a class="btn btn-primary" href="index_{{a}}.html" role="button">{{a}}</a>
{% else %}
   <a class="btn btn-primary" href="index_{{a}}.html" role="button" disabled>{{a}}</a> 
{% endif %}
{% endfor %}

   <h3>Use the slider to change the epoch of the merger, and click on the images to access the files.</h3>
   <br>
   
   <input id="epoch" data-slider-id='epochSlider' type="text" data-slider-min="0"
    data-slider-max="{{num_epochs}}" data-slider-step="1" data-slider-value="0"
    data-slider-tooltip="hide"/>
   <br><br>

   <h2 id="epoch_header"></h2>
   <a id="epoch_link">
   <figure style="display: inline-block;">
   <figcaption><h4>X-ray Emissivity</h4></figcaption>
   <img id="img_xray" width="450" />
   </figure>
   <figure style="display: inline-block;">
   <figcaption><h4>Projected Temperature</h4></figcaption>
   <img id="img_temp" width="450" />
   </figure>
   <figure id="fig_dens" style="display: inline-block;">
   <figcaption><h4>Total Density</h4></figcaption>
   <img id="img_dens" width="450" />
   </figure>
   <figure id="fig_szy" style="display: inline-block;">
   <figcaption><h4>Compton-y</h4></figcaption>
   <img id="img_szy" width="450" />
   </figure>
   </a>
   
   <script>
   
   var names = ["xray", "temp", "dens", "szy"];

   var filenos = [
   {% for fileno in filenos %}
       "{{fileno}}",
   {% endfor %}
   ];

   var girder_data = {
   {% for fileno, pngs in imgs.items %}
       "{{fileno}}": {
   {% for key, link in pngs.items %}
           "{{key}}":"{{link}}",
   {% endfor %}
       },
   {% endfor %}
   };
   
   var epochs = {
   {% for fileno, epoch in epochs.items %}
       "{{fileno}}": "{{epoch}}",
   {% endfor %}
   };
   
   $("#epoch").slider();
   $("#epoch").on("slide", function(slideEvt) {
       set_links(slideEvt.value);
   });

   $(document).ready(function () {
       set_links(0);
   });

   function set_links(num) {
       var fileno = filenos[num];
       document.getElementById("epoch_header").innerText = epochs[fileno];
       document.getElementById("epoch_header").textContent = epochs[fileno];
       document.getElementById("epoch_link").href = fileno+".html";
       for (var i = 0; i < names.length; i++) {
	   var img = document.getElementById('img_'+names[i]);
	   img.src = "../../images/loader.gif";
	   img.src = girder_data[fileno][names[i]];
       }
   }

   </script>

