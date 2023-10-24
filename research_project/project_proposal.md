# Final Project: 

aspects:
create your own functions
read/write data
Machine learning
publication-quality plot (multiple types of info)

## Background
Natural groundwater geochemistry is influenced by groundwater path. The longer groundwater is in contact with a certian rock, the more the chemistry of the groundwater will change through rock-water interactions. The new chemistry will reflect the ions located in the rock or soil in both constiutent and concentration. Concentration of groundwater geochemistry is also affected by the amount of water coming into the system, generally in the form of rainfall replenishment, which will affect system retention time.

Natural water contamination from inorganic contaminants is a product of groundwater path. The concentration of the contaminant determines how harmful groundwater is for consumption, and some common contaminants such as fluoride or arsenic become global problems due to how easily they reach hazardous concentrations. Geochemical modeling can show dissolution rates of rock ions into groundwater when accounting for factors such as rock ion constituents, ionic charge, reaction surface area, and field variable parameters such as pH and temperature. Because of this, geochemical modeling shows promise to be an important tool in predicting groundwater geochemistry.  

As groundwater geochemistry is affected by system inputs, climate change will certianly affect groundwater geochemistry through surface water pattern changes in rainfall, evaporation, and temperature, among other factors. Previously, members of the Zhu lab at IUB created high-performance computing hydrology models of various hydrology parameters (Precipitation, Evapotranspiration, Soil water content, Groundwater Recharge, Baseflow, Streamflow, and Water Yield) under emission scenarios RCP 4.5 and RCP 8.5 into the 2020s, 2050s and 2080s. Lab members posted these models interactively to the website "Future Water Indiana: Visualizing climate change impacts on the hydrology of the Wabash Basin". The data from these models may yet have unmeasured application to regional groundwater geochemistry.



## Overview
I propose to create importable geochemical reaction modules within Python.
I will complete a correlation analysis of Indiana geologic formations to historical groundwater geochemical data.
I will then incorporate climate emissions scenarios of groundwater recharge to predict future contaminant concentrations. 
I will then create an app for graph and map generation of contaminant model predictions by year and location within Indiana.

### 1) Build geochemical reaction function modules in python

    Classes: mineral, ion
    Atrributes: Elements, charge, 

    Functions: 
Use machine learning to model unstudied minerals or reactions
    General net dissolution rate and pH-based dissolution rates can be found at Zhang et al., 2019.

However, geochemical databases and models are not complete due to the difficulty in producing the high-quality data required for model creation.
    For example, arsenic wasn't included until ...


### 2) Application to State of Indiana (Wabash Basin)
This correlation analysis will include data from Indiana geologic formations to historical groundwater geochemical data.
    Historical hydrology: 
    The FutureWater website allows for download of historical data for streamflow, baseflow, recharge, precipitation, etc. categorized by HUC12 subbasin in the Wabash Basin. 

    Historical geochemistry:
    Ambient groundwater data of Indiana water-management basins, including nitrate, phosphate, sulfate, metals such as iron, sodium, and potassium, and potentially toxic constituents such as fluoride. Field parameters important to geochemical modeling such as pH and temperature are collected. Each entry has an attributed depth and UTM Coordinates. 

    Indiana rock composition:
    Using geologic map of Indiana, correlation analysis done of aqueous ion type to formation type
    Correlation analysis of aqueous ion concentration and type to formation and historical water data
    Use parallel processing to write code to estimate 

### 3) Predictive analysis  
    CO2 emission predictor data 
    subbasin historical hydro data
    detailed geologic map/core data?
    detailed water chemistry geospatial data?

    Caveat: Groundwater geochemistry depends on how long groundwater has been underground before being drawn. Length of time groundwater is in a system varies heavily, between days and hundreds of years. For this reason, there may be an observed 'lag' in geochemical variability caused by amount of groundwater entering a system. This lag would likely vary by location, and therefore be difficult to account for in the present analysis. 


### 4) App creation
The intended method for app creation is plot.ly.
Website user input would include location (by address). User would pick from predetermined options for the following factors: time, CO<sub>2</sub> emmision scenario, and contaminant of interest. User would choose between map or graph outputs. 
Website output would include a map of a contaminant concentration at a specified time and emission scenario, or a graph of a contaminant concentration varying by time at a location.

## Timeline
- [x] (Oct 27) write code to read in seismometer data files
- [ ] (Nov 3) write and test function `extract_earthquakes()` to extract individual earthquakes from data
- [ ] (Nov 10) write and test function `estimate_magnitude()` to estimate the magnitude of each earthquake
- [ ] (Nov 17) write code to run magnitude estimation in paralell on multiple seismometer data files
- [ ] (Nov 24) write code to run magnitude estimation in paralell on multiple seismometer data files
- [ ] (Dec 1) write code to run magnitude estimation in paralell on multiple seismometer data files

## Sketch


## Data Sources
[BASIC Scripts library for PHREEQC](http://149.165.154.118/basic_scripts/basic_scripts.php) ; [Github] (https://github.com/HydrogeoIU/PHREEQC-Kinetic-Library): Data library for geochemical modeling of reaction rates. 
Alternatively, the [rates calculator](https://hydrogeochem.earth.indiana.edu/software/index.html) may be used if geochemical modeling fails. 

[Downscaled CMIP5 Climate Change Scenarios for the State of Indiana](https://www.crc.nd.edu/~kbyun/CMIP5_IN_CCIA.html): State of Indiana climate change scenario data. Provides daily precipitation, max and min temperature, and wind speed at 1/16 degree resolution under 3 RCP emissions scenarios using 10 models. 

[State of Indiana subbasin shapefile](https://figshare.com/articles/dataset/Wabash_River_Basin_USGS_NHD_HUC_12_polygon_shapefile/8398394): HUC12 subbasins in Indiana to be used in geochemical interpolation.

[Future Water Historical Data](https://analysis.futurewater.indiana.edu/?_gl=1*1nsy30f*_ga*MjA2OTI3MjMyMy4xNjkyNTkxMjc5*_ga_61CH0D2DQW*MTY5ODA3MTE4MS4yNC4xLjE2OTgwNzIxMTUuNjAuMC4w): Historical Hydrology data of Wabash Basin. Includes historical data for streamflow, baseflow, recharge, precipitation, etc. by HUC12 subbasin in Indiana. 

[Ambient Ground Water Chemistry](https://www.in.gov/dnr/water/publications/ambient-ground-water-chemistry/ ): DNR historical groundwater chemistry data. Ambient water chemistry of 6 water-management basins in Indiana.

[Indiana Geologic Formation Data](https://mrdata.usgs.gov/geology/state/state.php?state=IN):
GIS database of geologic units and structures in Indiana contained within a .kml file.

Citation:
Gray, Henry H., Ault, Curtis, H., and Keller, Stanley, J., 1987, Bedrock geologic map of Indiana: Dept. of Natural Resources, Indiana Geological Survey, Miscellaneous Map 48, scale = 1:500,000
[BEDROCK_GEOL_MM48_IN: Bedrock Geology of Indiana (Indiana Geological Survey, 1:500,000, Polygon Shapefile)] which can be found at http://igs.indiana.edu/arcims/statewide/download.html

## References


Zhang, Y., Hu, B., Teng, Y., Tu, K., & Zhu, C. (2019). A library of BASIC scripts of reaction rates for geochemical modeling using phreeqc. Computers & Geosciences, 133, 104316. 