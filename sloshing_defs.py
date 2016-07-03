from collections import OrderedDict
from sim_defs import Simulation
    
slosh_info = {"name": "sloshing",
              "cadence": 0.01,
              "filespec": "sloshing_%s_hdf5_plt_cnt_%04d",
              "set_name": "Sloshing of the Cold Gas in Galaxy Cluster Cores (ZuHone, Markevitch, & Johnson 2010)",
              "set_journal": "ZuHone, J. A., Markevitch, M., & Johnson, R. E. 2010, ApJ, 717, 908",
              "ads_link": "http://adsabs.harvard.edu/abs/2010ApJ...717..908Z",
              "box_size": 10.0,
              "cell_size": 4.88,
              "sim_type": "AMR",
              "code": "FLASH",
              "primary_mass": "M_{200} = 8.83~{\\times}~10^{14}\\frac{R}{R+1}~M_{\odot}" + \
              "~\\rm{(where}~\\it{R}~\\rm{is~the~mass~ratio)}"}

fields = {}
fields["slice"] = ["dens","temp","pden","velx","vely"]
fields["proj"] = ["xray","temp","dens","szy","szk"]
fields["SZ"] = ["tau","temp","inty90","inty180","inty240"]
pngs = {}
pngs["slice"] = ["dens","temp","pden"]
pngs["proj"] = ["xray","temp","dens","szy"]
pngs["SZ"] = ["tau","inty240"]
pngs["cxo_evt"] = ["counts"]

slosh_dict = OrderedDict()
slosh_dict["R5_b500"] = Simulation("R = 1:5, b = 500 kpc, gasless secondary",
                                   [0, 90, 120, 130, 131, 132,
                                    133, 134, 135, 136, 137, 138, 139, 140,
                                    145, 150, 160, 170, 180, 190, 200, 210,
                                    220, 230, 240, 250, 260, 270, 280, 290,
                                    300, 310, 320, 330, 340, 350, 360, 370,
                                    380, 390, 395, 396, 397, 398, 399, 400,
                                    401, 402, 403, 404, 405, 410, 415, 420,
                                    430, 440, 450, 460, 470, 480, 490, 500,
                                    510, 520, 530, 540, 550, 560, 570, 580,
                                    590, 600], fields, pngs, ["x", "y", "z"])
slosh_dict["R5_b500_visc"] = Simulation("R = 1:5, b = 500 kpc, gasless secondary with viscosity",
                                        [0, 90, 120, 130, 131, 132,
                                         133, 134, 135, 136, 137, 138, 139, 140,
                                         145, 150, 160, 170, 180, 190, 200, 210,
                                         220, 230, 240, 250, 260, 270, 280, 290,
                                         300, 310, 320, 330, 340, 350, 360, 370,
                                         380, 390, 395, 396, 397, 398, 399, 400,
                                         401, 402, 403, 404, 405, 410, 415, 420,
                                         430, 440, 450, 460, 470, 480, 490, 500,
                                         510, 520, 530, 540, 550, 560, 570, 580,
                                         590, 600], fields, pngs, ["x", "y", "z"])
slosh_dict["R20_b200g"] = Simulation("R = 1:20, b = 200 kpc",
                                     [0, 90, 120, 125, 130, 131, 132, 133,
                                      134, 135, 136, 137, 138, 139, 140,
                                      145, 150, 155, 160, 165, 170, 180,
                                      190, 200, 210, 220, 240, 260, 280,
                                      300, 320, 340, 360, 380, 400, 420,
                                      430, 440, 450, 455, 456, 457, 458,
                                      459, 460, 461, 462, 463, 464, 465,
                                      470, 475, 480, 490, 500, 510, 530,
                                      550, 570, 590, 610, 630, 650, 670,
                                      690], fields, pngs, ["x", "y", "z"])
slosh_dict["R20_b1000g"] = Simulation("R = 1:20, b = 1000 kpc",
                                      [0, 90, 100, 110, 120, 125, 130,
                                       135, 136, 137, 138, 139, 140, 141,
                                       142, 143, 144, 145, 150, 155, 160,
                                       165, 170, 175, 180, 190, 200, 210,
                                       220, 230, 240, 250, 260, 270, 280,
                                       300, 320, 340, 360, 380, 400, 420,
                                       440, 460, 480, 500, 520, 540, 550],
                                      fields, pngs, ["x", "y", "z"])
