from collections import OrderedDict
from sim_defs import Simulation
from copy import deepcopy

mag_notes = ["There is no metallicity field in these simulations; hence for computing X-ray "+
             "emissivities a constant metallicity of :math:`Z = 0.3~Z_\odot` is assumed.",
             "The data presented here are not from the original simulations presented in the "+
             "relevant paper but are improved versions with higher spatial resolution and "+
             "improved treatment of gravity. For details on the latter see "+
             "`Roediger & ZuHone 2012 <http://adsabs.harvard.edu/abs/2012MNRAS.419.1338R>`_.",
             "For each simulation, the main cluster is fixed at **r** = [0, 0, 0] kpc. "+
             "A tab-separated ASCII table containing the subcluster position, velocity, "+
             "and acceleration as a function of time may be found "+
             "`here <https://girder.hub.yt/api/v1/item/578eaf8f7b6f0800011e6e28/download>`_."]

mag_info = {"name": "sloshing_magnetic",
            "cadence": 0.01,
            "filespec": "AM06_%s_hdf5_plt_cnt_%04d",
            "set_name": "Sloshing of the Magnetized Cool Gas in the Cores of Galaxy Clusters",
            "set_journals": [("ZuHone, J. A., Markevitch, M., & Lee, D. 2011, ApJ, 743, 16",
                              "http://adsabs.harvard.edu/abs/2011ApJ...743...16Z")],
            "box_size": "2 Mpc",
            "cell_size": "0.977 kpc",
            "sim_type": "AMR",
            "code": "FLASH",
            "primary_mass": "M_{200} = 10^{15}~M_{\odot}",
            "sim_notes": "For the following simulations, :math:`\\beta = p_{\\rm th}/p_B`.",
            "notes": mag_notes, "cosmo_warning": True, 'redshift': 0.05}

fields = {}
fields["slice"] = ["dens","temp","bmag","velx","vely"]
fields["proj"] = ["xray","temp","szy","szk","rm"]
fields["SZ"] = []
pngs = {}
pngs["slice"] = ["dens","temp","bmag"]
pngs["proj"] = ["xray","temp","szy","rm"]
pngs["cxo_evt"] = ["counts"]
pngs["SZ"] = []

fields_nomag = deepcopy(fields)
fields_nomag["slice"].remove("bmag")
fields_nomag["proj"].remove("rm")

pngs_nomag = deepcopy(pngs)
pngs_nomag["slice"].remove("bmag")
pngs_nomag["proj"].remove("rm")

filenos = [0, 130, 135, 140, 145, 150, 155,
           160, 165, 170, 175, 180, 185, 190,
           195, 200, 205, 210, 215, 220, 225,
           230, 235, 240, 245, 250, 255, 260,
           265, 270, 275, 280, 285, 290, 295,
           300, 310, 320, 330, 340, 350, 360,
           370, 380, 390, 400, 420, 440, 460,
           480]

mag_dict = OrderedDict()
mag_dict["nomag"] = Simulation("Unmagnetized", filenos,
                               fields_nomag, pngs_nomag,
                               ["x", "y", "z"])
mag_dict["beta1000"] = Simulation(":math:`\\beta` = 1000", filenos,
                                  fields, pngs, ["x", "y", "z"])
"""
mag_dict["beta500"] = Simulation(":math:`\\beta` = 500", filenos,
                                 fields, pngs, ["x", "y", "z"])
"""
mag_dict["beta200"] = Simulation(":math:`\\beta` = 200", filenos,
                                 fields, pngs, ["x", "y", "z"])
mag_dict["beta100"] = Simulation(":math:`\\beta` = 100", filenos,
                                 fields, pngs, ["x", "y", "z"])

mag_physics = list(mag_dict.keys())
