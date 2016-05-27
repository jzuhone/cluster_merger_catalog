
.. raw:: html
   
    <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
    <script src="lightbox/js/lightbox.js"></script>
    <script>$('head').append('<link rel="stylesheet" href="lightbox/css/lightbox.css"/>');</script>
    
    <h1 id="header"></h1>

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
    
    <script>
        var sim = sessionStorage.getItem("sim");
        var fileno = sessionStorage.getItem("fileno");
        var timestr = sessionStorage.getItem("timestr");
        var sim_name = sessionStorage.getItem("sim_name");
        var girder_root = "https://girder.hub.yt/api/v1";
        var axisList = document.getElementById("proj_axis");
        
        $(document).ready(function () {
             
            show_files(sim, fileno, 'proj', 'z')
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
                                  var element = '';
                                  if (names[i].indexOf("xray") > -1) {
                                      element = 'proj_xray';
                                  } else if (names[i].indexOf("kT") > -1) {
                                      element = 'proj_temp';
                                  } else if (names[i].indexOf("density") > -1) {
                                      element = 'proj_dens';
                                  }
                                  document.getElementById(element).src = get_link(ids[i]);
                                  document.getElementById('big_'+element).href = get_link(ids[i]);
                              } else {
                                  document.getElementById(type+'_fits').href = get_link(ids[i]);
                              }
                          }
                      });
        }
        
        function element_map(type) {
        }
        
        function get_link(id) {
            return girder_root+"/item/"+id+"/download";
        }

    </script>

    <script>
    
        var changeAxis = function () { 
            var axis = this.options[this.selectedIndex].value;
            show_files(sim, fileno, 'proj', axis);
        }

        axisList.addEventListener('change', changeAxis, false);
        
    </script>
