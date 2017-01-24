from collections import OrderedDict

unit_map = {}
unit_map["slice"] = {"dens": "Gas density in units of :math:`{\\rm M_\odot~kpc^{-3}}`",
                     "pden": "Dark matter density in units of :math:`{\\rm M_\odot~kpc^{-3}}`",
                     "temp": "Gas temperature in units of keV",
                     "velx": "The x-component of the gas velocity in units of :math:`{\\rm km~s^{-1}}`",
                     "vely": "The y-component of the gas velocity in units of :math:`{\\rm km~s^{-1}}`",
                     "bmag": "The magnetic field strength in units of :math:`{\\rm \mu{G}}`",
                     "clr1": "Mass fraction of gas from the primary cluster",
                     "clr2": "Mass fraction of gas from the secondary cluster"}
unit_map["proj"] = {"xray": "X-ray photon surface brightness in the 0.5-7.0 keV (observer) band, " + \
                    "in units of :math:`{\\rm photons~s^{-1}~{cm}^{-2}~{arcsec}^{-2}}`",
                    "temp": "Emission-weighted projected temperature in units of keV",
                    "dens": "Total mass density (gas and dark matter) in units of :math:`{\\rm M_\odot~{kpc}^{-2}}`",
                    "szy": "Integrated y-parameter for the thermal Sunyaev-Zeldovich (S-Z) effect",
                    "szk": "Integrated y-parameter for the kinetic S-Z effect",
                    "rm": "Faraday rotation measure in units of :math:`{\\rm rad~m^{-2}}`"}
unit_map["SZ"] = {"tau": "Compton optical depth of the cluster gas",
                  "temp": "Mass-weighted projected temperature in units of keV",
                  "inty90": "S-Z signal at 90 GHz in units of :math:`{\\rm MJy~{steradian}^{-1}}`",
                  "inty180": "S-Z signal at 180 GHz in units of :math:`{\\rm MJy~{steradian}^{-1}}`",
                  "inty240": "S-Z signal at 240 GHz in units of :math:`{\\rm MJy~{steradian}^{-1}}`"}

name_map = {}
name_map["slice"] = {"dens": ("density", "Density"),
                     "temp": ("kT", "Temperature"),
                     "bmag": ("magnetic_field_strength", "Magnetic Field Strength"),
                     "pden": ("dark_matter_density", "Dark Matter Density"),
                     "velx": ("velocity_x", "X-Velocity"),
                     "vely": ("velocity_y", "Y-Velocity"),
                     "clr1": ("clr1", "Primary Mass Fraction"),
                     "clr2": ("clr2", "Secondary Mass Fraction")}
name_map["proj"] = {"xray": ("xray_emissivity", "X-ray Emissivity"),
                    "temp": ("kT", "Temperature"),
                    "dens": ("total_density", "Total Density"),
                    "szy": ("szy", "Compton-y"),
                    "szk": ("sz_kinetic", "Compton-y Kinetic"),
                    "rm": ("rotation_measure", "Faraday Rotation Measure")}
name_map["SZ"] = {"tau": ("Tau", "Compton Optical Depth"),
                  "temp": ("TeSZ", "Temperature"),
                  "inty90": ("90_GHz", "S-Z Signal (90 GHz)"),
                  "inty180": ("180_GHz", "S-Z Signal (180 GHz)"),
                  "inty240": ("240_GHz", "S-Z Signal (240 GHz)")}
name_map["cxo_evt"] = {"counts":("counts","ACIS-I Counts Map")}
name_map["galaxies"] = {"ppv":("ppv","Galaxy Positions and Velocities")}

class Simulation(object):

    def __init__(self, sim_name, filenos, fields, pngs, proj_axes,
                 slice_axes, cat_type='epoch', halo_info=None,
                 hubble=71, omega_m=0.27, omega_l=0.73, **kwargs):
        self.name = sim_name
        self.filenos = filenos
        self.lname_map = {}
        self.sname_map = {}
        self.unit_map = {}
        self.slice_axes = slice_axes
        self.proj_axes = proj_axes
        self.cat_type = cat_type
        for itype in pngs:
            self.lname_map[itype] = OrderedDict()
            self.sname_map[itype] = OrderedDict()
            for name in pngs[itype]:
                self.sname_map[itype][name] = name_map[itype][name][0]
                self.lname_map[itype][name] = name_map[itype][name][1]
        for itype in fields:
            self.unit_map[itype] = OrderedDict()
            for name in fields[itype]:
                n = name_map[itype][name][0]
                self.unit_map[itype][n] = unit_map[itype][name]
        self.halo_info = halo_info
        self.cosmo = {"hubble": hubble, "omega_m": omega_m, "omega_l": omega_l}
        if "sigma8" in kwargs:
            self.cosmo["sigma8"] = kwargs["sigma8"]
        if "omega_b" in kwargs:
            self.cosmo["omega_b"] = kwargs["omega_b"]
