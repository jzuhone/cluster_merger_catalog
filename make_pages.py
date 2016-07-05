import os
import django.template
import django.conf
import re
import girder_client
from yt.funcs import get_pbar
from fiducial_defs import fid_dict, fid_info
from sloshing_defs import slosh_dict, slosh_info
from viscosity_defs import visc_dict, visc_info
import argparse
from collections import OrderedDict

try:
    django.conf.settings.configure()
    django.setup()
except RuntimeError as msg:
    print(msg)

GIRDER_API_URL = "https://girder.hub.yt/api/v1"

gc = girder_client.GirderClient(apiUrl=GIRDER_API_URL)

def make_set_page(set_info, set_dict):
    if not os.path.exists('source/%s' % set_info['name']):
        os.mkdir('source/%s' % set_info['name'])
    for sim, sim_info in set_dict.items():
        for ax in sim_info.axes:
            make_sim_page(set_info['name'], set_info["filespec"], sim, sim_info.name,
                          sim_info.filenos, sim_info.sname_map, sim_info.lname_map, ax,
                          set_info["cadence"], sim_info.axes)
        make_epoch_pages(set_info['name'], set_info['filespec'], sim, sim_info.name,
                         sim_info.filenos, sim_info.sname_map, sim_info.lname_map,
                         sim_info.unit_map, set_info["cadence"], sim_info.axes)
    context = {'name': set_info["name"],
               'sim_pages': list(set_dict.keys()),
               'set_name': set_info["set_name"],
               'set_journals': set_info["set_journals"],
               'box_size': set_info["box_size"],
               'cell_size': set_info["cell_size"],
               'sim_type': set_info['sim_type'],
               'code': set_info['code'],
               'primary_mass': set_info["primary_mass"],
               'sim_notes': set_info['sim_notes'],
               'notes': set_info['notes'],
               'cosmo_warning': set_info['cosmo_warning']}
    template_file = 'templates/set_template.rst'
    make_template('source/%s/index.rst' % set_info["name"], template_file, context)

def make_sim_page(set_name, filespec, sim, sim_name, filenos, sname_map,
                  lname_map, ax, cadence, axes):
    sim_dir = 'source/%s/%s' % (set_name, sim)
    if not os.path.exists(sim_dir):
        os.mkdir(sim_dir)
    outfile = sim_dir+"/index_%s.rst" % ax
    if not os.path.exists(outfile):
        pbar = get_pbar("Setting up simulation page for "+sim+", %s" % ax, len(filenos))
        epochs = OrderedDict()
        imgs = OrderedDict()
        for fileno in filenos:
            fn = "%04d" % fileno
            pngs = {}
            for fd, field in sname_map["proj"].items():
                filename = filespec % (sim, fileno) + "_proj_%s_%s" % (ax, field)
                pngs[fd] = get_file(filename)
            epochs[fn] = "t = %4.2f Gyr" % (fileno*cadence)
            imgs[fn] = pngs
            pbar.update()
        pbar.finish()
        num_epochs = len(epochs.keys())
        context = {'sim_name': sim_name,
                   'ax': ax,
                   'axes': axes,
                   'epochs': epochs,
                   'imgs': imgs,
                   'num_epochs': num_epochs-1,
                   'filenos': ["%04d" % i for i in filenos],
                   'names': lname_map["proj"]}
        template_file = 'templates/sim_template.rst'
        make_template(outfile, template_file, context)

def make_template(outfile, template_file, context):
    django_context = django.template.Context(context)
    template = open(template_file).read()
    template = re.sub(r' %}\n', ' %}', template)
    template = django.template.Template(template)
    open(outfile, 'w').write(template.render(django_context))

def make_epoch_pages(set_name, filespec, sim, sim_name, filenos, sname_map,
                     lname_map, unit_map, cadence, axes):
    pbar = get_pbar("Setting up epoch pages for simulation "+sim, len(filenos))
    num_epochs = len(filenos)
    for noi, fileno in enumerate(filenos):
        outfile = "source/%s/%s/%04d.rst" % (set_name, sim, fileno)
        if not os.path.exists(outfile):
            data = {}
            for itype in sname_map.keys():
                data[itype] = OrderedDict()
                for ax in axes:
                    if itype == "slice" and ax != "z":
                        continue
                    data[itype][ax] = {}
                    filename = filespec % (sim, fileno) + "_%s_%s" % (itype, ax)
                    data[itype][ax]['fits'] = get_file(filename)
                    imgs = {}
                    for link, field in sname_map[itype].items():
                        imgs[link] = get_file(filename+"_"+field)
                    data[itype][ax]['pngs'] = imgs
            template_file = 'templates/epoch_template.rst'
            timestr = "t = %4.2f Gyr" % (fileno*cadence)
            if noi == 0:
                prev_link = ""
                dis_prev = "disabled"
            else:
                prev_link = "%04d.html" % filenos[noi-1]
                dis_prev = ""
            if noi == num_epochs-1:
                next_link = ""
                dis_next =  "disabled"
            else:
                next_link = "%04d.html" % filenos[noi+1]
                dis_next = ""
            context = {"data": data,
                       "sim_name": sim_name,
                       "timestr": timestr,
                       "slice_names": lname_map["slice"],
                       "proj_names": lname_map["proj"],
                       "sz_names": lname_map["SZ"],
                       "slice_fields": unit_map["slice"],
                       "proj_fields": unit_map["proj"],
                       "sz_fields": unit_map["SZ"],
                       "prev_link": prev_link,
                       "next_link": next_link,            
                       "dis_prev": dis_prev,
                       "dis_next": dis_next}
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
    make_set_page(visc_info, visc_dict)
    
