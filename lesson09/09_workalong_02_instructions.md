# Exercise 02 - Animating the weather in parallel

In this exercise, we will develop code to generate an animation, taking advantage of parallelization to make the process fast.

https://github.com/taobrienlbl/advanced_earth_science_data_analysis/assets/8796694/7c701d6a-895d-4707-87c8-0d59066ce469

## 2.1 Developing plot code

In a jupyter notebook, we'll develop code to generate a nice plot of total atmospheric water (*precipitable water* is the technical term), which is a good way to look at [atmospheric rivers](https://www.noaa.gov/stories/what-are-atmospheric-rivers).

Download [this file](https://github.com/taobrienlbl/advanced_earth_science_data_analysis/blob/spring_2023_iub/lessons/09_parallelization_intro/09_workalong_02.1.ipynb) to your lesson09 folder on BigRed200 and follow along.

## 2.2 Testing plot code

Make a module for your plotting code called `generate_frame.py`; put your function in that file (and any necessary imports).

Test your function from the command line by typing the following in the terminal:
```bash
conda activate easg690
cd lessons/09_parallelization_intro/
python3 -c 'import generate_frame; generate_frame.generate_frame(11)'
```

It might not work the first time.  If not, look at the error messages and try to understand what is not working; update `generate_frame.py` until the testing process results in the creation of the expected image file (in this case `animation_frames/tcw_00011.png`) without errors.

## 2.3 Parallelize the plot code

Now we can use `mpi4py` to generate animation frames in parallel! Do the following:

1. Make a new script called `parallel_generate_frames.py`
1. import both `mpi4py` and `generate_frame` in your script
1. use the MPI rank to set which frame to plot
1. use `generate_frame.generate_frame()` to generate the requested frame
1. use `salloc` to get an allocation for one node and 20 processors
1. use `srun` to run `parallel_generate_frames.py` on 20 processors

## 2.4 Make an mp4

Now we'll use `ffmpeg` to generate an animation.  We'll first need to install the `ffmpeg` and `openh264` libraries in conda; run `mamba install -c conda-forge ffmpeg openh264 --yes` in your terminal (make sure your `easg690` environment is active when you do.)

Run the following command from your animation directory (e.g., do `cd animation_frames` first):

```bash
ffmpeg -framerate 10 -i tcw_%05d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p tcw_animation.mp4
```

Note that my animation frame filenames have five digits in the frame number, hence the `-i tcw_%05d.png` argument.  If yours has fewer, like two digits, you'll need to modify, e.g.,: `-i tcw_%02d.png`

## 2.5 Going beyond

How could you modify `parallel_generate_frames.py` to generate 100 frames while still only using 10 processors? 

How could you modify `parallel_generate_frames.py` to generate N frames using M processors?
