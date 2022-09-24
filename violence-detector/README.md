# Violence Detector application

This application can be used to detect violent situations on videos or using a webcam. As this software has created for my Master Thesis it is not intended to be an Enterprise application, thus many things can be improved.

This application has been developed to be executed as a container image. For this reason some parameters are hardcoded into the code.

This applicantion can predict from two sources:

* To process video files.
* To process images from a webcam.

This application is intended to test models so it uses tensorflow instead of OpenVINO. So, you can try it although you do not have a Myriad device.

Using the application:

* You can use the application in [standalone mode](standalone.md).
* You can use the application using a [container image](containers.md). So you do not have to install the application and its dependencies.
