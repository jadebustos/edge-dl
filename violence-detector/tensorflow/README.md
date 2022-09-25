# Violence Detector application (Tensorflow 2.x)

This application can be used to detect violent situations on videos or using a webcam. As this software has created for my Master Thesis it is not intended to be an Enterprise application, thus many things can be improved.

It has been developed to be executed as a container image using Tensorflow 2.x. For this reason some parameters are hardcoded into the code.

Predictions can be performed from two sources:

* Processing video files.
* Processing images from a webcam.

This application is intended to test models so it uses tensorflow instead of OpenVINO. So, you can try it although you do not have a Myriad device.

Using the application:

* You can use the application in [standalone mode](standalone.md).
* You can use the application using a [container image](containers.md). So you do not have to install the application and its dependencies.
