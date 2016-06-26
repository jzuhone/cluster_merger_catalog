{{sim_name}}
============

.. raw:: html
   
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
 
{% for fileno, time, imgs in info %}

{{time}}
------------

.. raw:: html

   <div class="row">
     <div class="small-10 medium-11 columns">
       <div class="range-slider" data-slider data-options="display_selector: #sliderOutput3;">
         <span class="range-slider-handle" role="slider" tabindex="0"></span>
         <span class="range-slider-active-segment"></span>
       </div>
     </div>
     <div class="small-2 medium-1 columns">
       <span id="sliderOutput3"></span>
     </div>
   </div>

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
