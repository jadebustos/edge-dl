# Violence Detector application

This application can be used to detect violent situations on videos or using a webcam. As this software has created for my Master Thesis it is not intended to be an Enterprise application, thus many things can be improved.

This application has been developed to be executed as a container image. For this reason some parameters are hardcoded into the code.

This applicantion can be used in two ways:

* To process videos.
* To process images from a webcam.

## Requirements

The following directories must be created:

* */opt/violence-detector*, root directory for all data needed/producted.
* */opt/violence-detector/input*, when videos are used to detect violent situations will be readed from this directory.
* */opt/violence-detector/output*, predictions will be stored in this directory.
* */opt/violence-detector/models*, deep learning models will be stored in this directory.

It is recommended using [python virtual environments](virtual-environment.md) with the following python modules installed:

* *numpy*, 1.19.5 version was used.
* *opencv-python*, 4.6.0.66 version was used.
* *tensorflow*, 2.5.3 version was used.

## Running the violence-detector application for video processing

```bash
jadebustos@reypastor:~$ source ~/pyenvs/tfm-tf/bin/activate
(tfm-tf) jadebustos@reypastor:~$ cd tfm
(tfm-tf) jadebustos@reypastor:tfm$ python3 violence-detector --input directory --model xception --weights xception.h5 \
                                         --device 1 --graphical
(tfm-tf) jadebustos@reypastor:tfm$
(tfm-tf) jadebustos@reypastor:tfm$
(tfm-tf) jadebustos@reypastor:tfm$
(tfm-tf) jadebustos@reypastor:tfm$
```

