
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

{{sim_name}}, {{timestr}}
==========================

To make the best use out of this page:

* Click on any image to enlarge it.
* Download FITS files from the links or load them into JS9 below.
* Change the axis of projection for the images and links using the drop-down menu. 

.. raw:: html

    <h2>Slices</h2>
    <figure style="display: inline-block;">
    <figcaption><h4>Density</h4></figcaption>
    <a id="big_slice_dens" data-lightbox="lb_slice_dens" ><img id="slice_dens" width="350" /></a>
    </figure>
    <figure style="display: inline-block;">
    <figcaption><h4>Temperature</h4></figcaption>
    <a id="big_slice_temp" data-lightbox="lb_slice_temp" ><img id="slice_temp" width="350" /></a>
    </figure>
    <figure style="display: inline-block;">
    <figcaption><h4>Dark Matter Density</h4></figcaption>
    <a id="big_slice_pden" data-lightbox="lb_slice_pden" ><img id="slice_pden" width="350" /></a>
    </figure>
    <br>
    <a id="slice_fits">FITS File Download</a><br>
    <a id="slice_js9">Open in JS9</a>
    <br><br>

    <h2>Projections</h2>

    Change the projection direction:
    <select id="proj_axis">
    </select>

    <br>
    <figure style="display: inline-block;">
    <figcaption><h4>X-ray Emissivity</h4></figcaption>
    <a id="big_proj_xray" data-lightbox="lb_proj_xray" ><img id="proj_xray" width="450" /></a>
    </figure>
    <figure style="display: inline-block;">
    <figcaption><h4>Projected Temperature</h4></figcaption>
    <a id="big_proj_temp" data-lightbox="lb_proj_temp" ><img id="proj_temp" width="450" /></a>
    </figure>
    <figure style="display: inline-block;">
    <figcaption><h4>Total Density</h4></figcaption>
    <a id="big_proj_dens" data-lightbox="lb_proj_dens" ><img id="proj_dens" width="450" /></a>
    </figure>
    <figure style="display: inline-block;">
    <figcaption><h4>Compton-y</h4></figcaption>
    <a id="big_proj_szy" data-lightbox="lb_proj_szy" ><img id="proj_szy" width="450" /></a>
    </figure>
    <br>
    <a id="proj_fits">FITS File Download</a><br>
    <a id="proj_js9">Open in JS9</a>

    <br><br>
    
    <figure style="display: inline-block;">
    <figcaption><h4>Compton Optical Depth</h4></figcaption>
    <a id="big_SZ_tau" data-lightbox="lb_SZ_tau" ><img id="SZ_tau" width="450" /></a>
    </figure>
    <figure style="display: inline-block;">
    <figcaption><h4>S-Z Signal (240 GHz)</h4></figcaption>
    <a id="big_SZ_inty" data-lightbox="lb_SZ_inty" ><img id="SZ_inty" width="450" /></a>
    </figure>
    <br>
    <a id="SZ_fits">FITS File Download</a><br>
    <a id="SZ_js9">Open in JS9</a>
    <br><br>
    
    <figure style="display: inline-block;">
    <figcaption><h4>X-ray Counts (<em>Chandra</em> ACIS-I, 50 ks)</h4></figcaption>
    <a id="big_cxo_evt_counts" data-lightbox="lb_cxo_evt_counts" ><img id="cxo_evt_counts" width="450" /></a>
    </figure>
    <br>
    <a id="cxo_evt_fits">FITS File Download</a><br>
    <a id="cxo_evt_js9">Open in JS9</a>
    <br><br>
    
    <h2>JS9 Interface</h2>
    
    Once an image file is loaded, use the drop-down menu below to switch between 
    the different fields in the file.

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

        var girder_data = {};
        var axes = [];

        {% for itype, axes in data.items %}
        girder_data["{{itype}}"] = {};
        {% for ax, ftypes in axes.items %}
        girder_data["{{itype}}"]["{{ax}}"] = {};
        girder_data["{{itype}}"]["{{ax}}"]["fits"] = "{{ftypes.fits}}";
        girder_data["{{itype}}"]["{{ax}}"]["pngs"] = {};
        {% for key, link in ftypes.pngs.items %}
        girder_data["{{itype}}"]["{{ax}}"]["pngs"]["{{key}}"] = "{{link}}";
        {% endfor %}
        {% endfor %}
        {% endfor %}

        {% for ax in data.proj %}
        axes.push("{{ax}}");
        {% endfor %}
        
        $(document).ready(function () {

            show_files('slice', 'z');
            fits_link('slice', 'z');
            show_files('proj', 'z');
            fits_link('proj', 'z');
            show_files('SZ', 'z');
            fits_link('SZ', 'z');
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
            document.getElementById(itype+'_js9').href = "javascript:js9Load('"+fits_link+"','"+itype+"');";
            document.getElementById(itype+'_js9').innerText = "Open in JS9 ("+axis+"-axis)";
        }
        
        function show_files(itype, axis) {
            var pngs = girder_data[itype][axis]["pngs"];
            $.each(pngs, function(key, value) {
                document.getElementById(itype+'_'+key).src = value;
                document.getElementById('big_'+itype+'_'+key).href = value;
            });
        }
         
        var changeAxis = function () { 
            var axis = this.options[this.selectedIndex].value;
            show_files('proj', axis);
            fits_link('proj', axis);
            show_files('SZ', axis);
            fits_link('SZ', axis);
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
