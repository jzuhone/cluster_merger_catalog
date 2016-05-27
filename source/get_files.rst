
.. raw:: html
  
    <script src="https://hub.yt/girder/static/built/girder.ext.min.js"></script>
    <script src="https://hub.yt/girder/static/built/girder.app.min.js"></script>

    <script>
        var sim = sessionStorage.getItem("sim");
        var fileno = sessionStorage.getItem("fileno");

        $(document).ready(function () {
            //var sim = sessionStorage.getItem("sim");
            //var fileno = sessionStorage.getItem("fileno");
            
            var fn = "fiducial_"+sim+"_hdf5_plt_cnt_"+fileno+"_proj_z";
            
            get_file_ids(fn)

        });
        
        function get_file_ids(fn_spec) {
            $.getJSON('https://girder.hub.yt/api/v1/resource/search',
                      {q: fn_spec,  types: '["item"]'},
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
            return "http://girder.hub.yt/api/v1/item/"+id+"/download";
        }

    </script>

    <h2>Projections</h2>

    <select id="proj_axis">
        <option value="x">x</option>
        <option value="z" selected="selected">z</option>
    </select>
    
    <br><br>

    <img id="xray" width="350" />
    <img id="temp" width="350" />
    <img id="dens" width="350" />
    <br>
    <a id="proj_fits">Download the FITS file</a>

    <script>
    
        var changeAxis = function () { 
            var axis = this.options[this.selectedIndex].value;
            var fn = "fiducial_"+sim+"_hdf5_plt_cnt_"+fileno+"_proj_"+axis;
            get_file_ids(fn);
        }

        var axisList = document.getElementById('proj_axis');
        axisList.addEventListener('change', changeAxis, false);
        
    </script>
