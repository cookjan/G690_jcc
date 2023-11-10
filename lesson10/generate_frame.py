
# import libraries
import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd
import cartopy
import cmocean
import os

# set the path to the input data file
input_file = "/N/project/obrienta_startup/datasets/ERA5/ds633.0/e5.oper.an.sfc/202106/e5.oper.an.sfc.128_136_tcw.ll025sc.2021060100_2021063023.nc"

# set the directory where we'll save the images
output_dir = "./animation_frames"

# set the timestep to plot
i = 0

# make sure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# load the data file
ds_in = xr.open_dataset(input_file, chunks = -1)

""" Make a function to plot and save the data at a given timestep. """

def generate_frame(
        i : int,
        input_file = "/N/project/obrienta_startup/datasets/ERA5/ds633.0/e5.oper.an.sfc/202106/e5.oper.an.sfc.128_136_tcw.ll025sc.2021060100_2021063023.nc",
        output_dir = "./animation_frames/"):

        # prevent matplotlib from displaying the plot
        plt.ioff()
        
        # get the variable at the requested timestep
        time1 = ds_in["TCW"].isel(time=i) #needed help

        #set coords of bloomington IN
        bloomington_lon = -86.526386
        bloomington_lat = 39.165325
        projection = cartopy.crs.Orthographic(central_longitude=bloomington_lon, central_latitude=bloomington_lat)
        transform = cartopy.crs.PlateCarree()#others - mercator?

        # plot the data
        #create a fig
        fig, ax = plt.subplots(subplot_kw= dict(projection = projection))

        #draw on the data
        tcw = time1 #time1.isel(time = i) #(season = 'DJF')
        tcw_dimensions = ds_in['TCW'].squeeze()
        lat = tcw_dimensions.latitude
        lon = tcw_dimensions.longitude
        cplt = ax.pcolormesh(lon, lat, tcw,\
              transform = transform, \
              cmap = cmocean.cm.rain, \
            )
              #cbar_kwargs = dict(label = f'Precipitable Water [mm]'))

        fig.colorbar(cplt, ax = ax, label = "Precipitable Water [mm]")
                #NOTE: this is in place of a legend on a gradient graph or map, cant remember which

        #drwa continent boundary
        ax.coastlines()

        #plot a point VERY ROUGHLY corresponding to bloomington IN
        ax.plot(bloomington_lon, bloomington_lat, 'r*', transform = transform)

        #set a glbal extent
        ax.set_global()

        # get the time of the timestep
        time = tcw.time.values
        # convert it to a datetime object
        time = pd.to_datetime(time)

        # add a title with a nicely formatted date
        ax.set_title("Plot at " + time.strftime("%Y-%m-%d %H:%M UTC"))

        # save the plot
        output_file = os.path.join(output_dir, f"tcw_{i:05d}.png")
        fig.savefig(output_file, dpi=300, bbox_inches="tight")

        # close the figure
        plt.close(fig)

        return output_file

generate_frame(i)