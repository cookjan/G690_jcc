
# Final Project: 

## Groundwater Geochemistry in a Subset of Indiana

This project consists of a number of analyses contained in the Jupyter notebooks below:
1. IDNR_GW
2. HFK-database
3. IN_geological-formations
4. research_wateruse_03

The folder also contains several subfolders:
- data
- HFKplots
- IDNR_GWchem
- images
- ut_modules

Besides these, there is one markdown file containing the project proposal (```project_proposal.md```). These files/folders and their contents are explained below.

## Notebooks

#### 1. IDNR_GW

This notebook looks at a historical groundwater chemistry dataset of six groundwater basins in Indiana, published by the Indiana DNR, and completes an interpolation analysis of groundwater hardness in the dataset. This was the most successful analysis of the project.

#### 2. HFK-database

This analysis was completed as part of the machine learning unit in class (lesson 7). It examines the geochemical mineral database “SUPCRTBL” created by researchers at IUB. It attempted an reLU correlation of geochemical variables within the dataset, but the model produced obvious errors. 

This analysis produced numerous graphs available for view in the folder **HKFplots**.

#### 3. IN_geological-formations

This analysis used the IDNR groundwater chemistry dataset as before and attempted to correlate points in that dataset with a map of geologic formations in Indiana. This analysis failed due to inability to parse the geologic formation datafiles required. These files can be found:
> research_project\data\ingeol.kml
> research_project\data\WBHUC12shp\Wabash_HUC12.shp 

#### 4. research_wateruse_03
This was a correlation analysis of a dataset published by USGS of US county-level water use in 2015. This analysis was completed as an assignment in conjunction with lesson 3.

## Folders

#### data

This eponymous folder contains the majority of data involved in the analyses described above, with the exception of the IDNR_GW datafiles contained in a separate folder. Citations for the data can be found in the file ```project_proposal.md``` and the notebooks in which the data in question are used. 

#### HFKplots

This folder was created as part of the ```HFK-database``` analysis and contains scatterplots of the geochemical variables listed in the SUPCRTBL database. 

#### IDNR_GWchem

This folder contains data, shapefiles, and metadata associated with the IDNR groundwater chemistry dataset.

#### images

This folder contains images displayed in other files, such as the draft figure from the project proposal.

#### ut_modules

This folder contains utility modules designed to be imported into analyses. Sources are imbedded where appropriate. 

