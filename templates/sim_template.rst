{{sim_name}}
============

.. raw:: html

   <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
   <script type="text/javascript" src="../../scripts/bootstrap-slider.js"></script>
   <script>$('head').append('<link type="text/css" rel="stylesheet" href="../../scripts/bootstrap-slider.css">');</script>
   <script>$('#dLabelLocalToc').addClass('hidden');</script>
   <script>$('.navbar-nav').first().append('<li><a href="../index.html">&#10094; Back to Simulation Set</a></li>');</script>
   
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

   <button type="button" id="left_button" class="btn btn-primary btn-sm">&#10094;</button>
   <span>     </span>
   <input id="epoch" data-slider-id='epochSlider' type="text" data-slider-min="0"
    data-slider-max="{{num_epochs}}" data-slider-step="1" data-slider-value="0"
    data-slider-tooltip="hide"/>
   <span>     </span>
   <button type="button" id="right_button" class="btn btn-primary btn-sm">&#10095;</button>   
   <br><br>

   <a id="epoch_link">
   <h2 id="epoch_header"></h2>
   {% for key, name in names.items %}
   <figure style="display: inline-block;">
   <figcaption><h4>{{name}}</h4></figcaption>
   <img id="img_{{key}}" width="450" />
   </figure>
   {% endfor %}
   </a>
   
   <script>

   var num_epochs = {{num_epochs}};
   var names = [
   {% for short_name in names %}
       "{{short_name}}",
   {% endfor %}    
   ];

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
   
   var epochSlider = $("#epoch").slider();
   $("#epoch").on("slide", function(slideEvt) {
       set_links(slideEvt.value);
   });

   $("#left_button").click(function() {
       var value = epochSlider.slider("getValue");
       if (value > 0) {
           set_links(value-1);
           epochSlider.slider("setValue", value-1);
       }
   });

   $("#right_button").click(function() {
       var value = epochSlider.slider("getValue");
       if (value < num_epochs) {
           set_links(value+1);
           epochSlider.slider("setValue", value+1);
       }	   
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

