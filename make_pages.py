import os
import re
import girder_client
from yt.funcs import get_pbar
from fiducial_defs import fid_dict, fid_info, fid_physics, fid_acks
from sloshing_defs import slosh_dict, slosh_info, slosh_physics, slosh_acks
from virgo_defs import virgo_dict, virgo_info, virgo_physics, virgo_acks
from magnetic_defs import mag_dict, mag_info, mag_physics, mag_acks
from omega_defs import omega_dict, omega_info, omega_physics, omega_acks
import argparse
from collections import OrderedDict
import jinja2

GIRDER_API_URL = "https://girder.hub.yt/api/v1"

gc = girder_client.GirderClient(apiUrl=GIRDER_API_URL)

def make_set_page(set_info, set_dict, set_physics, set_acks):
    set_physics_dict = OrderedDict([(k, (set_dict[k].name, set_dict[k].filenos)) 
                                    for k in set_physics])
    if not os.path.exists('source/%s' % set_info['name']):
        os.mkdir('source/%s' % set_info['name'])
    for sim, sim_info in set_dict.items():
        totsize = make_epoch_pages(set_info['name'], set_info['filespec'], sim, sim_info.name,
                                   sim_info.filenos, sim_info.sname_map, sim_info.lname_map,
                                   sim_info.unit_map, set_info["cadence"], sim_info.proj_axes,
                                   set_physics_dict)
        make_sim_page(set_info['name'], set_info["filespec"], sim, sim_info.name,
                      sim_info.filenos, sim_info.sname_map, sim_info.lname_map,
                      set_info["cadence"], sim_info.proj_axes, totsize)
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
               'cosmo_warning': set_info['cosmo_warning'],
               'redshift': set_info['redshift'],
               'acks': set_acks}
    template_file = 'templates/set_template.rst'
    make_template('source/%s/index.rst' % set_info["name"], template_file, context)

def make_sim_page(set_name, filespec, sim, sim_name, filenos, sname_map,
                  lname_map, cadence, proj_axes, totsize):
    sim_dir = 'source/%s/%s' % (set_name, sim)
    outfile = sim_dir+"/index.rst"
    if not os.path.exists(outfile):
        pbar = get_pbar("Setting up simulation page for "+sim, len(filenos))
        epochs = OrderedDict()
        imgs = OrderedDict()
        for fileno in filenos:
            pngs = {}
            for ax in proj_axes:
                pngs[ax] = {}
                for fd, field in sname_map["proj"].items():
                    filename = filespec % (sim, fileno) + "_proj_%s_%s" % (ax, field)
                    pngs[ax][fd] = get_file(filename, "proj")
            epochs[fileno] = "t = %4.2f Gyr" % (float(fileno)*cadence)
            imgs[fileno] = pngs
            pbar.update()
        pbar.finish()
        simfd = get_folder('/'.join([set_name, sim]))
        sim_dl = "https://girder.hub.yt/api/v1/folder/%s/download" % simfd["_id"]
        num_epochs = len(epochs.keys())
        context = {'sim_name': sim_name,
                   'sim_dl': sim_dl,
                   'size': "%.2f" % totsize,
                   'proj_axes': proj_axes,
                   'epochs': epochs,
                   'imgs': imgs,
                   'num_epochs': num_epochs-1,
                   'filenos': filenos,
                   'names': lname_map["proj"]}
        template_file = 'templates/sim_template.rst'
        make_template(outfile, template_file, context)

def make_template(outfile, template_file, context):
    template = open(template_file).read()
    template = re.sub(r' %}\n', ' %}', template)
    template = jinja2.Template(template)
    open(outfile, 'w').write(template.render(**context))

def make_epoch_pages(set_name, filespec, sim, sim_name, filenos, sname_map,
                     lname_map, unit_map, cadence, proj_axes, set_physics):
    totsize = 0.0 
    sim_dir = 'source/%s/%s' % (set_name, sim)
    if not os.path.exists(sim_dir):
        os.mkdir(sim_dir)
    pbar = get_pbar("Setting up epoch pages for simulation "+sim, len(filenos))
    num_epochs = len(filenos)
    for noi, fileno in enumerate(filenos):
        outfile = "source/%s/%s/%s.rst" % (set_name, sim, fileno)
        setp = OrderedDict([(sim, val[0]) for sim, val in set_physics.items() 
                           if fileno in val[-1]])
        if not os.path.exists(outfile):
            data = {}
            for itype in sname_map.keys():
                data[itype] = OrderedDict()
                for ax in proj_axes:
                    if itype == "slice" and ax != "z":
                        continue
                    data[itype][ax] = {}
                    if itype == "galaxies":
                        filename = "_".join([set_name, sim, fileno]) + "_%s_%s" % (itype, ax)
                    else:
                        filename = filespec % (sim, fileno) + "_%s_%s" % (itype, ax)
                    data[itype][ax]['fits'] = get_file(filename, itype)
                    if itype == "galaxies":
                        gal_files = get_file(filename, itype)
                        data[itype][ax]['reg'] = gal_files['reg']
                        data[itype][ax]['fits'] = gal_files['fits']
                    else:
                        data[itype][ax]['fits'] = get_file(filename, itype)
                    imgs = {}
                    for link, field in sname_map[itype].items():
                        imgfn = filename+"_"+field
                        imgs[link] = get_file(imgfn, itype)
                    data[itype][ax]['pngs'] = imgs
            template_file = 'templates/epoch_template.rst'
            timestr = "t = %4.2f Gyr" % (float(fileno)*cadence)
            if noi == 0:
                prev_link = ""
                dis_prev = "disabled"
            else:
                prev_link = "%s.html" % filenos[noi-1]
                dis_prev = ""
            if noi == num_epochs-1:
                next_link = ""
                dis_next =  "disabled"
            else:
                next_link = "%s.html" % filenos[noi+1]
                dis_next = ""
            epochfd = get_folder('/'.join([set_name, sim, fileno]))
            epoch_dl = "https://girder.hub.yt/api/v1/folder/%s/download" % epochfd["_id"]
            size = epochfd["size"]/(1024.*1024.*1024.)
            totsize += size
            hub_folder = "https://girder.hub.yt/#collection/57c866a07f2483000181aefa/folder/"+epochfd["_id"]
            context = {"data": data,
                       "sim": sim,
                       "epoch_dl": epoch_dl,
                       "size": "%.2f" % size, 
                       "fileno": fileno,
                       "sim_name": sim_name,
                       "timestr": timestr,
                       "slice_names": lname_map["slice"],
                       "proj_names": lname_map["proj"],
                       "sz_names": lname_map["SZ"],
                       "slice_fields": unit_map["slice"],
                       "proj_fields": unit_map["proj"],
                       "sz_fields": unit_map["SZ"],
                       "galaxies": "galaxies" in sname_map.keys(),
                       "prev_link": prev_link,
                       "next_link": next_link,
                       "dis_prev": dis_prev,
                       "dis_next": dis_next,
                       "hub_folder": hub_folder, 
                       "set_physics": setp if sim in setp else {}}
            make_template(outfile, template_file, context)
        pbar.update()
    pbar.finish()
    return totsize

def get_file(filename, itype):
    items = gc.get("resource/search", {"q": '"'+filename+'"', "types": '["item"]'})['item']
    if len(items) == 0:
        return "https://girder.hub.yt/static/built/plugins/ythub/extra/img/yt_logo.png"
    elif itype == "galaxies" and len(items) >= 2:
        gals = {}
        for item in items:
            if "fits" in item['name']:
                gals["fits"] = "https://girder.hub.yt/api/v1/item/%s/download" % item['_id']
            elif "reg" in item['name']:
                gals["reg"] = "https://girder.hub.yt/api/v1/item/%s/download" % item['_id']
        return gals
    else:
        return "https://girder.hub.yt/api/v1/item/%s/download" % items[0]['_id']

def get_folder(folder):
    folder_path = os.path.join('/collection', 'cluster_mergers', folder)
    folder = gc.get("resource/lookup", {"path": folder_path})
    return folder

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action='store_true')
    args = parser.parse_args()
    make_set_page(fid_info, fid_dict, fid_physics, fid_acks)
    make_set_page(slosh_info, slosh_dict, slosh_physics, slosh_acks)
    make_set_page(virgo_info, virgo_dict, virgo_physics, virgo_acks)
    make_set_page(mag_info, mag_dict, mag_physics, mag_acks)
