from collections import OrderedDict
from sim_defs import Simulation
from copy import deepcopy

virgo_notes = ["There is no metallicity field in these simulations; hence for computing X-ray "+
               "emissivities a constant metallicity of :math:`Z = 0.3~Z_\odot` is assumed.",
               "Simulations with viscosity and/or thermal conduction were restarted from their "+
               "corresponding ideal HD/MHD simulations at core passage, hence for these simulations "+
               "there are no earlier snapshots available.",
               "For each simulation, the main cluster is fixed at **r** = [0, 0, 0] kpc. "+
               "A tab-separated ASCII table containing the subcluster position, velocity, "+
               "and acceleration as a function of time may be found "+
               "`here <https://girder.hub.yt/api/v1/file/57c9d6297f248300018398ed/download>`_."]

virgo_acks = "This set of simulations was performed using the Pleiades supercomputer at NASA's Ames Research Center."

virgo_info = {"name": "virgo",
             "cadence": 0.05,
             "filespec": "virgo_%s.%04d",
             "set_name": "Simulations of the Virgo Cold Fronts with Magnetic Fields and Viscosity",
             "set_journals": [("ZuHone, J. A., Kunz, M. W., Markevitch, M., Stone, J. M., & Biffi, V. 2015, ApJ, 798, 90",
                               "http://adsabs.harvard.edu/abs/2015ApJ...798...90Z"),
                              ("Werner, N., ZuHone, J. A., Zhuravleva, I., et al. 2016, MNRAS, 455, 846",
                               "http://adsabs.harvard.edu/abs/2016MNRAS.455..846W")],
             "box_size": "4 Mpc",
             "cell_size": "0.488-0.977 kpc",
             "sim_type": "SMR",
             "code": "Athena",
             "primary_mass": "M_{200} = 1.51\\times10^{14}~M_{\odot}",
             "sim_notes": "For the following simulations, :math:`\\beta = p_{\\rm th}/p_B`.",
             "notes": virgo_notes, "cosmo_warning": True, 'redshift': 0.0036}

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

virgo_dict = OrderedDict()
virgo_dict["nomag"] = Simulation("Unmagnetized, Inviscid",
                                 [0, 18, 20, 22, 24, 26, 28, 30, 32,
                                  34, 36, 38, 40, 42, 44, 46, 48, 50,
                                  52, 54], fields_nomag, pngs_nomag,
                                 ["x", "y", "z"])
virgo_dict["nomag_visc"] = Simulation("Unmagnetized, 10\% Isotropic Spitzer Viscosity",
                                      [22, 24, 26, 28, 30, 32,
                                       34, 36, 38, 40, 42, 44, 46, 48, 50,
                                       52, 54], fields_nomag, pngs_nomag,
                                      ["x", "y", "z"])
virgo_dict["novisc"] = Simulation(":math:`\\beta` = 1000, Inviscid",
                                 [0, 18, 20, 22, 24, 26, 28, 30, 32, 
                                  34, 36, 38, 40, 42, 44, 46, 48, 50, 
                                  52, 54], fields, pngs, ["x", "y", "z"])
virgo_dict["beta_100"] = Simulation(":math:`\\beta` = 100, Inviscid",
                                    [0, 18, 20, 22, 24, 26, 28, 30, 32,
                                     34, 36, 40, 42, 44, 46, 48, 50,
                                     52, 54], fields, pngs, ["x", "y", "z"])
virgo_dict["avisc1"] = Simulation(":math:`\\beta` = 1000, Braginskii Viscosity",
                                 [22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42,
                                  44, 46, 48, 50, 52, 54], fields, pngs,
                                 ["x", "y", "z"])
virgo_dict["ivisc1"] = Simulation(":math:`\\beta` = 1000, Isotropic Spitzer Viscosity",
                                 [22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42,
                                  44, 46, 48, 50, 52, 54], fields, pngs,
                                 ["x", "y", "z"])
virgo_dict["ivisc0.1"] = Simulation(":math:`\\beta` = 1000, 10\% Isotropic Spitzer Viscosity",
                                    [22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42,
                                     44, 46, 48, 50, 52, 54], fields, pngs,
                                    ["x", "y", "z"])
virgo_dict["cond"] = Simulation(":math:`\\beta` = 1000, Anisotropic Thermal Conduction",
                                [22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42,
                                 44, 46, 48, 50, 52, 54], fields, pngs,
                                ["x", "y", "z"])
virgo_dict["cond_visc"] = Simulation(":math:`\\beta` = 1000, Braginskii Viscosity, Anisotropic Thermal Conduction",
                                     [22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42,
                                      44, 46, 48, 50, 52, 54], fields, pngs,
                                     ["x", "y", "z"])

virgo_physics = list(virgo_dict.keys())
