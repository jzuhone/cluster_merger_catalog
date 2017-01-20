{{sim_name|safe}}
============

.. raw:: html

   <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
   <script>$('#dLabelLocalToc').addClass('hidden');</script>
   <script>$('.navbar-nav').first().append('<li><a href="../index.html">&#10094; Back to Simulation Set</a></li>');</script>
   <script type="text/javascript" src="../../scripts/bootstrap-slider.js"></script>
   <script>$('head').append('<link type="text/css" rel="stylesheet" href="../../scripts/bootstrap-slider.css">');</script>

   <br>
   <a id="sim_dl" href="{{sim_dl}}">Download all of the files from this particular simulation here ({{size}} GB).</a>
   
   <h3>Click on one of the axes below to change the axis of projection.</h3>
{% for a in axes %}
   <button type="button" class="btn btn-primary" id="button_{{a}}" onclick="change_axis('{{a}}')">{{a}}</button>
{% endfor %}

   <h3>Use the slider to change the epoch, and click on the images to access the files.</h3>
   <br>

   <span style="margin-right: 20px;">
   <button type="button" id="left_button" class="btn btn-primary btn-sm">&#10094;</button></span>
   <input id="epoch" data-slider-id='epochSlider' type="text" data-slider-min="0"
    data-slider-max="{{num_epochs}}" data-slider-step="1" data-slider-value="0"
    data-slider-tooltip="hide"/>
   <span style="margin-left: 20px;">
   <button type="button" id="right_button" class="btn btn-primary btn-sm">&#10095;</button></span>  
   <br><br>

   <a id="epoch_link">
   <h2 id="epoch_header"></h2>
   {% for key, name in names.items() %}
   <figure style="display: inline-block;">
   <figcaption><h4>{{name}}</h4></figcaption>
   <img id="img_{{key}}" width="450" />
   </figure>
   {% endfor %}
   </a>
   
   <script>

   var axis = "z";
   document.getElementById("button_z").disabled = true;
   
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
   {% for fileno, pngs in imgs.items() %}
       "{{fileno}}": {
   {% for key, axes in pngs.items() %}
           "{{key}}": { 
   {% for ax, link in axes.items() %}
               "{{ax}}":"{{link}}",
   {% endfor %}
           },
   {% endfor %}
       },
   {% endfor %}
   };
   
   var epochs = {
   {% for fileno, epoch in epochs.items() %}
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

   function change_axis(ax) {
       document.getElementById("button_"+axis).disabled = false;
       document.getElementById("button_"+ax).disabled = true;
       axis = ax;
       var fileno = filenos[epochSlider.slider("getValue")];
       var epoch_text = epochs[fileno]+", "+axis+" Projection";
       document.getElementById("epoch_header").innerText = epoch_text;
       document.getElementById("epoch_header").textContent = epoch_text;		 
       set_images(fileno);
   }
   
   function set_links(num) {
       var fileno = filenos[num];
       var epoch_text = epochs[fileno]+", "+axis+" Projection";
       document.getElementById("epoch_header").innerText = epoch_text;
       document.getElementById("epoch_header").textContent = epoch_text;
       document.getElementById("epoch_link").href = fileno+".html";
       set_images(fileno);
   }

   function set_images(fileno) {
       for (var i = 0; i < names.length; i++) {
           var img = document.getElementById('img_'+names[i]);
	       img.src = "../../images/loader.gif";
	       img.src = girder_data[fileno][axis][names[i]];
       }
   }

   </script>

