
.. raw:: html
   
    <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
    <script src="../../lightbox/js/lightbox.js"></script>
    <script>$('head').append('<link rel="stylesheet" href="../../lightbox/css/lightbox.css"/>');</script>
    <script>$('head').append('<link type="text/css" rel="stylesheet" href="../../js9/js9support.css">');</script>
    <script>$('head').append('<link type="text/css" rel="stylesheet" href="../../js9/js9.css">');</script>
    <script type="text/javascript" src="../../js9/js9support.min.js"></script>
    <script type="text/javascript" src="../../js9/js9.min.js"></script>
    <script type="text/javascript" src="../../js9/js9plugins.js"></script>
    <script>$('#dLabelGlobalToc').addClass('hidden');</script>
    <script>$('#dLabelLocalToc').addClass('hidden');</script>
    <script>$('.navbar-nav').first().append('<li><a href="index_z.html">&#10094; Back to Simulation</a></li>');</script>
   
{{sim_name|safe}}: {{timestr}}
=========================

.. raw:: html

   <a class="btn btn-primary" href="{{prev_link}}" role="button" {{dis_prev}}>&#10094; Previous Epoch</a>
   <a class="btn btn-primary" href="{{next_link}}" role="button" {{dis_next}}>&#10095; Next Epoch</a>
   <br><br>

To make the best use out of this page:

* Click on any image to enlarge it.
* Download FITS files from the links or load them into the JS9 window at the bottom of the page.
* Change the axis of projection for the images and links using the drop-down menu. 

.. raw:: html

    <h2>Slices</h2>

The slice FITS file contains the following fields:

{% for field, descr in slice_fields.items %}
* ``"{{field}}"``: {{descr}}
{% endfor %}
  
.. raw:: html

    <a id="slice_fits">FITS File Download</a><br>
    <a id="slice_js9">Open in JS9 below</a>
    <br><br>	       
    {% for key, name in slice_names.items %}
    <figure style="display: inline-block;">
    <figcaption><h4>{{name}}</h4></figcaption>
    <a id="big_slice_{{key}}" data-lightbox="lb_slice_{{key}}" ><img id="slice_{{key}}" width="450" /></a>
    </figure>
    {% endfor %}
    <br>

    <h2>Projections</h2>

    Change the projection direction:
    <select id="proj_axis">
    </select>
    <br><br>

The projection FITS file contains the following fields:

{% for field, descr in proj_fields.items %}
* ``"{{field}}"``: {{descr}}
{% endfor %}

.. raw:: html

    <a id="proj_fits">FITS File Download</a><br>
    <a id="proj_js9">Open in JS9 below</a>
    <br><br>
    {% for key, name in proj_names.items %}
    <figure style="display: inline-block;">
    <figcaption><h4>{{name}}</h4></figcaption>
    <a id="big_proj_{{key}}" data-lightbox="lb_proj_{{key}}" ><img id="proj_{{key}}" width="450" /></a>
    </figure>
    {% endfor %}
    <br><br>

{% if sz_fields|length > 0 %}

The SZ FITS file contains the following fields:

{% for field, descr in sz_fields.items %}
* ``"{{field}}"``: {{descr}}
{% endfor %}

.. raw:: html

    <a id="SZ_fits">FITS File Download</a><br>
    <a id="SZ_js9">Open in JS9 below</a>
    <br><br>    
    {% for key, name in sz_names.items %}
    <figure style="display: inline-block;">
    <figcaption><h4>{{name}}</h4></figcaption>
    <a id="big_SZ_{{key}}" data-lightbox="lb_SZ_{{key}}" ><img id="SZ_{{key}}" width="450" /></a>
    </figure>
    {% endfor %}
			
    <br><br>
{% endif %}
    
    The events FITS file contains an X-ray event list.
    <br><br>	 
    <a id="cxo_evt_fits">FITS File Download</a><br>
    <a href="../../files/acisi_rmfs.tar.gz">Download Response Files</a><br>
    <a id="cxo_evt_js9">Open in JS9 below</a>
    <br><br>
    <figure style="display: inline-block;">
    <figcaption><h4>X-ray Counts (<em>Chandra</em> ACIS-I, 50 ks)</h4></figcaption>
    <a id="big_cxo_evt_counts" data-lightbox="lb_cxo_evt_counts" ><img id="cxo_evt_counts" width="450" /></a>
    </figure>
    <br><br>
    
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

        var default_js9 = {"slice":"DENSITY","proj":"XRAY_EMISSIVITY","SZ":"180_GHZ","cxo_evt":"EVENTS"};

        var girder_data = {
        {% for itype, axes in data.items %}
            "{{itype}}": {
        {% for ax, ftypes in axes.items %}
                "{{ax}}": {"fits": "{{ftypes.fits}}",
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

            for (var i = 0; i < axes.length; i++) {
                var new_ax = document.createElement("option");
                new_ax.text = axes[i];
                axisList.options.add(new_ax, i);
            }
            $('#proj_axis').val("z");

        });

        function fits_link(itype, axis) {
            var fits_link = girder_data[itype][axis]["fits"];
            document.getElementById(itype+'_fits').href = fits_link;
            document.getElementById(itype+'_fits').innerText = "FITS File Download ("+axis+"-axis)";
            document.getElementById(itype+'_fits').textContent = "FITS File Download ("+axis+"-axis)";
	    document.getElementById(itype+'_js9').href = "javascript:js9Load('"+fits_link+"','"+itype+"');";
            document.getElementById(itype+'_js9').innerText = "Open in JS9 below ("+axis+"-axis)";
            document.getElementById(itype+'_js9').textContent = "Open in JS9 below ("+axis+"-axis)";
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
