from collections import OrderedDict
from sim_defs import Simulation
from utils import process_filenos
import numpy as np

omega_notes = ["For the non-radiative simulation, there is no metallicity field; hence for computing X-ray " +
               "emissivities a constant metallicity of :math:`Z = 0.3~Z_\odot` is assumed."]

omega_acks = ""

omega_info = {"name": "omega500",
              "cadence": 0.0,
              "filespec": "a%s_cl%s",
              "set_name": "Omega 500 Simulations",
              "set_journals": [("Nelson, K., Lau, E. T., Nagai, D., Rudd, D. H., & Yu, L. 2014, ApJ, 782, 107",
                                "http://adsabs.harvard.edu/abs/2014ApJ...782..107N")],
              "box_size": "500 comoving Mpc/h",
              "cell_size": "3.81 comoving kpc/h",
              "sim_type": "AMR",
              "code": "ART",
              "sim_notes": "",
              "primary_mass": "",
              "notes": omega_notes, "cosmo_warning": False, 'redshift': ""}

fields = {}
fields["slice"] = ["dens","temp","velx","vely"]
fields["proj"] = ["xray","temp","dens","szy","szk"]
fields["SZ"] = ["tau","temp","inty90","inty180","inty240"]
pngs = {}
pngs["slice"] = ["dens","temp"]
pngs["proj"] = ["xray","temp","dens","szy"]
pngs["SZ"] = ["tau","inty240"]
pngs["cxo_evt"] = ["counts"]

omega_physics = [("non_radiative", "1.0005")]

f = open("halolist_a1.0005.txt", "r")
lines = f.readlines()
f.close()

halo_ids = []
halo_info = []

for line in lines[1:]:
    halo_dict = OrderedDict()
    words = line.strip().split()
    halo_ids.append(int(words[0]))
    masses = np.modf(np.log10(np.array(words[1:4]).astype("float")))
    halo_dict[":math:`M_{vir}`"] = ":math:`\\rm{%5.3f \\times 10^{%d}~M_\odot}`" % (10**masses[0][0], masses[1][0])
    halo_dict[":math:`M_{200c}`"] = ":math:`\\rm{%5.3f \\times 10^{%d}~M_\odot}`" % (10**masses[0][1], masses[1][1])
    halo_dict[":math:`M_{500c}`"] = ":math:`\\rm{%5.3f \\times 10^{%d}~M_\odot}`" % (10**masses[0][2], masses[1][2])
    halo_dict[":math:`r_{vir}`"] = ":math:`\\rm{%s kpc}`" % words[4]
    halo_dict[":math:`r_{200c}`"] = ":math:`\\rm{%s kpc}`" % words[5]
    halo_dict[":math:`r_{500c}`"] = ":math:`\\rm{%s kpc}`" % words[6]
    halo_info.append(halo_dict)
    
omega_dict = OrderedDict()
omega_dict[("non_radiative", "1.0005")] = Simulation("Non-Radiative, z = 0", process_filenos(halo_ids, fmt="%05d"),
                                                     fields, pngs, ["x", "y", "z"], ["x", "y", "z"], cat_type='halo',
                                                     halo_info=halo_info)
