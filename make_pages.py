import os
import django.template
import django.conf
import re
import girder_client
from sim_defs import \
    fid_dict, fid_info, \
    slosh_info, slosh_dict,\
    test_info, test_dict

cadence = {"fiducial":0.02, "sloshing":0.01}

try:
    django.conf.settings.configure()
    django.setup()
except RuntimeError as msg:
    print(msg)

GIRDER_API_URL = "https://girder.hub.yt/api/v1"

gc = girder_client.GirderClient(apiUrl=GIRDER_API_URL)

def make_set_page(set_info, set_dict):
    sim_pages = []
    for sim, sim_info in set_dict.items():
        sim_pages.append(make_png_page(set_info["basenm"], sim, sim_info[0], sim_info[1]))
    context = {'name': set_info["name"],
               'sim_pages': sim_pages,
               'set_name': set_info["set_name"],
               'ads_link': set_info["ads_link"],
               'set_journal': set_info["set_journal"],
               'box_size': set_info["box_size"],
               'cell_size': set_info["cell_size"]}
    template_file = 'templates/set_template.rst'
    make_template('source/%s.rst' % set_info["name"], template_file, context)

def make_png_page(basenm, sim, sim_name, filenos):
    info = []
    for fileno in filenos:
        imgs = {}
        for field in ["xray_emissivity","kT","total_density","szy"]:
            filename = basenm+"_%s_hdf5_plt_cnt_%04d_proj_z_%s" % (sim, fileno, field)
            item = gc.get("resource/search", {"q": filename, "types": '["item"]'})['item'][0]
            imgs[field] = "http://girder.hub.yt/api/v1/item/%s/download" % item['_id']
        time = "t = %4.2f Gyr" % (fileno*cadence[basenm])
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
    #make_set_page(test_info, test_dict)
    #make_set_page(fid_info, fid_dict)
    make_set_page(slosh_info, slosh_dict)
