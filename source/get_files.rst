
.. raw:: html
   
    <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
    <script src="lightbox/js/lightbox.js"></script>
    <script>$('head').append('<link rel="stylesheet" href="lightbox/css/lightbox.css"/>');</script>
    <script>$('head').append('<link type="text/css" rel="stylesheet" href="js9/js9support.css">');</script>
    <script>$('head').append('<link type="text/css" rel="stylesheet" href="js9/js9.css">');</script>
    <script type="text/javascript" src="js9/js9support.min.js"></script>
    <script type="text/javascript" src="js9/js9.min.js"></script>
    <script type="text/javascript" src="js9/js9plugins.js"></script>

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

    <h2>Slices</h2>
    
    <a id="big_slice_dens" data-lightbox="lb_slice_dens" ><img id="slice_dens" width="350" /></a>
    <a id="big_slice_temp" data-lightbox="lb_slice_temp" ><img id="slice_temp" width="350" /></a>
    <a id="big_slice_pden" data-lightbox="lb_slice_pden" ><img id="slice_pden" width="350" /></a>
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

    <h3>X-ray Emissivity, Spectroscopic Temperature, Total Density, Compton-y</h3>

    <a id="big_proj_xray" data-lightbox="lb_proj_xray" ><img id="proj_xray" width="450" /></a>
    <a id="big_proj_temp" data-lightbox="lb_proj_temp" ><img id="proj_temp" width="450" /></a>
    <a id="big_proj_dens" data-lightbox="lb_proj_dens" ><img id="proj_dens" width="450" /></a>
    <a id="big_proj_szy" data-lightbox="lb_proj_szy" ><img id="proj_szy" width="450" /></a>
    <br>
    <a id="proj_fits">FITS File Download</a><br>
    <a id="proj_js9">Open in JS9</a>

    <br><br>
    
    <h3>Sunyaev-Zeldovich Intensity</h3>
    <a id="SZ_fits">FITS File Download</a><br>
    <a id="SZ_js9">Open in JS9</a>
    <br><br>
    
    <h2>Jupyter Notebook</h2>
    <a id="notebook" >Start a Jupyter notebook with access to these files.</a>

    <h2>JS9 Interface</h2>

    <select id="fits_ext"></select>
    <br>

    <div class="JS9Menubar"></div>
    <div class="JS9"></div>
    <div style="margin-top: 2px;">
    <div class="JS9Colorbar"></div>
    </div>

    <script>
        var sim = getParameterByName('sim')
        var fileno = getParameterByName('fileno')
        var girder_root = "https://girder.hub.yt/api/v1";
        var axisList = document.getElementById("proj_axis");
        var fitsList = document.getElementById("fits_ext");
         
        var field_map = {xray_emissivity:"xray",
                         total_density:"dens",
                         kT:"temp",
                         dark_matter_density:"pden",
                         density:"dens",
                         szy:"szy"};

        var type_map = {"slice":["density","kT","dark_matter_density"],
                        "proj":["xray_emissivity","kT","total_density","szy"]};
        var sim_map = {"1to3_b0" : "R = 1:3, b = 0 kpc"};
        var default_js9 = {"slice":2,"proj":0,"SZ":0};
        var hdu_map = {"slice":["CLR2","CLR1","DENSITY","KT","DARK_MATTER_DENSITY","VELOCITY_X","VELOCITY_Y"],
                       "proj":["XRAY_EMISSIVITY","SZ_KINETIC","SZY","TOTAL_DENSITY","KT"],
                       "SZ":["180_GHZ","90_GHZ","240_GHZ","TESZ","TAU"]};
                       
        var sim_name = sim_map[sim];
        var timestr = "t = " + (parseFloat(fileno)*0.02).toFixed(2) + " Gyr";

        $(document).ready(function () {
             
            show_files(sim, fileno, 'slice', 'z');
            fits_link(sim, fileno, 'slice', 'z');
            show_files(sim, fileno, 'proj', 'z');
            fits_link(sim, fileno, 'proj', 'z');
            fits_link(sim, fileno, 'SZ', 'z');
            document.getElementById('header').innerText = sim_name+", "+timestr;
            document.title = sim_name+", "+timestr;

            if (sim.substring(sim.length-2,sim.length) != "b0") {
                var new_ax = document.createElement("option");
                new_ax.text = "y";
                axisList.options.add(new_ax, 1);
            }
            
        });
        
        function fits_link(sim, fileno, type, axis) {
            var fn = "fiducial_"+sim+"_hdf5_plt_cnt_"+fileno+"_"+type+"_"+axis;
            $.getJSON(girder_root+'/resource/search',
                      {q: fn,  types: '["item"]'},
                      function(data) {
                          var id = data.item[0]._id;
                          document.getElementById(type+'_fits').href = get_link(id);
                          document.getElementById(type+'_fits').innerText = "FITS File Download ("+axis+"-axis)";
                          document.getElementById(type+'_js9').href = "javascript:js9Load('"+get_link(id)+"','"+type+"');";
                          document.getElementById(type+'_js9').innerText = "Open in JS9 ("+axis+"-axis)";
                      });
        }
        
        function show_files(sim, fileno, type, axis) {
            var fn = "fiducial_"+sim+"_hdf5_plt_cnt_"+fileno+"_"+type+"_"+axis;
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
            var st = name.lastIndexOf(axis+"_")+2;
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
            fits_link(sim, fileno, 'SZ', axis);
            $('#fits_ext').empty();
            JS9.CloseImage();
        }

        axisList.addEventListener('change', changeAxis, false);
        
        function js9Load(url, type) {
            JS9.Load(url+"["+default_js9[type]+"]");
            $('#fits_ext').empty();
            var hdulist = hdu_map[type];
            for (var i = 0; i < hdulist.length; i++) {
                var new_hdu = document.createElement("option");
                new_hdu.text = hdulist[i];
                fitsList.options.add(new_hdu, i);
            }
            $('#fits_ext').val(hdu_map[type][default_js9[type]]);
        }

        var changeFits = function () {
            var extid = this.selectedIndex;
            JS9.DisplayExtension(extid);
        }
        
        fitsList.addEventListener('change', changeFits, false);
        
    </script>
