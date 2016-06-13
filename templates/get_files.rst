
.. raw:: html
   
    <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
    <script src="lightbox/js/lightbox.js"></script>
    <script>$('head').append('<link rel="stylesheet" href="lightbox/css/lightbox.css"/>');</script>
    <script>$('head').append('<link type="text/css" rel="stylesheet" href="js9/js9support.css">');</script>
    <script>$('head').append('<link type="text/css" rel="stylesheet" href="js9/js9.css">');</script>
    <script src="https://girder.hub.yt/static/built/girder.ext.min.js"></script>
    <script src="https://girder.hub.yt/static/built/girder.app.min.js"></script>
    <script type="text/javascript" src="js9/js9support.min.js"></script>
    <script type="text/javascript" src="js9/js9.min.js"></script>
    <script type="text/javascript" src="js9/js9plugins.js"></script>
    <script>$('#dLabelGlobalToc').addClass('hidden');</script>
    <script>$('#dLabelLocalToc').addClass('hidden');</script>

    <script>
        function getParameterByName(name, url) {
            if (!url) url = window.location.href;
            var name = name.replace(/[\[\]]/g, "\\$&");
            var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
                results = regex.exec(url);
            if (!results) return null;
            if (!results[2]) return '';
            return decodeURIComponent(results[2].replace(/\+/g, " "));
        }
    </script>

    <h1 id="header"></h1>

For directions on how to navigate this page, check out :ref:`how-to-use`.

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
        <option value="x">x</option>
        <option value="z" selected="selected">z</option>
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
    <figcaption><h4>X-ray Counts (0.5-7 keV, <em>Chandra</em> ACIS-I, 50 ks)</h4></figcaption>
    <a id="big_cxo_evt_counts" data-lightbox="lb_cxo_evt_counts" ><img id="cxo_evt_counts" width="450" /></a>
    </figure>
    <br>
    <a id="cxo_evt_fits">FITS File Download</a><br>
    <a id="cxo_evt_js9">Open in JS9</a>
    <br><br>

    <!-- <h2>Jupyter Notebook</h2>
    <a id="notebook" >Start a Jupyter notebook with access to these files.</a>
    -->
    
    <h2>JS9 Interface</h2>

    <select id="fits_ext"></select>
    <br>

    <div class="JS9Menubar"></div>
    <div class="JS9"></div>
    <div style="margin-top: 2px;">
    <div class="JS9Colorbar"></div>
    </div>

    <script>
        var sim = getParameterByName('sim');
        var fileno = getParameterByName('fileno');
        var girder_root = "https://girder.hub.yt/api/v1";
        var axisList = document.getElementById("proj_axis");
        var fitsList = document.getElementById("fits_ext");

        var field_map = {xray_emissivity:"xray",
                         total_density:"dens",
                         kT:"temp",
                         dark_matter_density:"pden",
                         density:"dens",
                         szy:"szy",
                         Tau:"tau",
                         "240_GHz":"inty",
                         "counts":"counts"};

        var type_map = {"slice":["density","kT","dark_matter_density"],
                        "proj":["xray_emissivity","kT","total_density","szy"],
                        "SZ":["Tau","240_GHz"],
                        "cxo_evt":["counts"]};
        var default_js9 = {"slice":"DENSITY","proj":"XRAY_EMISSIVITY","SZ":"180_GHZ","cxo_evt":"EVENTS"};
                       
        var sim_name = get_sim_name(sim);
        var timestr = "t = " + (parseFloat(fileno)*{{cadence}}).toFixed(2) + " Gyr";

        $(document).ready(function () {
             
            girder.apiRoot = girder_root;
            girder.router.enabled(false);
 
            show_files(sim, fileno, 'slice', 'z');
            fits_link(sim, fileno, 'slice', 'z');
            show_files(sim, fileno, 'proj', 'z');
            fits_link(sim, fileno, 'proj', 'z');
            show_files(sim, fileno, 'SZ', 'z');
            fits_link(sim, fileno, 'SZ', 'z');
            show_files(sim, fileno, 'cxo_evt', 'z');
            fits_link(sim, fileno, 'cxo_evt', 'z');
            document.getElementById('header').innerText = sim_name+", "+timestr;
            document.title = sim_name+", "+timestr;

            if (sim.substring(sim.length-2,sim.length) != "b0") {
                var new_ax = document.createElement("option");
                new_ax.text = "y";
                axisList.options.add(new_ax, 1);
            }
 
        });
        
        function get_sim_name(sim) {
            if (sim.startsWith("R")) {
                var ridx = sim.indexOf("R")+1;
            } else {
                var ridx = sim.indexOf("to")+2;
            }
            var bidx = sim.indexOf("b")+1;
            var ratio = sim.substring(ridx,ridx+1);
            var b = sim.substring(bidx,sim.length);
            if (!sim.startsWith("R")) {
                var b = ~~(parseFloat(b)*1000);
            }
            return "R = 1:"+ratio+", b = "+b+" kpc";
        }
        
        function fits_link(sim, fileno, type, axis) {
            var fn = "{{basenm}}_"+sim+"_hdf5_plt_cnt_"+fileno+"_"+type+"_"+axis;
            $.getJSON(girder_root+'/resource/search',
                      {q: fn,  types: '["item"]'},
                      function(data) {
                          var id = data.item[0]._id;
                          var folderId = data.item[0].folderId;
                          document.getElementById(type+'_fits').href = get_link(id);
                          document.getElementById(type+'_fits').innerText = "FITS File Download ("+axis+"-axis)";
                          document.getElementById(type+'_js9').href = "javascript:js9Load('"+get_link(id)+"','"+type+"');";
                          document.getElementById(type+'_js9').innerText = "Open in JS9 ("+axis+"-axis)";
                          //if (type == 'slice') {
                          //    document.getElementById('notebook').href = "javascript:open_nb('"+folderId+"');";
                          //}
                      });
        }
        
        function show_files(sim, fileno, type, axis) {
            var fn = "{{basenm}}_"+sim+"_hdf5_plt_cnt_"+fileno+"_"+type+"_"+axis;
            var fields = type_map[type];
            for (var i = 0; i < fields.length; i++) {
                $.getJSON(girder_root+'/resource/search',
                          {q: fn+"_"+fields[i],  types: '["item"]'},
                          function(data) {
                              var id = data.item[0]._id;
                              var name = data.item[0].name;
                              var element = type+"_"+element_map(axis,name);
                              document.getElementById(element).src = get_link(id);
                              document.getElementById('big_'+element).href = get_link(id);
                          });
            }

        }
        
        function element_map(axis, name) {
            var st = name.lastIndexOf("_"+axis+"_")+3;
            var ed = name.indexOf(".png");
            field = name.substring(st,ed);
            return field_map[field]
        }
        
        function get_link(id) {
            return girder_root+"/item/"+id+"/download";
        }
 
        var changeAxis = function () { 
            var axis = this.options[this.selectedIndex].value;
            show_files(sim, fileno, 'proj', axis);
            fits_link(sim, fileno, 'proj', axis);
            show_files(sim, fileno, 'SZ', axis);
            fits_link(sim, fileno, 'SZ', axis);
            show_files(sim, fileno, 'cxo_evt', axis);
            fits_link(sim, fileno, 'cxo_evt', axis);
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
                var new_hdu = document.createElement("option");
                if (name == "DENSITY" || name == "XRAY_EMISSIVITY" ||
                    name == "180_GHZ" || name == "EVENTS") {
                    default_name = name;
                }
                if (name != "PRIMARY") {
                    new_hdu.text = name;
                    fitsList.options.add(new_hdu, i)
                }
            }
            $('#fits_ext').val(default_name);
        }
        
        function js9Load(url, type) {
            JS9.CloseImage();
            JS9.Load(url+"["+default_js9[type]+"]", {onload: getHDUList});
        }

        var changeFits = function () {
            var extid = this.selectedIndex;
            JS9.DisplayExtension(extid);
        }
        
        fitsList.addEventListener('change', changeFits, false);
 
        function open_nb(folderId) {
            girder.restRequest({
                path: 'notebook/' + folderId,
                type: 'POST'
            }).done(function (notebook) {
                window.location.assign(hub["url"] + notebook["url"]);
            });
        }
    </script>
