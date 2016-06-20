import os
import django.template
import django.conf
import re
import girder_client
from yt.funcs import get_pbar
from sim_defs import \
    fid_dict, fid_info, \
    slosh_info, slosh_dict,\
    test_info, test_dict
import argparse
import json

cadence = {"fiducial":0.02, "sloshing":0.01}

try:
    django.conf.settings.configure()
    django.setup()
except RuntimeError as msg:
    print(msg)

GIRDER_API_URL = "https://girder.hub.yt/api/v1"

gc = girder_client.GirderClient(apiUrl=GIRDER_API_URL)

itypes = ["slice", "proj", "SZ", "cxo_evt"]

type_map = {"slice":["density","kT","dark_matter_density"],
            "proj":["xray_emissivity","kT","total_density","szy"],
            "SZ":["Tau","240_GHz"],
            "cxo_evt":["counts"]}

def make_set_page(set_info, set_dict):
    if not os.path.exists('source/%s' % set_info['name']):
        os.mkdir('source/%s' % set_info['name'])
    sim_pages = []
    for sim, sim_info in set_dict.items():
        sim_pages.append(make_png_page(set_info['name'], set_info["basenm"], sim, sim_info[0], sim_info[1]))
        make_json(set_info['name'], set_info['basenm'], sim, sim_info[1])
    context = {'name': set_info["name"],
               'sim_pages': sim_pages,
               'set_name': set_info["set_name"],
               'ads_link': set_info["ads_link"],
               'set_journal': set_info["set_journal"],
               'box_size': set_info["box_size"],
               'cell_size': set_info["cell_size"]}
    template_file = 'templates/set_template.rst'
    make_template('source/%s/index.rst' % set_info["name"], template_file, context)
    context = {'basenm': set_info['basenm'],
               'cadence': cadence[set_info['basenm']]}
    template_file = 'templates/get_files.rst'
    make_template('source/%s/get_files.rst' % set_info["name"], template_file, context)

def make_png_page(set_name, basenm, sim, sim_name, filenos):
    outfile = "source/%s/%s.rst" % (set_name, sim)
    if not os.path.exists(outfile):
        info = []
        pbar = get_pbar("Setting up simulation page for "+sim, len(filenos))
        for fileno in filenos:
            imgs = {}
            for field in ["xray_emissivity","kT","total_density","szy"]:
                filename = basenm+"_%s_hdf5_plt_cnt_%04d_proj_z_%s" % (sim, fileno, field)
                imgs[field] = get_file(filename)
            time = "t = %4.2f Gyr" % (fileno*cadence[basenm])
            info.append(["%04d" % fileno, time, imgs])
            pbar.update()
        pbar.finish()
        context = {'sim': sim,
                   'sim_name': sim_name,
                   'info': info}
        template_file = 'templates/sim_template.rst'
        make_template(outfile, template_file, context)
    return os.path.split(outfile[:-4])[-1]

def make_template(outfile, template_file, context):
    django_context = django.template.Context(context)
    template = open(template_file).read()
    template = re.sub(r' %}\n', ' %}', template)
    template = django.template.Template(template)
    open(outfile, 'w').write(template.render(django_context))

def make_json(set_name, basenm, sim, filenos):
    data = {}
    pbar = get_pbar("Setting up JSON for simulation "+sim, len(filenos))
    for fileno in filenos:
        data[fileno] = {}
        for itype in itypes:
            data[fileno][itype] = {}
            for ax in "xyz":
                if itype == "slice" and ax != "z":
                    continue
                data[fileno][itype][ax] = {}
                filename = basenm+"_%s_hdf5_plt_cnt_%04d_%s_%s" % (sim, fileno, itype, ax)
                data[fileno][itype][ax]['fits'] = get_file(filename)
                imgs = []
                for field in type_map[itype]:
                    imgs.append(get_file(filename+"_"+field))
                data[fileno][itype][ax]['pngs'] = imgs
        pbar.update()
    pbar.finish()
    outfile = "source/%s/%s.json" % (set_name, sim)
    with open(outfile, 'w') as f:
        json.dump(data, f)

def get_file(filename):
    item = gc.get("resource/search", {"q": filename, "types": '["item"]'})['item'][0]
    return "http://girder.hub.yt/api/v1/item/%s/download" % item['_id']

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action='store_true')
    args = parser.parse_args()
    if args.test:
        make_set_page(test_info, test_dict)
    else:
        make_set_page(fid_info, fid_dict)
        make_set_page(slosh_info, slosh_dict)
