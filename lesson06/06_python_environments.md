# Python Environments

We'll use the following steps to create a new `conda` environment.

1. Open anaconda prompt (or your terminal on a mac operating system)
1. Create a new conda environment: `conda create --yes -n easg690 python=3.10`
1. Activate the new environmenta: `conda activate easg690`
1. Install [`mamba`](https://github.com/mamba-org/mamba): `conda install --yes -c conda-forge mamba`
1. Download this [requirements.yml](https://raw.githubusercontent.com/taobrienlbl/advanced_earth_science_data_analysis/spring_2023_iub/lessons/06_advanced_plotting/requirements.yml) file
1. Verify that `requirements.yml` has all the packages you think you'll need; add others as needed
1. Install the packages into the environment: `mamba env update -f requirements.yml`
1. Install the jupyter kernel into the environment: `ipython kernel install --name easg690 --user`
1. Open the *Advanced Plotting* notebook we just completed; change the environment in vscode to `easg690`
1. Verify that you can re-run your notebook with this environment