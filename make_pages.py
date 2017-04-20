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
from six import string_types

GIRDER_API_URL = "https://girder.hub.yt/api/v1"

gc = girder_client.GirderClient(apiUrl=GIRDER_API_URL)

def make_set_page(set_info, set_dict, set_physics, set_acks):
    set_physics_dict = OrderedDict([(k, (set_dict[k].name, set_dict[k].filenos)) 
                                    for k in set_physics])
    set_path = os.path.join('source', set_info['name'])
    if not os.path.exists(set_path):
        os.mkdir(set_path)
    for sim, sim_info in set_dict.items():
        totsize = make_epoch_pages(set_info['name'], set_info['filespec'], sim, sim_info.name,
                                   sim_info.filenos, sim_info.sname_map, sim_info.lname_map,
                                   sim_info.unit_map, set_info["cadence"], sim_info.proj_axes,
                                   sim_info.slice_axes, set_physics_dict, sim_info.cat_type,
                                   sim_info.halo_info)
        make_sim_page(set_info['name'], set_info["filespec"], sim, sim_info.name,
                      sim_info.filenos, sim_info.sname_map, sim_info.lname_map,
                      set_info["cadence"], sim_info.proj_axes, sim_info.cat_type, totsize)
    sim_pages = []
    for key in set_dict:
        if isinstance(key, tuple):
            sim_pages.append('_'.join(key))
        else:
            sim_pages.append(key)
    context = {'name': set_info["name"],
               'sim_pages': sim_pages,
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
               'cosmo': sim_info.cosmo,
               'redshift': set_info['redshift'],
               'acks': set_acks}
    template_file = 'templates/set_template.rst'
    make_template('source/%s/index.rst' % set_info["name"], template_file, context)

def make_sim_page(set_name, filespec, sim, sim_name, filenos, sname_map,
                  lname_map, cadence, proj_axes, cat_type, totsize):
    if isinstance(sim, tuple):
        sim_path = list(sim)
        sim = sim[-1]
    else:
        sim_path = [sim]
    sim_dir = os.path.join('source', set_name, '_'.join(sim_path))
    outfile = sim_dir+"/index.rst"
    if not os.path.exists(outfile):
        pbar = get_pbar("Setting up simulation page for %s" % (sim_path,), len(filenos))
        files = OrderedDict()
        imgs = OrderedDict()
        for fileno in filenos:
            pngs = {}
            for ax in proj_axes:
                pngs[ax] = {}
                for fd, field in sname_map["proj"].items():
                    filename = filespec % (sim, fileno) + "_proj_%s_%s" % (ax, field)
                    pngs[ax][fd] = get_file(filename, "proj")
            if cat_type == "epoch":
                files[fileno] = "t = %4.2f Gyr" % (float(fileno)*cadence)
            elif cat_type == "halo":
                files[fileno] = "Halo ID %d" % (int(fileno))
            imgs[fileno] = pngs
            pbar.update()
        pbar.finish()
        simfd = get_folder('/'.join([set_name, *sim_path]))
        sim_dl = "https://girder.hub.yt/api/v1/folder/%s/download" % simfd["_id"]
        num_fids = len(files.keys())
        context = {'sim_name': sim_name,
                   'sim_dl': sim_dl,
                   'size': "%.2f" % totsize,
                   'proj_axes': proj_axes,
                   'cat_type': "epoch" if cat_type == "epoch" else "halo",
                   'files': files,
                   'imgs': imgs,
                   'num_fids': num_fids-1,
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
                     lname_map, unit_map, cadence, proj_axes, slice_axes,
                     set_physics, cat_type, halo_info):
    totsize = 0.0
    pbar = get_pbar("Setting up epoch pages for simulation %s " % (sim,), len(filenos))
    if isinstance(sim, tuple):
        sim_path = list(sim)
        sim = sim[-1]
    else:
        sim_path = [sim]
    sim_dir = os.path.join('source', set_name, '_'.join(sim_path))
    if not os.path.exists(sim_dir):
        os.mkdir(sim_dir)
    num_epochs = len(filenos)
    for noi, fileno in enumerate(filenos):
        outfile = os.path.join('source', set_name, '_'.join(sim_path), "%s.rst" % fileno)
        setp = OrderedDict([(sim, val[0]) for sim, val in set_physics.items() 
                           if fileno in val[-1]])
        if not os.path.exists(outfile):
            data = {}
            for itype in sname_map.keys():
                data[itype] = OrderedDict()
                for ax in proj_axes:
                    if itype == "slice" and ax not in slice_axes:
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
            if cat_type == "epoch":
                filestr = "t = %4.2f Gyr" % (float(fileno)*cadence)
            elif cat_type == "halo":
                filestr = "Halo ID %d" % (int(fileno))
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
            epochfd = get_folder('/'.join([set_name, *sim_path, fileno]))
            epoch_dl = "https://girder.hub.yt/api/v1/folder/%s/download" % epochfd["_id"]
            size = epochfd["size"]/(1024.*1024.*1024.)
            totsize += size
            hub_folder = "https://girder.hub.yt/#collection/57c866a07f2483000181aefa/folder/"+epochfd["_id"]
            if halo_info is not None:
                hinfo = halo_info[noi]
            else:
                hinfo = None
            context = {"data": data,
                       "sim": sim,
                       "epoch_dl": epoch_dl,
                       "size": "%.2f" % size, 
                       "fileno": fileno,
                       "sim_name": sim_name,
                       "filestr": filestr,
                       "slice_axes": len(slice_axes) > 1,
                       "slice_names": lname_map["slice"],
                       "proj_names": lname_map["proj"],
                       "sz_names": lname_map.get("SZ", []),
                       "slice_fields": unit_map["slice"],
                       "proj_fields": unit_map["proj"],
                       "sz_fields": unit_map.get("SZ", []),
                       "xray_events": "cxo_evt" in lname_map,
                       "galaxies": "galaxies" in sname_map.keys(),
                       "prev_link": prev_link,
                       "next_link": next_link,
                       "dis_prev": dis_prev,
                       "dis_next": dis_next,
                       "hub_folder": hub_folder,
                       "hinfo": hinfo, 
                       "cat_type": "epoch" if cat_type == "epoch" else "halo",
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
    make_set_page(omega_info, omega_dict, omega_physics, omega_acks)
