# Violence detector application

The violence applications has been created using two different technologies for inference:

* Tensorflow 2.x.
* OpenVINO toolkit.

Violence detector deployment modes:

|          | Standalone | Container |
|----------|------------|-----------|
| x86_64   |     Yes    |    Yes    |
| Raspberry Pi |     Yes    |    No     |

Violence detector functionalities:

|          | Webcam     | Video files |
|----------|------------|-----------|
| x86_64   |     Yes    |    Yes    |
| Raspberry Pi |     Yes    |    No     |

## Tensorflow 2.0 version

You can use this version in any computer and you can take advantage of NVIDIA GPUs if you have installed CUDA. If you have not got any NVIDIA GPU you still can use the application.

You can get all the information for the Tensorflow Violence detector application [here](tensorflow/README.md).

## OpenVINO toolkit version

You can use this version if you have a Intel® Neural Compute Stick 2 (Intel® NCS2) or an Intel® CPU.

You can get all the information for the OpenVINO Violence detector application [here](openvino/README.md).

## Containerized version

A containerized versión has been created for x86_64. If you want to use it you will have to install a container engine. You can check how to install a [container engine](installing-containers.md).

A container for Raspberry Pi has not been created due to Raspberry Pi is running a 32-bits OS. This OS is based on Debian Buster, which is a bit older and the effort to create the container image is not worht it, from my point of view.
