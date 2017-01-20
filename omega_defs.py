from collections import OrderedDict
from sim_defs import Simulation
from utils import process_filenos

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
#pngs["cxo_evt"] = ["counts"]

omega_physics = ["non_radiative/1.0005"]

f = open("halolist_a1.0005.txt", "r")
lines = f.readlines()
f.close()

halo_ids = []
halo_mvir = []
halo_m200c = []
halo_m500c = []
halo_rvir = []
halo_r200c = []
halo_r500c = []

for line in lines[1:]:
    words = line.strip().split()
    halo_ids.append(int(words[0]))
    halo_mvir.append(float(words[1]))
    halo_m200c.append(float(words[2]))
    halo_m500c.append(float(words[3]))
    halo_rvir.append(float(words[4]))
    halo_r200c.append(float(words[5]))
    halo_r500c.append(float(words[6]))

omega_dict = OrderedDict()
omega_dict["non_radiative/1.0005"] = Simulation("Non-Radiative, z = 0", process_filenos(halo_ids, fmt="%05d"),
                                                fields, pngs, ["x", "y", "z"], ["x", "y", "z"])
