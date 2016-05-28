
.. raw:: html
   
    <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
    <script src="lightbox/js/lightbox.js"></script>
    <script>$('head').append('<link rel="stylesheet" href="lightbox/css/lightbox.css"/>');</script>
    <script>
        function getParameterByName(name, url) {
            if (!url) url = window.location.href;
            name = name.replace(/[\[\]]/g, "\\$&");
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
    <a id="slice_fits">FITS File Download</a>
    <br><br>

    <h2>Projections</h2>

    Change the projection direction:
    <select id="proj_axis">
        <option value="x">x</option>
        <option value="z" selected="selected">z</option>
    </select>

    <h3>X-ray Emissivity, Spectroscopic Temperature, Total Density</h3>

    <a id="big_proj_xray" data-lightbox="lb_proj_xray" ><img id="proj_xray" width="350" /></a>
    <a id="big_proj_temp" data-lightbox="lb_proj_temp" ><img id="proj_temp" width="350" /></a>
    <a id="big_proj_dens" data-lightbox="lb_proj_dens" ><img id="proj_dens" width="350" /></a>
    <br>
    <a id="proj_fits">FITS File Download</a>
    <br><br>
    
    <h3>Sunyaev-Zeldovich</h3>
    <a id="big_SZ_240" data-lightbox="lb_SZ_240" ><img id="SZ_240" width="350" /></a>
    <br>
    <a id="SZ_fits">FITS File Download</a>
    <br><br>

    <script>
        //var sim = sessionStorage.getItem("sim");
        //var fileno = sessionStorage.getItem("fileno");
        //var timestr = sessionStorage.getItem("timestr");
        //var sim_name = sessionStorage.getItem("sim_name");
        var sim = getParameterByName('sim')
        var fileno = getParameterByName('fileno')
        var girder_root = "https://girder.hub.yt/api/v1";
        var axisList = document.getElementById("proj_axis");

        var field_map = {xray_emissivity:"xray",
                         total_density:"dens",
                         kT:"temp",
                         dark_matter_density:"pden",
                         density:"dens",
                         "240_GHz":"240"};

        var sim_map = {"1to3_b0" : "R = 1:3, b = 0 kpc"};

        var sim_name = sim_map[sim];
        var timestr = fileno

        $(document).ready(function () {
             
            show_files(sim, fileno, 'slice', 'z');
            show_files(sim, fileno, 'proj', 'z');
            show_files(sim, fileno, 'SZ', 'z');
            document.getElementById('header').innerText = sim_name+", "+timestr;
            document.title = sim_name+", "+timestr;

            if (sim.substring(sim.length-2,sim.length) != "b0") {
                var new_ax = document.createElement("option");
                new_ax.text = "y";
                axisList.options.add(new_ax, 1);
            }
            
        });
        
        function show_files(sim, fileno, type, axis) {
            var fn = "fiducial_"+sim+"_hdf5_plt_cnt_"+fileno+"_"+type+"_"+axis;
            $.getJSON(girder_root+'/resource/search',
                      {q: fn,  types: '["item"]'},
                      function(data) {
                          files = data.item;
                          ids = files.map(function(f){return f._id});
                          names = files.map(function(f){return f.name});
                          for (var i = 0; i < names.length; i++) {
                              if (names[i].indexOf("png") > -1) {
                                  element = type+"_"+element_map(names[i]);
                                  document.getElementById(element).src = get_link(ids[i]);
                                  document.getElementById('big_'+element).href = get_link(ids[i]);
                              } else {
                                  document.getElementById(type+'_fits').href = get_link(ids[i]);
                                  document.getElementById(type+'_fits').innerText = "FITS File Download ("+axis+"-axis)";
                              }
                          }
                      });
        }
        
        function element_map(name) {
            st = name.indexOf("_Slice_z_")+9
            ed = name.indexOf(".png")
            field = name.substring(st,ed)
            return field_map[field]
        }
        
        function get_link(id) {
            return girder_root+"/item/"+id+"/download";
        }

    </script>

    <script>
    
        var changeAxis = function () { 
            var axis = this.options[this.selectedIndex].value;
            show_files(sim, fileno, 'proj', axis);
            show_files(sim, fileno, 'SZ', axis);
        }

        axisList.addEventListener('change', changeAxis, false);
        
    </script>
