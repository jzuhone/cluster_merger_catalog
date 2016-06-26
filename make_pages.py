import os
import django.template
import django.conf
import re
import girder_client
from yt.funcs import get_pbar
from sim_defs import \
    fid_dict, fid_info, \
    slosh_info, slosh_dict
import argparse
from collections import OrderedDict

cadence = {"fiducial": 0.02, 
           "sloshing": 0.01}

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

link_map = {"slice":["dens","temp","pden"],
            "proj":["xray","temp","dens","szy"],
            "SZ":["tau","inty"],
            "cxo_evt":["counts"]}

def make_set_page(set_info, set_dict):
    if not os.path.exists('source/%s' % set_info['name']):
        os.mkdir('source/%s' % set_info['name'])
    for sim, sim_info in set_dict.items():
        if sim[-2:] == "b0":
            axes = "xz"
        else:
            axes = "xyz"
        for ax in axes:
            make_sim_page(set_info['name'], set_info["basenm"], sim, sim_info[0], sim_info[1], ax)
        make_epoch_pages(set_info['name'], set_info['basenm'], sim, sim_info[0], sim_info[1])
    context = {'name': set_info["name"],
               'sim_pages': list(set_dict.keys()),
               'set_name': set_info["set_name"],
               'ads_link': set_info["ads_link"],
               'set_journal': set_info["set_journal"],
               'box_size': set_info["box_size"],
               'cell_size': set_info["cell_size"],
               'sim_type': set_info['sim_type'],
               'primary_mass': set_info["primary_mass"]}
    template_file = 'templates/set_template.rst'
    make_template('source/%s/index.rst' % set_info["name"], template_file, context)

def make_sim_page(set_name, basenm, sim, sim_name, filenos, ax):
    sim_dir = 'source/%s/%s' % (set_name, sim)
    if not os.path.exists(sim_dir):
        os.mkdir(sim_dir)
    outfile = sim_dir+"/index_%s.rst" % ax
    if sim[-2:] == "b0":
        axes = ["x","z"]
    else:
        axes = ["x", "y", "z"]
    if not os.path.exists(outfile):
        pbar = get_pbar("Setting up simulation page for "+sim+", %s" % ax, len(filenos))
        epochs = {}
        imgs = {}
        for fileno in filenos:
            fn = "%04d" % fileno
            pngs = {}
            for fd, field in zip(link_map["proj"], ["xray_emissivity","kT","total_density","szy"]):
                filename = basenm+"_%s_hdf5_plt_cnt_%04d_proj_%s_%s" % (sim, fileno, ax, field)
                pngs[fd] = get_file(filename)
            epochs[fn] = "t = %4.2f Gyr" % (fileno*cadence[basenm])
            imgs[fn] = pngs
            pbar.update()
        pbar.finish()
        context = {'sim_name': sim_name,
                   'ax': ax,
                   'axes': axes,
                   'epochs': epochs,
                   'imgs': imgs}
        template_file = 'templates/sim_template.rst'
        make_template(outfile, template_file, context)

def make_template(outfile, template_file, context):
    django_context = django.template.Context(context)
    template = open(template_file).read()
    template = re.sub(r' %}\n', ' %}', template)
    template = django.template.Template(template)
    open(outfile, 'w').write(template.render(django_context))

def make_epoch_pages(set_name, basenm, sim, sim_name, filenos):
    pbar = get_pbar("Setting up epoch pages for simulation "+sim, len(filenos))
    for fileno in filenos:
        outfile = "source/%s/%s/%04d.rst" % (set_name, sim, fileno)
        if not os.path.exists(outfile):
            if sim[-2:] == "b0":
                axes = "xz"
            else:
                axes = "xyz"
            data = {}
            for itype in itypes:
                data[itype] = OrderedDict()
                for ax in axes:
                    if itype == "slice" and ax != "z":
                        continue
                    data[itype][ax] = {}
                    filename = basenm+"_%s_hdf5_plt_cnt_%04d_%s_%s" % (sim, fileno, itype, ax)
                    data[itype][ax]['fits'] = get_file(filename)
                    imgs = {}
                    for field, link in zip(type_map[itype], link_map[itype]):
                        imgs[link] = get_file(filename+"_"+field)
                    data[itype][ax]['pngs'] = imgs
            template_file = 'templates/epoch_template.rst'
            timestr = "t = %4.2f Gyr" % (fileno*cadence[basenm])
            context = {"data": data,
                       "sim_name": sim_name,
                       "timestr": timestr}
            make_template(outfile, template_file, context)
        pbar.update()
    pbar.finish()

def get_file(filename):
    items = gc.get("resource/search", {"q": '"'+filename+'"', "types": '["item"]'})['item']
    if len(items) == 0:
        return "https://girder.hub.yt/static/built/plugins/ythub/extra/img/yt_logo.png"
    else:
        return "https://girder.hub.yt/api/v1/item/%s/download" % items[0]['_id']

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action='store_true')
    args = parser.parse_args()
    make_set_page(fid_info, fid_dict)
    make_set_page(slosh_info, slosh_dict)
