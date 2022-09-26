# Violence Detector application (OpenVINO toolkit)

This application can be used to detect violent situations on videos or using a webcam. As this software has created for my Master Thesis it is not intended to be an Enterprise application, thus many things can be improved.

It has been developed to be executed as a container image using OpenVINO toolkit. For this reason some parameters are hardcoded into the code.

Predictions can be performed from two sources:

* Processing video files.
* Processing images from a webcam.

This application is intended to use OpenVINO. So, you need have a Myriad device to use it or a Intel CPU.

Using the application:

* You can use the application in [standalone mode](standalone.md).

> ![](../../icons/information-icon.png) Application it is being migrated to OpenVINO 2022.2 which uses a new API. This new OpenVINO version is not supported on the Raspberry Pi.