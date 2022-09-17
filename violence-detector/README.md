# Violence Detector application

This application can be used to detect violent situations on videos or using a webcam. As this software has created for my Master Thesis it is not intended to be an Enterprise application, thus many things can be improved.

This application has been developed to be executed as a container image. For this reason some parameters are hardcoded into the code.

## Requirements

The following directories are required:

* */opt/violence-detector*, root directory for all data needed/producted.
* */opt/violence-detector/input*, when videos are used to detect violent situations will be readed from this directory.
* */opt/violence-detector/output*, predictions will be stored in this directory.
* */opt/violence-detector/models*, deep learning models will be stored in this directory.