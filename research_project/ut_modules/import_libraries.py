#import libraries

#analytical 
import numpy as np
import scipy
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt


#mapping
import shapely #is this just a map thing?
import cartopy #see 06_workalong02
import geopandas as gpd
import pykml #attempted for geologic formations section of G690 final project
import utm
import shapefile

#display an image
from IPython.display import Image, display

#for better colormaps
import cmocean #see 06_workalong01

#??
import numpy.fft as fft #see 11_workalong_01
import os #keep from redownloading a file. see 05_multid

#machine learning
import torch
import torch.nn as nn

#parallel code
from mpi4py import MPI # see 09_workalong_01

import sklearn #scikit-learn
from sklearn import preprocessing as pr

import scipy.special #see 03_warmup