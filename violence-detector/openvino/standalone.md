# Violence detector application in standalone mode

To use the application in standalone mode you will have to install both the application and its dependencies.

## Requirements

The following directories must be created:

* */opt/violence-detector*, root directory for all data needed/producted.
* */opt/violence-detector/input*, when videos are used to detect violent situations will be readed from this directory.
* */opt/violence-detector/output*, predictions will be stored in this directory.
* */opt/violence-detector/models*, deep learning models and weights will be stored in this directory.

It is recommended using [python virtual environments](../virtual-environment.md). The following configuration was tested:

* *python*, version 3.7 was used.
* *numpy*, 1.19.5 version was used.
* *opencv-python*, 4.6.0.66 version was used.
* *tensorflow*, 2.5.3 version was used.

Images will be resized to 200x200 to feed the deep learning models. If you use your own models you will need to modify **IMAGE_WIDTH** and **IMAGE_HEIGHT** variables in [myvars.py](myvars.py) to fit your input shape.

By default one of each five images will be choosen to make a prediction. If you want to modify that you need to change the **FRAMES_STEP** variable in [myvars.py](myvars.py) accordingly.

## Running the violence-detector application for video file processing

Activate the python virtual environment and run:

```bash
jadebustos@reypastor:~$ source ~/pyenvs/tfm-tf/bin/activate
(tfm-tf) jadebustos@reypastor:~$ cd tfm
(tfm-tf) jadebustos@reypastor:tfm$ python3 violence-detector.py ---input directory  \
                                      --model-xml xception_frozen_graph.xml \
                                      --model-bin xception_frozen_graph.bin \
                                      --accelerator MYRIAD --graphical
(tfm-tf) jadebustos@reypastor:tfm$
```

Where:

* **--input directory** tells the application that must read videos from */opt/violence-detector/input*. Before running the application copy in this directory the videos you want to analyze.
* **--model-xml xception_frozen_graph.xml** tells the application where the deep learning model is. This model is in IR OpenVINO format. The model will be loaded from */opt/violence-detector/models*. To see how to export the model check [tensorflow2openvino.md](../../movidius/dev/tensorflow2openvino.md).
* **--model-bin xception_frozen_graph.bin** tells the application where the trained weights are. The weights will be loaded from */opt/violence-detector/models*. To see how to export the model check [tensorflow2openvino.md](../../movidius/dev/tensorflow2openvino.md).
* **--accelerator MYRIAD** tells the application what acceleration device use. Two values can be used, **CPU** or **MYRIAD**.
* **--graphical** tels the application that graphical mode is available and a window will be opened to see the images and the prediction. To quit press *q*. This argument is optional. 

Preditions will be saved within directory */opt/violence-detector/output*. A directory for each video will be created. Iimages will be stored together with the prediction and a csv file will be created with all the information as well.

## Running the violence-detector application for webcam image processing

Activate the python virtual environment and run:

```bash
jadebustos@reypastor:~$ source ~/pyenvs/tfm-tf/bin/activate
(tfm-tf) jadebustos@reypastor:~$ cd tfm
(tfm-tf) jadebustos@reypastor:tfm$ python3 violence-detector.py --input webcam  --model-xml xception_frozen_graph.xml \
                                              --model-bin xception_frozen_graph.bin --accelerator MYRIAD --graphical \
                                              --device 1 --graphical --width 800 --height 600
(tfm-tf) jadebustos@reypastor:tfm$
```

Where:

* **--input directory** tells the application that must read videos from */opt/violence-detector/input*. Before running the application copy in this directory the videos you want to analyze.
* **--model-xml xception_frozen_graph.xml** tells the application where the deep learning model is. This model is in IR OpenVINO format. The model will be loaded from */opt/violence-detector/models*. To see how to export the model check [tensorflow2openvino.md](../../movidius/dev/tensorflow2openvino.md).
* **--model-bin xception_frozen_graph.bin** tells the application where the trained weights are. The weights will be loaded from */opt/violence-detector/models*. To see how to export the model check [tensorflow2openvino.md](../../movidius/dev/tensorflow2openvino.md).
* **--accelerator MYRIAD** tells the application what acceleration device use. Two values can be used, **CPU** or **MYRIAD**.
* **--device 1** tells the application the video device to use is **/dev/video1**. To see how to get the video devices check [video-devices.md](../video-devices.md). 
* **--graphical** tells the application that graphical mode is available and a window will be openned to see the images and the prediction. To quit press *q*. This argument is optional. 
* **--width 800** tells the application the width component for the webcam resolution. By default 1280 is used.This argument is optional.
* **--height 600** tells the application the height component for the webcam resolution. By default 720 is used.This argument is optional.

Predictions will be saved within directory */opt/violence-detector/output*. Images will be stored together with the prediction and a csv file will be created with all the information as well.

## Using your own custom model

To use your own custom model you need:

* Export a xml model within the *models* directory. 
* Copy the bin file in the *models* directory.

  ```bash
  [jadebustos@archimedes violence-detector]$ ls -lh models/
  total 139M
  -rw-rw-r--. 1 jadebustos jadebustos 139M Sep 15 15:51 xception_frozen_graph.bin
  -rw-rw-r--. 1 jadebustos jadebustos 161K Sep 15 15:51 xception_frozen_graph.xml
  [jadebustos@archimedes violence-detector]$
  ```

> ![](../../icons/warning-icon.png) Your model will have to use a 200x200 image size. If you need to change the model image size you can modify it in the file [myvars.py](myvars.py).

After that you can run the violent-detector application using **--model-xml mycustomodelxml** and **--model-bin mycustommodelbin**.