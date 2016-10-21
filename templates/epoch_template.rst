
.. raw:: html
   
    <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
    <script>$('#dLabelGlobalToc').addClass('hidden');</script>
    <script>$('#dLabelLocalToc').addClass('hidden');</script>
    <script>$('.navbar-nav').first().append('<li><a href="index.html">&#10094; Back to Simulation</a></li>');</script>
    <script src="../../lightbox/js/lightbox.js"></script>
    <script>$('head').append('<link rel="stylesheet" href="../../lightbox/css/lightbox.css"/>');</script>
    <script>$('head').append('<link type="text/css" rel="stylesheet" href="../../js9/js9support.css">');</script>
    <script>$('head').append('<link type="text/css" rel="stylesheet" href="../../js9/js9.css">');</script>
    <script>$('head').append('<link type="text/css" rel="stylesheet" href="../../scripts/modal.css">');</script>
    <script type="text/javascript" src="../../js9/js9support.min.js"></script>
    <script type="text/javascript" src="../../js9/js9.min.js"></script>
    <script type="text/javascript" src="../../js9/js9plugins.js"></script>
   
{{sim_name|safe}}: {{timestr}}
=========================

.. raw:: html

   <a class="btn btn-primary" href="{{prev_link}}" role="button" {{dis_prev}}>&#10094; Previous Epoch</a>
   <a class="btn btn-primary" href="{{next_link}}" role="button" {{dis_next}}>&#10095; Next Epoch</a>
   <br><br>
   <a id="epoch_dl" href="{{epoch_dl}}">Download all of the files from this particular epoch here ({{size}} GB).</a>
   <br><br>

{% if set_physics|length > 0 %}
Explore similar simulations with different input physics at the same epoch using these links:

{% for key, value in set_physics.items %}
{% if key != sim %}
.. |{{key}}_epoch_link| replace:: {{value|safe}}: {{timestr}}
.. _{{key}}_epoch_link: ../{{key}}/{{fileno}}.html
{% endif %}
{% endfor %}
  
{% for key in set_physics %}
{% if key != sim %}
* |{{key}}_epoch_link|_
{% endif %} 
{% endfor %}
{% endif %}

To make the best use out of this page:

* Click on any image to enlarge it.
* Download FITS files from the links or load them into the JS9 window at the bottom of the page.
* Change the axis of projection for the images and links using the drop-down menu. 

.. note::

   Typically, images shown here are zoomed-in; the width of the images in the FITS files are usually
   larger, spanning the original simulation domain or a large portion of it.

.. raw:: html
 
   <h2>Slices</h2>

The slice FITS file contains the following fields:

{% for field, descr in slice_fields.items %}
* ``"{{field}}"``: {{descr}}
{% endfor %}
  
.. raw:: html

    <a id="slice_fits">FITS File Download</a><br>
    <a id="slice_js9" href="#js9">Open FITS file in JS9 below</a>
    <br><br>	       
    {% for key, name in slice_names.items %}
    <figure style="display: inline-block;">
    <figcaption><h4>{{name}}</h4></figcaption>
    <a id="big_slice_{{key}}" data-lightbox="lb_slice_{{key}}" ><img id="slice_{{key}}" width="450" /></a>
    </figure>
    {% endfor %}
    <br>

    <h2>Projected Quantities</h2>

    Change the projection direction:
    <select id="proj_axis">
    </select>
    <br>

    <h3>Projections</h3>

The projection FITS file contains the following fields:

{% for field, descr in proj_fields.items %}
* ``"{{field}}"``: {{descr}}
{% endfor %}

.. raw:: html
    
    <a id="proj_fits">FITS File Download</a><br>
    <a id="proj_js9" href="#js9">Open FITS file in JS9 below</a>
    <br><br>
    {% for key, name in proj_names.items %}
    <figure style="display: inline-block;">
    <figcaption><h4>{{name}}</h4></figcaption>
    <a id="big_proj_{{key}}" data-lightbox="lb_proj_{{key}}" ><img id="proj_{{key}}" width="450" /></a>
    </figure>
    {% endfor %}
    <br><br>
    
    {% if galaxies %}
    <h3>Galaxies</h3>

    The galaxies FITS file contains positions, velocities, IDs, and original halo information
    for a set of galaxy particles.<br><br> 
    <a id="galaxies_fits">FITS File Download</a><br>
    <a id="galaxies_reg">Region File Download</a><br><br>
    <!-- <a id="galaxies_js9">Open region file in JS9 below</a> -->
    <!-- <br><br> -->
    <figure style="display: inline-block;">
    <figcaption><h4>Galaxy Positions and Velocities</h4></figcaption>
    <a id="big_galaxies_ppv" data-lightbox="lb_galaxies_ppv" ><img id="galaxies_ppv" width="450" /></a>
    </figure>	
    <br><br>
    {% endif %}

{% if sz_fields|length > 0 %}

.. raw:: html

    <h3>S-Z Projections</h3>
    
The S-Z FITS file contains the following fields:

{% for field, descr in sz_fields.items %}
* ``"{{field}}"``: {{descr}}
{% endfor %}

.. raw:: html

    <a id="SZ_fits">FITS File Download</a><br>
    <a id="SZ_js9" href="#js9">Open FITS file in JS9 below</a>
    <br><br>    
    {% for key, name in sz_names.items %}
    <figure style="display: inline-block;">
    <figcaption><h4>{{name}}</h4></figcaption>
    <a id="big_SZ_{{key}}" data-lightbox="lb_SZ_{{key}}" ><img id="SZ_{{key}}" width="450" /></a>
    </figure>
    {% endfor %}

    <br><br>
    
{% endif %}

    <h3>X-ray Events</h3>
    
    The events FITS file contains an X-ray event list.
    <br><br>	 
    <a id="cxo_evt_fits">FITS File Download</a><br>
    <a href="../../files/acisi_rmfs.tar.gz">Download Response Files</a><br>
    <a id="cxo_evt_js9" href="#js9">Open FITS file in JS9 below</a>
    <br><br>
    <figure style="display: inline-block;">
    <figcaption><h4>X-ray Counts (<em>Chandra</em> ACIS-I, 50 ks)</h4></figcaption>
    <a id="big_cxo_evt_counts" data-lightbox="lb_cxo_evt_counts" ><img id="cxo_evt_counts" width="450" /></a>
    </figure>
    <br><br>

    <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#hubModal">Get access to these files on the yt Hub and run Jupyter notebooks.</button>

    <a name="js9"></a>
    <h2>JS9 Interface</h2>
    
    Once an image file is loaded, use the drop-down menu below to switch between 
    the different fields in the file.<br>

    <select id="fits_ext"></select>
    <br>

    <div class="JS9Menubar"></div>
    <div class="JS9"></div>
    <div style="margin-top: 2px;">
    <div class="JS9Colorbar"></div>
    </div>

    <script>

        var axisList = document.getElementById("proj_axis");
        var fitsList = document.getElementById("fits_ext");

        var default_js9 = {"slice":"DENSITY",
                           "proj":"XRAY_EMISSIVITY",
                           "SZ":"180_GHZ",
                           "cxo_evt":"EVENTS"};

        var girder_data = {
        {% for itype, axes in data.items %}
            "{{itype}}": {
        {% for ax, ftypes in axes.items %}
                "{{ax}}": {"fits": "{{ftypes.fits}}",		
        {% if itype|stringformat:"s" == "galaxies" %}
                           "reg": "{{ftypes.reg}}",
        {% endif %}                   
                           "pngs": {
        {% for key, link in ftypes.pngs.items %}
                               "{{key}}": "{{link}}",
        {% endfor %}
                       },},
        {% endfor %}
            },
        {% endfor %}
        };

        var axes = [
        {% for ax in data.proj %}
            "{{ax}}",
        {% endfor %}
        ];

        $(document).ready(function () {

            //var myModal = document.getElementById('hubModal');  
            //var myLink = document.getElementById("hubLink");
            //var mySpan = document.getElementById("closeModal");
            //myLink.onclick = function() {
            //    myModal.style.display = "block";
            // }
            //mySpan.onclick = function() {
            //    myModal.style.display = "none";
            //}
            //window.onclick = function(event) {
            //    if (event.target == modal) {
            //        modal.style.display = "none";
            //    }
            //}
            //document.getElementById('hubFolder').href = "{{hub_folder}}";

            show_files('slice', 'z');
            fits_link('slice', 'z');
            show_files('proj', 'z');
            fits_link('proj', 'z');
            {% if sz_fields|length > 0 %}
            show_files('SZ', 'z');
            fits_link('SZ', 'z');
            {% endif %}
            show_files('cxo_evt', 'z');
            fits_link('cxo_evt', 'z');
            {% if galaxies %}
            show_files('galaxies', 'z');
            fits_link('galaxies', 'z');
            {% endif %}
            for (var i = 0; i < axes.length; i++) {
                var new_ax = document.createElement("option");
                new_ax.text = axes[i];
                axisList.options.add(new_ax, i);
            }
            $('#proj_axis').val("z");

        });

        function get_hub_link() {
            window.open("{{hub_folder}}", "_blank");
        }

        function fits_link(itype, axis) {
            var fits_link = girder_data[itype][axis]["fits"];
            document.getElementById(itype+'_fits').href = fits_link;
            document.getElementById(itype+'_fits').innerText = "FITS File Download ("+axis+"-axis)";
            document.getElementById(itype+'_fits').textContent = "FITS File Download ("+axis+"-axis)";
            var descr = "";
            if (itype == "galaxies") {
                descr = "region";
                var reg_link = girder_data["galaxies"][axis]["reg"];
                //document.getElementById(itype+'_js9').href = "javascript:JS9.LoadRegions('"+reg_link+"');";
                document.getElementById(itype+'_reg').href = reg_link;
                document.getElementById(itype+'_reg').innerText = "Region File Download ("+axis+"-axis)";
                document.getElementById(itype+'_reg').textContent = "Region File Download ("+axis+"-axis)";
            } else {
                descr = "FITS";
                document.getElementById(itype+'_js9').onclick = function(){js9Load(fits_link, itype)};
                document.getElementById(itype+'_js9').innerText = "Open "+descr+" file in JS9 below ("+axis+"-axis)";
                document.getElementById(itype+'_js9').textContent = "Open "+descr+" file in JS9 below ("+axis+"-axis)";
            }
            //document.getElementById(itype+'_js9').innerText = "Open "+descr+" file in JS9 below ("+axis+"-axis)";
            //document.getElementById(itype+'_js9').textContent = "Open "+descr+" file in JS9 below ("+axis+"-axis)";
        }
        
        function show_files(itype, axis) {
            var pngs = girder_data[itype][axis]["pngs"];
            $.each(pngs, function(key, value) {
                var img = document.getElementById(itype+'_'+key);
                img.src = "../../images/loader.gif";
                img.src = value;
                document.getElementById('big_'+itype+'_'+key).href = value;
            });
        }
         
        var changeAxis = function () { 
            var axis = this.options[this.selectedIndex].value;
            show_files('proj', axis);
            fits_link('proj', axis);
            {% if sz_fields|length > 0 %}
            show_files('SZ', axis);
            fits_link('SZ', axis);
            {% endif %}
            show_files('cxo_evt', axis);
            fits_link('cxo_evt', axis);
            {% if galaxies %}
            show_files('galaxies', axis);
            fits_link('galaxies', axis);
            {% endif %}
            $('#fits_ext').empty();
            JS9.CloseImage();
        }

        axisList.addEventListener('change', changeAxis, false);
        
        var getHDUList = function() {
            $('#fits_ext').empty();
            imdata = JS9.GetImageData(false);
            var default_name = "";
            for (var i = 0; i < imdata.hdus.length; i++) {
                var name = imdata.hdus[i].name;
                if (name == "DENSITY" || name == "XRAY_EMISSIVITY" ||
                    name == "180_GHZ" || name == "EVENTS") {
                    default_name = name;
                }
                if (typeof name != "undefined" && name != "STDGTI") {
                    var new_hdu = document.createElement("option");
                    new_hdu.text = name;
                    fitsList.options.add(new_hdu, i)
                }
            }
            $('#fits_ext').val(default_name);
        }
        
        function js9Load(url, itype) {
            JS9.CloseImage();
            JS9.Load(url+"["+default_js9[itype]+"]", {onload: getHDUList});
        }

        var changeFits = function () {
            var extid = this.selectedIndex;
            JS9.DisplayExtension(extid);
        }
        
        fitsList.addEventListener('change', changeFits, false);

    </script>

    <div id="hubModal" class="modal fade" role="dialog">
    <div class="modal-content">
    <div class="modal-header">
    <button type="button" class="close" data-dismiss="modal">&times;</button>
    </div>
    <div class="modal-body">
    <p>
    <img src="../../images/start_notebook.png" hspace="10" align="right" width="300"/>
    <a href="" onclick="get_hub_link()"><h3>Get direct access to these files from within the yt Hub.</h3></a>
    If you have an account on the <a href="http://girder.hub.yt" target="_blank">yt Hub</a>, click the link above and use the blue arrow button in the top-right corner (see image at right) to start a Jupyter notebook on the server, with access to the files and a full Python stack including NumPy, SciPy, AstroPy, yt, and more. The files are located in the "data" folder from within the notebook. 
    </p>
    </div>
    </div>
    </div>
