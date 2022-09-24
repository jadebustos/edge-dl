# Violence detector application in standalone mode

To use the application in standalone mode you will have to install both the application and its dependencies.

## Requirements

The following directories must be created:

* */opt/violence-detector*, root directory for all data needed/producted.
* */opt/violence-detector/input*, when videos are used to detect violent situations will be readed from this directory.
* */opt/violence-detector/output*, predictions will be stored in this directory.
* */opt/violence-detector/models*, deep learning models and weights will be stored in this directory.

It is recommended using [python virtual environments](virtual-environment.md). The following configuration was tested:

* *python*, version 3.7 was used.
* *numpy*, 1.19.5 version was used.
* *opencv-python*, 4.6.0.66 version was used.
* *tensorflow*, 2.5.3 version was used.

Images will be resized to 200x200 to feed the deep learning models. If you use your own models you will need to modify **IMAGE_WIDTH** and **IMAGE_HEIGHT** variables in [myvars.py](myvars.py) to fit your input shape.

By default one of each five images will be choosen to make a prediction. If you want to modify that you need to change the **FRAMES_STEP** variable in [myvars.py](myvars.py) accordingly.

## Running the violence-detector application for video files processing

Activate the python virtual environment and run:

```bash
jadebustos@reypastor:~$ source ~/pyenvs/tfm-tf/bin/activate
(tfm-tf) jadebustos@reypastor:~$ cd tfm
(tfm-tf) jadebustos@reypastor:tfm$ python3 violence-detector.py --input directory --model xception \
                                                --weights xception.h5 --graphical
(tfm-tf) jadebustos@reypastor:tfm$
```

Where:

* **--input directory** tells the application that must read videos from */opt/violence-detector/input*. Before running the application copy in this directory the videos you want to analyze.
* **--model xception** tells the application where the deep learning model is. The model will be loaded from */opt/violence-detector/models*. To see how to export the model check [exporting-models.md](exporting-models.md). In this case **xception** will be the directory name where the model was exported. 
* **--weights xception.h5** tells the application where the trained weights are. The weights will be loaded from */opt/violence-detector/models*.
* **--graphical** tels the application that graphical mode is available and a window will be openned to see the images and the prediction. To quit press *q*. This argument is optional. 

Preditions will be saved within directory */opt/violence-detector/output*. Images will be stored together with the prediction and a csv file will be created with all the information as well.

## Running the violence-detector application for webcam images processing

Activate the python virtual environment and run:

```bash
jadebustos@reypastor:~$ source ~/pyenvs/tfm-tf/bin/activate
(tfm-tf) jadebustos@reypastor:~$ cd tfm
(tfm-tf) jadebustos@reypastor:tfm$ python3 violence-detector.py --input webcam --model xception \
                                                --weights xception.h5 --device 1 --graphical \
                                                --width 800 --height 600
(tfm-tf) jadebustos@reypastor:tfm$
```

Where:

* **--input directory** tells the application that must read videos from */opt/violence-detector/input*. Before running the application copy in this directory the videos you want to analyze.
* **--model xception** tells the application where the deep learning model is. The model will be loaded from */opt/violence-detector/models*. To see how to export the model check [exporting-models.md](exporting-models.md). In this case **xception** will be the directory name where the model was exported.
* **--weights xception.h5** tells the application where the trained weights are. The weights will be loaded from */opt/violence-detector/models*. 
* **--device 1** tells the application the video device to use is **/dev/video1**. To see how to get the video devices check [video-devices.md](video-devices.md). 
* **--graphical** tells the application that graphical mode is available and a window will be openned to see the images and the prediction. To quit press *q*. This argument is optional. 
* **--width 800** tells the application the width component for the webcam resolution. By default 1280 is used.This argument is optional.
* **--height 600** tells the application the height component for the webcam resolution. By default 720 is used.This argument is optional.

Predictions will be saved within directory */opt/violence-detector/output*. Images will be stored together with the prediction and a csv file will be created with all the information as well.