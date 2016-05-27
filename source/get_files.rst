
.. raw:: html
   
    <script src="https://hub.yt/girder/static/built/girder.ext.min.js"></script>
    <script src="https://hub.yt/girder/static/built/girder.app.min.js"></script>

    <h1 id="header"></h1>

    <h2>Projections</h2>

    Change the projection direction:
    <select id="proj_axis">
        <option value="x">x</option>
        <option value="z" selected="selected">z</option>
    </select>

    <h3>X-ray Emissivity, Spectroscopic Temperature, Total Density</h3>
     
    <br><br>

    <img id="xray" width="350" />
    <img id="temp" width="350" />
    <img id="dens" width="350" />
    <br>
    <a id="proj_fits">Download the FITS file</a>

    <script>
        var sim = sessionStorage.getItem("sim");
        var fileno = sessionStorage.getItem("fileno");
        var timestr = sessionStorage.getItem("timestr");
        var sim_name = sessionStorage.getItem("sim_name");
        var girder_root = "https://girder.hub.yt/api/v1";
        var axisList = document.getElementById("proj_axis");
        
        $(document).ready(function () {
             
            show_files(sim, fileno, 'z')
            document.getElementById('header').innerText = sim_name+", "+timestr;
            document.title = sim_name+", "+timestr;

            
            if (sim.substring(sim.length-2,sim.length) != "b0") {
                var new_ax = document.createElement("option");
                new_ax.text = "y";
                axisList.options.add(new_ax, 1);
            }
            
        });
        
        function show_files(sim, fileno, axis) {
            var fn = "fiducial_"+sim+"_hdf5_plt_cnt_"+fileno+"_proj_"+axis;
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
                                      element = 'xray';
                                  } else if (names[i].indexOf("kT") > -1) {
                                      element = 'temp';
                                  } else if (names[i].indexOf("density") > -1) {
                                      element = 'dens';
                                  }
                                  document.getElementById(element).src = get_link(ids[i]);
                              } else {
                                  document.getElementById('proj_fits').href = get_link(ids[i]);
                              }
                          }
                      });
        }
        
        function get_link(id) {
            return girder_root+"/item/"+id+"/download";
        }

    </script>

    <script>
    
        var changeAxis = function () { 
            var axis = this.options[this.selectedIndex].value;
            show_files(sim, fileno, axis);
        }

        axisList.addEventListener('change', changeAxis, false);
        
    </script>
