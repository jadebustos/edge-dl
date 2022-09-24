# Violence Detector application

This application can be used to detect violent situations on videos or using a webcam. As this software has created for my Master Thesis it is not intended to be an Enterprise application, thus many things can be improved.

This application has been developed to be executed as a container image. For this reason some parameters are hardcoded into the code.

This applicantion can be used in two ways:

* To process video files.
* To process images from a webcam.

This application is intended to test models so it uses tensorflow instead of OpenVINO. So, you can try it although you do not have a Myriad device.

## Requirements

The following directories must be created:

* */opt/violence-detector*, root directory for all data needed/producted.
* */opt/violence-detector/input*, when videos are used to detect violent situations will be readed from this directory.
* */opt/violence-detector/output*, predictions will be stored in this directory.
* */opt/violence-detector/models*, deep learning models will be stored in this directory.

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
(tfm-tf) jadebustos@reypastor:tfm$ python3 violence-detector --input directory --model xception ---graphical
(tfm-tf) jadebustos@reypastor:tfm$
```

Where:

* **--input directory** tells the application that must read videos from */opt/violence-detector/input*. Before running the application copy in this directory the videos you want to analyze.
* **--model xception** tells the application where the deep learning model is. The model will be loaded from */opt/violence-detector/models*. To see how to export the model check [exporting-models.md](exporting-models.md). In this case **xception** will be the directory name where the model was exported. 
* **--graphical** tels the application that graphical mode is available and a window will be openned to see the images and the prediction. To quit press *q*. This argument is optional. 

Preditions will be saved within directory */opt/violence-detector/output*. Images will be stored together with the prediction and a csv file will be created with all the information as well.

## Running the violence-detector application for webcam images processing

Activate the python virtual environment and run:

```bash
jadebustos@reypastor:~$ source ~/pyenvs/tfm-tf/bin/activate
(tfm-tf) jadebustos@reypastor:~$ cd tfm
(tfm-tf) jadebustos@reypastor:tfm$ python3 violence-detector --input webcam --model xception \
                                            --device 1 --graphical --width 800 --height 600
(tfm-tf) jadebustos@reypastor:tfm$
```

Where:

* **--input directory** tells the application that must read videos from */opt/violence-detector/input*. Before running the application copy in this directory the videos you want to analyze.
* **--model xception** tells the application where the deep learning model is. The model will be loaded from */opt/violence-detector/models*. To see how to export the model check [exporting-models.md](exporting-models.md). In this case **xception** will be the directory name where the model was exported. 
* **--device 1** tells the application the video device to use is **/dev/video1**. To see how to get the video devices check [video-devices.md](video-devices.md). 
* **--graphical** tells the application that graphical mode is available and a window will be openned to see the images and the prediction. To quit press *q*. This argument is optional. 
* **--width 800** tells the application the width component for the webcam resolution. By default 1280 is used.This argument is optional.
* **--height 600** tells the application the height component for the webcam resolution. By default 720 is used.This argument is optional.

Preditions will be saved within directory */opt/violence-detector/output*. Images will be stored together with the prediction and a csv file will be created with all the information as well.