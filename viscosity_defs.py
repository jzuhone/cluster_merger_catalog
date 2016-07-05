from collections import OrderedDict
from sim_defs import Simulation

visc_notes = ["There is no metallicity field in these simulations; hence for computing X-ray "+
              "emissivities a constant metallicity of :math:`Z = 0.3~Z_\odot` is assumed."]

visc_info = {"name": "viscosity",
             "cadence": 0.05,
             "filespec": "virgo_%s.%04d",
             "set_name": "The Effect of Anisotropic Viscosity on Cold Fronts in Galaxy Clusters (ZuHone et al. 2015)",
             "set_journals": [("ZuHone, J. A., Kunz, M. W., Markevitch, M., Stone, J. M., & Biffi, V. 2015, ApJ, 798, 90",
                               "http://adsabs.harvard.edu/abs/2015ApJ...798...90Z"),
                              ("Werner, N., ZuHone, J. A., Zhuravleva, I., et al. 2016, MNRAS, 455, 846",
                               "http://adsabs.harvard.edu/abs/2016MNRAS.455..846W")],
             "box_size": "4 Mpc",
             "cell_size": "0.488-0.977 kpc",
             "sim_type": "SMR",
             "code": "Athena",
             "primary_mass": "TBD",
             "sim_notes": "For the following simulations, :math:`\\beta = p_{\\rm th}/p_B`.",
             "notes": visc_notes, "cosmo_warning": True}

fields = {}
fields["slice"] = ["dens","temp","bmag","velx","vely"]
fields["proj"] = ["xray","temp","szy","szk","rm"]
fields["SZ"] = []
pngs = {}
pngs["slice"] = ["dens","temp","bmag"]
pngs["proj"] = ["xray","temp","szy","rm"]
pngs["cxo_evt"] = ["counts"]
pngs["SZ"] = []

filenos = [0, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36,
           38, 40, 42, 44, 46, 48, 50, 52, 54]
           
visc_dict = OrderedDict()
visc_dict["novisc"] = Simulation(":math:`\\beta` = 1000, Inviscid",
                                 filenos, fields, pngs,
                                 ["x", "y", "z"])
