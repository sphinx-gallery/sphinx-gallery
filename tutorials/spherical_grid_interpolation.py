
# -*- coding: utf-8 -*-
"""

Spherical Grid Conversion
=========================

* **ACTM Performer:** AIBEDO Team (PARC, UVic and UW);
* **Author:** Haruki Hirasawa (hhirasawa@uvic.ca) 

We use ``pygsp`` package to interpolate 2D-gridded data into a spherical grid format. This is done in two steps:

**Step 1:** Generate a text file ("skeleton") with the desired Icosahedral level using our python script 
link `here <https://github.com/kramea/aibedo/blob/preprocess_MS3/preprocessing/gen_icosph_gridfile.py>`_. 

This code block generates a text file that will be used to generate the spherical sample for level 6. 
To generate a text file for another grid level, please change the ``sphlevel`` in the code. 

**Step 2:** Once the text file is generated in step 1, we use the ``cdo`` (Climate Data Operator) 
command line tool to generate the interpolated ``netCDF`` file. 
Please see `here <https://www.isimip.org/protocol/preparing-simulation-files/cdo-help/>`_ for instructions to download ``cdo``. 

The following script is given in command line to generate the interpolated file for model training:

``cdo remapbil,icosphere_6.txt in.nc out.nc``

Here, ``in.nc`` is the 2D-gridded file from ESM model ensembles or Reanalysis datasets, and ``out.nc`` is 
the name of the interpolated file that will be used for model training.

"""


import pygsp as pg
import numpy as np
### Generates a text file with centre points of a icosahedral sphere grid
### Formatted to pass as an argument for 'cdo remap,GRIDFILE in.nc out.nc'
def xyz2lonlat(x:float,y:float,zLfloat, radius=6371.0e6):
    """From cartesian geocentric coordinates to 2D geographic coordinates."""
    """ lon: [-180, 180], lat:[-90, 90] """
    latitude = np.arcsin(z / radius)/np.pi*180
    longitude = np.arctan2(y, x)/np.pi*180
    return longitude, latitude 
def gen_icosphere(level:int,radius:float = 6371.0e6):
    '''
    Generates points on a icosphere grid (from Soo Kim)
    level (int): iteration level
    radius (float): radius of the earth
    '''
    #(1) generate graph of SphereIcosahedral
    graph = pg.graphs.SphereIcosahedral(2**level)
    #(2) extract lon, lat coordinate
    vertices = graph.coords # xyz coordinates
    #print("number of vertices for level "+str(level)+" (2**"+str(level)+")is "+str(graph.n_vertices))
    lon = []
    lat = []
    radius = 1
    # convert cartesian points to spherical lon/lat
    for tmp_xyz in vertices:
        tmp_lon, tmp_lat = xyz2lonlat(tmp_xyz[0],tmp_xyz[1],tmp_xyz[2], radius=radius)
        lon.append(tmp_lon)
        lat.append(tmp_lat)
    return lon, lat
sphlevel = 6
lon,lat = gen_icosphere(sphlevel,radius = 6371.0e6)
f = open("isosphere_{0}.txt".format(sphlevel), "a")
# write grid to file
f.write("gridtype = unstructured\n")
f.write("gridsize = {0}\n".format(len(lon)))
f.write("# Longitudes\n")
f.write("xvals = " + ' '.join(map(str, lon))+"\n")
f.write("# Latitudes\n")
f.write("yvals = " + ' '.join(map(str, lat))+"\n")

