from collections import OrderedDict
from sim_defs import Simulation

fid_notes = ["There is no metallicity field in these simulations; hence for computing X-ray "+
             "emissivities a constant metallicity of :math:`Z = 0.3~Z_\odot` is assumed."]

fid_info = {"name": "fiducial", 
            "cadence": 0.02,
            "filespec": "fiducial_%s_hdf5_plt_cnt_%04d",
            "set_name": "A Parameter Space Exploration of Galaxy Cluster Mergers (ZuHone 2011)",
            "set_journals": [("ZuHone, J. A. 2011, ApJ, 728, 54",
                              "http://adsabs.harvard.edu/abs/2011ApJ...728...54Z")],
            "box_size": "14.26 Mpc",
            "cell_size": "6.96 kpc",
            "sim_type": "AMR",
            "code": "FLASH",
            "primary_mass": "M_{200} = 6~{\\times}~10^{14}~M_{\odot}",
            "sim_notes": "For the following simulations, :math:`R` is the mass ratio between " + \
                         "the two clusters and :math:`b` is the initial impact parameter in kpc.",
            "notes": fid_notes, "cosmo_warning": True, 'redshift': 0.05}

fields = {}
fields["slice"] = ["dens","temp","pden","velx","vely","clr1","clr2"]
fields["proj"] = ["xray","temp","dens","szy","szk"]
fields["SZ"] = ["tau","temp","inty90","inty180","inty240"]

pngs = {}
pngs["slice"] = ["dens","temp","pden"]
pngs["proj"] = ["xray","temp","dens","szy"]
pngs["SZ"] = ["tau","inty240"]
pngs["cxo_evt"] = ["counts"]
pngs["galaxies"] = ["ppv"]

fid_physics = []

fid_dict = OrderedDict()
fid_dict["1to1_b0"] = Simulation("R = 1:1, b = 0 kpc",
                                 [0, 20, 30, 40, 50, 60, 61, 62, 63,
                                  64, 65, 66, 67, 68, 69, 70, 75, 80,
                                  85, 90, 100, 110, 120, 125, 126, 127,
                                  128, 129, 130, 131, 132, 133, 134, 135,
                                  140, 145, 150, 160, 170, 180, 190, 200,
                                  210, 220, 240, 260, 280, 300, 350, 400,
                                  450, 500], fields, pngs, ["x", "z"])
fid_dict["1to1_b0.5"] = Simulation("R = 1:1, b = 500 kpc",
                                   [0, 20, 30, 40, 50, 60, 65, 66, 67,
                                    68, 69, 70, 71, 72, 73, 74, 75, 80,
                                    85, 90, 100, 110, 120, 130, 135, 136,
                                    137, 138, 139, 140, 141, 142, 143, 144,
                                    145, 150, 155, 160, 165, 170, 180, 190,
                                    200, 210, 220, 240, 260, 280, 300, 350,
                                    400, 450, 500], fields, pngs, ["x", "y", "z"])
fid_dict["1to1_b1"] = Simulation("R = 1:1, b = 1000 kpc",
                                 [0, 20, 30, 40, 50, 55, 60, 61, 62,
                                  63, 64, 65, 66, 67, 68, 69, 70, 71,
                                  72, 73, 74, 75, 80, 90, 100, 110, 120,
                                  130, 140, 141, 142, 143, 144, 145, 146,
                                  147, 148, 149, 150, 151, 152, 153, 154,
                                  155, 160, 165, 170, 175, 180, 190, 200,
                                  210, 220, 240, 260, 280, 300, 350, 400,
                                  450, 500], fields, pngs, ["x", "y", "z"])
fid_dict["1to3_b0"] = Simulation("R = 1:3, b = 0 kpc",
                                 [0, 20, 30, 40, 50, 55, 56, 57, 58, 59, 60,
                                  61, 62, 63, 64, 65, 70, 80, 90, 100, 110, 120,
                                  130, 140, 141, 142, 143, 144, 145, 146, 147, 148,
                                  149, 150, 160, 170, 180, 181, 182, 183, 184, 185,
                                  186, 187, 188, 189, 190, 200, 210, 220, 230, 240,
                                  250, 260, 300, 350, 400, 450, 500], fields, pngs,
                                 ["x", "z"])
fid_dict["1to3_b0.5"] = Simulation("R = 1:3, b = 500 kpc",
                                   [0, 20, 30, 40, 50, 55, 56, 57,
                                    58, 59, 60, 61, 62, 63, 64, 65,
                                    70, 75, 80, 85, 90, 100, 110,
                                    120, 130, 140, 145, 150, 151,
                                    152, 153, 154, 155, 156, 157,
                                    158, 159, 160, 165, 170, 175,
                                    180, 185, 190, 195, 200, 210,
                                    220, 230, 240, 250, 260, 280,
                                    300, 350, 400, 450, 500], fields, pngs,
                                   ["x", "y", "z"])
fid_dict["1to3_b1"] = Simulation("R = 1:3, b = 1000 kpc",
                                 [0, 20, 30, 40, 50, 55, 60, 61, 62,
                                  63, 64, 65, 66, 67, 68, 69, 70, 75,
                                  80, 85, 95, 105, 115, 125, 135, 145,
                                  155, 160, 165, 170, 171, 172, 173, 174,
                                  175, 176, 177, 178, 179, 180, 185, 190,
                                  200, 210, 215, 216, 217, 218, 219, 220,
                                  221, 222, 223, 224, 225, 230, 240, 250,
                                  260, 270, 280, 290, 300, 320, 340, 360,
                                  380, 400, 450, 500], fields, pngs,
                                 ["x", "y", "z"])
fid_dict["1to10_b0"] = Simulation("R = 1:10, b = 0 kpc",
                                  [0, 20, 30, 40, 50, 51, 52, 53, 54, 55,
                                   56, 57, 58, 59, 60, 65, 70, 75, 80, 85,
                                   90, 95, 100, 110, 120, 130, 140, 150,
                                   160, 165, 170, 175, 176, 177, 178, 179,
                                   180, 181, 182, 183, 184, 185, 190, 195,
                                   200, 205, 210, 220, 230, 240, 250, 255,
                                   260, 265, 270, 275, 280, 285, 290, 300,
                                   310, 320, 330, 340, 350, 400, 450, 500],
                                  fields, pngs, ["x","z"])
