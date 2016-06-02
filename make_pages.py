import os
import django.template
import django.conf
import re
import girder_client
from collections import OrderedDict

try:
    django.conf.settings.configure()
    django.setup()
except RuntimeError as msg:
    print(msg)

GIRDER_API_URL = "https://girder.hub.yt/api/v1"

gc = girder_client.GirderClient(apiUrl=GIRDER_API_URL)

sim_dict = OrderedDict()
sim_dict["1to3_b0"] = ("R = 1:3, b = 0 kpc", 
                       [0, 20, 30, 40, 50, 55, 56, 57, 58, 59, 60, 
                        61, 62, 63, 64, 65, 70, 80, 90, 100, 110, 120,
                        130, 140, 141, 142, 143, 144, 145, 146, 147, 148,
                        149, 150, 160, 170, 180, 181, 182, 183, 184, 185, 
                        186, 187, 188, 189, 190, 200, 210, 220, 230, 240, 
                        250, 260, 300, 350, 400, 450, 500])
sim_dict["1to3_b1"] = ("R = 1:3, b = 1000 kpc",
                       [0, 20, 30, 40, 50, 55, 60, 61, 62,
                        63, 64, 65, 66, 67, 68, 69, 70, 75,
                        80, 85, 95, 105, 115, 125, 135, 145,
                        155, 160, 165, 170, 171, 172, 173, 174,
                        175, 176, 177, 178, 179, 180, 185, 190,
                        200, 210, 215, 216, 217, 218, 219, 220,
                        221, 222, 223, 224, 225, 230, 240, 250,
                        260, 270, 280, 290, 300, 320, 340, 360,
                        380, 400, 450, 500])

def make_main_page(sims):
    sim_pages = []
    for sim, sim_info in sims.items():
        sim_pages.append(make_png_page(sim, sim_info[0], sim_info[1]))
    context = {'sim_pages': sim_pages}
    template_file = 'templates/index_template.rst'
    make_template('source/index.rst', template_file, context)

def make_png_page(sim, sim_name, filenos):
    info = []
    for fileno in filenos:
        imgs = {}
        for field in ["xray_emissivity","kT","total_density","szy"]:
            filename = "fiducial_%s_hdf5_plt_cnt_%04d_proj_z_%s" % (sim, fileno, field)
            item = gc.get("resource/search", {"q": filename, "types": '["item"]'})['item'][0]
            imgs[field] = "http://girder.hub.yt/api/v1/item/%s/download" % item['_id']
        time = "t = %4.2f Gyr" % (fileno*0.02)
        info.append(["%04d" % fileno, time, imgs])
    outfile = "source/%s.rst" % sim
    context = {'sim': sim,
               'sim_name': sim_name,
               'info': info,
               }
    template_file = 'templates/sim_template.rst'
    make_template(outfile, template_file, context)
    return os.path.split(outfile[:-4])[-1]

def make_template(outfile, template_file, context):
    django_context = django.template.Context(context)
    template = open(template_file).read()
    template = re.sub(r' %}\n', ' %}', template)
    template = django.template.Template(template)
    open(outfile, 'w').write(template.render(django_context))

if __name__ == "__main__":
    make_main_page(sim_dict)