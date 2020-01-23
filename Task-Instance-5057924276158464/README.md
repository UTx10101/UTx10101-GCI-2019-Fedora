# Color Detection Program in Python
This program uses OpenCV and a Supervised Machine Learning Algorithm: K-NearestNeighbours

## Steps to Setup:
1. `pip install -r requirement.txt`  - This will install both the dependencies OpenCV and Numpy.
2. `python DetectorMain.py`

## How to Use:
1. After following above steps you will be asked whether you want to train the script.
2. To train the script you can either add more images to respective color folders in `trainingSet/` or add your own color folders.
3. Now to train the script just start the `DetectorMain.py` and type `Y` or `y` on prompt to train.
5. After the training a `.csv` file will be generated in `colorDetectionProg/` now our script can use this as info instead of training on each run.
6. Now you will be asked for image path or name there are some sample images in `Demo_Images/` to test (try them or enter your own image).
7. Then script will show you the colors present in the image.
8. Also you can preview the image by answering `Y` or `y` to next prompt.

## Screenshots:
### Terminal:-
![Terminal](https://github.com/UTx10101/UTx10101-GCI-2019-Fedora/blob/master/Task-Instance-5057924276158464/screenshot_Terminal.png)
### ImagePreviev:- (As my screen is small the image couldn't be displayed accurately)
![ImagePreview](https://github.com/UTx10101/UTx10101-GCI-2019-Fedora/blob/master/Task-Instance-5057924276158464/screenshot_ImagePreview.png)

### This app was created by UTx10101 to Complete a GCI-2019 task by Fedora : [Here](https://codein.withgoogle.com/dashboard/task-instances/5057924276158464/)
