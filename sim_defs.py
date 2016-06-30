from collections import OrderedDict

fid_info = {"name": "fiducial", 
            "basenm": "fiducial",
            "set_name": "A Parameter Space Exploration of Galaxy Cluster Mergers (ZuHone 2011)",
            "set_journal": "ZuHone, J. A. 2011, ApJ, 728, 54",
            "ads_link": "http://adsabs.harvard.edu/abs/2011ApJ...728...54Z",
            "box_size": 14.26,
            "cell_size": 6.96,
            "sim_type": "AMR",
            "primary_mass": "M_{200} = 6~{\\times}~10^{14}~M_{\odot}"}

fid_fields = OrderedDict()
fid_fields["slice"] = OrderedDict([("density", "Gas density in units of :math:`{\\rm M_\odot~kpc^{-3}}`"),
                                   ("dark_matter_density", "Dark matter density in units of :math:`{\\rm M_\odot~kpc^{-3}}`"),
                                   ("kT", "Gas temperature in units of keV"),
                                   ("velocity_x", "The x-component of the gas velocity in units of :math:`{\\rm km~s^{-1}}`"),
                                   ("velocity_y", "The y-component of the gas velocity in units of :math:`{\\rm km~s^{-1}}`"),
                                   ("clr1", "Mass fraction of gas from the primary cluster"),
                                   ("clr2", "Mass fraction of gas from the secondary cluster")])
fid_fields["proj"] = OrderedDict([("xray_emissivity", "X-ray photon surface brightness in the 0.5-7.0 keV (observer) band," + \
                                   "in units of :math:`{\\rm photons~s^{-1}~{cm}^{-2}~{arcsec}^{-2}}`"),
                                  ("kT", "Emission-weighted projected temperature in units of keV"),
                                  ("total_density", "Total mass density (gas and dark matter) in units of :math:`{\\rm M_\odot~{kpc}^{-2}}`"),
                                  ("szy", "Integrated y-parameter for the thermal Sunyaev-Zeldovich (S-Z) effect"),
                                  ("sz_kinetic", "Integrated y-parameter for the kinetic S-Z effect")])
fid_fields["SZ"] = OrderedDict([("tau", "Compton optical depth of the cluster gas"),
                                ("TeSZ", "Mass-weighted projected temperature in units of keV"),
                                ("90_GHz", "S-Z signal at 90 GHz in units of :math:`{\\rm MJy~{steradian}^{-1}}`"), 
                                ("180_GHz", "S-Z signal at 180 GHz in units of :math:`{\\rm MJy~{steradian}^{-1}}`"),
                                ( "240_GHz", "S-Z signal at 240 GHz in units of :math:`{\\rm MJy~{steradian}^{-1}}`")]) 

fid_dict = OrderedDict()
fid_dict["1to1_b0"] = ("R = 1:1, b = 0 kpc",
                       [0, 20, 30, 40, 50, 60, 61, 62, 63,
                        64, 65, 66, 67, 68, 69, 70, 75, 80,
                        85, 90, 100, 110, 120, 125, 126, 127,
                        128, 129, 130, 131, 132, 133, 134, 135,
                        140, 145, 150, 160, 170, 180, 190, 200,
                        210, 220, 240, 260, 280, 300, 350, 400, 450, 500])
fid_dict["1to1_b0.5"] = ("R = 1:1, b = 500 kpc",
                         [0, 20, 30, 40, 50, 60, 65, 66, 67,
                          68, 69, 70, 71, 72, 73, 74, 75, 80,
                          85, 90, 100, 110, 120, 130, 135, 136,
                          137, 138, 139, 140, 141, 142, 143, 144,
                          145, 150, 155, 160, 165, 170, 180, 190,
                          200, 210, 220, 240, 260, 280, 300, 350,
                          400, 450, 500])
fid_dict["1to1_b1"] = ("R = 1:1, b = 1000 kpc",
                       [0, 20, 30, 40, 50, 55, 60, 61, 62,
                        63, 64, 65, 66, 67, 68, 69, 70, 71,
                        72, 73, 74, 75, 80, 90, 100, 110, 120,
                        130, 140, 141, 142, 143, 144, 145, 146,
                        147, 148, 149, 150, 151, 152, 153, 154,
                        155, 160, 165, 170, 175, 180, 190, 200,
                        210, 220, 240, 260, 280, 300, 350, 400,
                        450, 500])
fid_dict["1to3_b0"] = ("R = 1:3, b = 0 kpc",
                       [0, 20, 30, 40, 50, 55, 56, 57, 58, 59, 60,
                        61, 62, 63, 64, 65, 70, 80, 90, 100, 110, 120,
                        130, 140, 141, 142, 143, 144, 145, 146, 147, 148,
                        149, 150, 160, 170, 180, 181, 182, 183, 184, 185,
                        186, 187, 188, 189, 190, 200, 210, 220, 230, 240,
                        250, 260, 300, 350, 400, 450, 500])
fid_dict["1to3_b0.5"] = ("R = 1:3, b = 500 kpc",
                         [0, 20, 30, 40, 50, 55, 56, 57,
                          58, 59, 60, 61, 62, 63, 64, 65,
                          70, 75, 80, 85, 90, 100, 110,
                          120, 130, 140, 145, 150, 151,
                          152, 153, 154, 155, 156, 157,
                          158, 159, 160, 165, 170, 175,
                          180, 185, 190, 195, 200, 210,
                          220, 230, 240, 250, 260, 280,
                          300, 350, 400, 450, 500])
fid_dict["1to3_b1"] = ("R = 1:3, b = 1000 kpc",
                       [0, 20, 30, 40, 50, 55, 60, 61, 62,
                        63, 64, 65, 66, 67, 68, 69, 70, 75,
                        80, 85, 95, 105, 115, 125, 135, 145,
                        155, 160, 165, 170, 171, 172, 173, 174,
                        175, 176, 177, 178, 179, 180, 185, 190,
                        200, 210, 215, 216, 217, 218, 219, 220,
                        221, 222, 223, 224, 225, 230, 240, 250,
                        260, 270, 280, 290, 300, 320, 340, 360,
                        380, 400, 450, 500])
slosh_info = {"name": "sloshing",
              "basenm": "sloshing",
              "set_name": "Sloshing of the Cold Gas in Galaxy Cluster Cores (ZuHone, Markevitch, & Johnson 2010)",
              "set_journal": "ZuHone, J. A., Markevitch, M., & Johnson, R. E. 2010, ApJ, 717, 908",
              "ads_link": "http://adsabs.harvard.edu/abs/2010ApJ...717..908Z",
              "box_size": 10.0,
              "cell_size": 4.88,
              "sim_type": "AMR",
              "primary_mass": "M_{200} = 8.83~{\\times}~10^{14}\\frac{R}{R+1}~M_{\odot}" + \
                  "~\\rm{(where}~\\it{R}~\\rm{is~the~mass~ratio)}"}

slosh_fields = fid_fields.copy()
slosh_fields["slice"].pop("clr1")
slosh_fields["slice"].pop("clr2")

slosh_dict = OrderedDict()
slosh_dict["R5_b500"] = ("R = 1:5, b = 500 kpc, gasless subcluster",
                         [0, 90, 120, 130, 131, 132,
                          133, 134, 135, 136, 137, 138, 139, 140,
                          145, 150, 160, 170, 180, 190, 200, 210,
                          220, 230, 240, 250, 260, 270, 280, 290,
                          300, 310, 320, 330, 340, 350, 360, 370,
                          380, 390, 395, 396, 397, 398, 399, 400,
                          401, 402, 403, 404, 405, 410, 415, 420,
                          430, 440, 450, 460, 470, 480, 490, 500,
                          510, 520, 530, 540, 550, 560, 570, 580,
                          590, 600])
slosh_dict["R20_b200g"] = ("R = 1:20, b = 200 kpc",
                           [0, 90, 120, 125, 130, 131, 132, 133,
                            134, 135, 136, 137, 138, 139, 140,
                            145, 150, 155, 160, 165, 170, 180,
                            190, 200, 210, 220, 240, 260, 280,
                            300, 320, 340, 360, 380, 400, 420,
                            430, 440, 450, 455, 456, 457, 458,
                            459, 460, 461, 462, 463, 464, 465,
                            470, 475, 480, 490, 500, 510, 530,
                            550, 570, 590, 610, 630, 650, 670,
                            690])
slosh_dict["R20_b1000g"] = ("R = 1:20, b = 1000 kpc",
                            [0, 90, 100, 110, 120, 125, 130,
                             135, 136, 137, 138, 139, 140, 141,
                             142, 143, 144, 145, 150, 155, 160,
                             165, 170, 175, 180, 190, 200, 210,
                             220, 230, 240, 250, 260, 270, 280,
                             300, 320, 340, 360, 380, 400, 420,
                             440, 460, 480, 500, 520, 540, 550])

