# Container

Using containers allows you to use the application without having to struggle with installation.

The container engine used will be [Podman](https://podman.io/). [Buildah](https://buildah.io/) will be used to build the container images.

Docker can be used as well.

## Installing podman

Why podman?

Contrary to docker podman is a daemonless container engine which does not run containers as root. This means that security is increased due to container processes are executed as non-privileged users by default.

Whereas docker includes all functionality, [Podman](https://podman.io/) only runs containers. [Buildah](https://buildah.io/) is used to build containers and [Skopeo](https://github.com/containers/skopeo) is used for image management.

Although all the examples in this repository use podman, you can use docker as well.

### Installing podman in Debian 11 (Bullseye) or newer

Podman, buildah and skopeo are available in the official Debian repositories for Debian 11 or newer, so you only need to install them:

```bash
root@reypastor:~# apt install podman buildah skopeo -y
```

### Installing podman in Ubuntu 20.10 or newer

Podman, buildah and skopeo are available in the official Ubuntu repositories for Ubuntu 20.10 or newer, so you only need to install them:

```bash
root@reypastor:~# apt install podman buildah skopeo -y
```

### Installing podman in Ubuntu 20.04 or earlier

You will need to configure the [kubic repository to be able to install podman](https://phoenixnap.com/kb/install-podman-on-ubuntu).

### Installing podman for other Linux distributions

For other Linux distributions you can get how to install Podman from [the Podman documentation](https://podman.io/getting-started/installation).

## Getting the container image for violence-detector 

You do not need to build the container image. A tensorflow container image has been built so you can use it although you do not have any Intel Movidius device.

The image is available at my [docker repository](https://hub.docker.com/r/jadebustos2/violence-detector) and it includes a Xception model which achieved the following metrics over the test dataset:

* **Accuracy:** 96.50 %
* **Recall:** 94.71 %
* **Precision:** 98.50 %
* **Specificity:** 98.44 %
* **F1:** 0.9657

When evaluated over the [fight detection surveillance dataset](https://github.com/sayibet/fight-detection-surv-dataset):

* **Accuracy:** 52.00 %
* **Recall:** 51.30 %
* **Precision:** 78.67 %
* **Specificity:** 54.29 %
* **F1:** 0.6211

When evaluated over the [airtlab dataset](https://github.com/airtlab/A-Dataset-for-Automatic-Violence-Detection-in-Videos):

* **Accuracy:** 70.86 %
* **Recall:** 70.51 %
* **Precision:** 95.65 %
* **Specificity:** 73.68 %
* **F1:** 0.8118

To run the application some arguments are needed. These arguments can be passed to the container image as environment variables. The environment variables that can be used are:

* **VIDEO_INDEX** to tell the application the video device. By default this variable is set to **0**, so the default video device is */dev/video0*. This variable is mapped to the **--device** argument.
* **INPUT** to tell the application from where video will be read. By default is set to *directory*. This variable can take two values, **directory** and **webcam**. This variable is mapped to the **--input** argument.
* **MODEL** to tell the application what model to load. By default is set to *xception*. This variable is mapped to the **--model** argument.
* **WEIGHTS** to tell the application what weights to load for the model. By default is set to *xception.h5*. This variable is mapped to the **--weights** argument.
* **WIDTH** to tell the application the webcam's width. By default is set to *800*. This variable is mapped to the **--width** argument.
* **HEIGHT** to tell the application the webcam's height. By default is set to *600*. This variable is mapped to the **--height** argument.

## Using the container image for video file processing

To process videos you will need to copy them within a directory, for instance *~/videos/input*. You also need to create a directory to store the predictions, for instance *~/videos/output*.

As containers are non-persistent by default we will map the above directories. Thus the container will be able to access the videos to read them and the stored predictions will not be deleted after container termination.

```bash
[jadebustos@archimedes ~]$ podman run --rm --env INPUT='directory' \
                                -v ~/videos/input:/opt/violence-detector/input:Z \
                                -v ~/videos/output:/opt/violence-detector/output:Z \
                                --name violence-detector -d docker.io/jadebustos2/violence-detector
```

where:

* *~/videos/input* is the directory where are stored the videos we want to analyse. This directory is mapped to the container directory */opt/violence-detector/input*. The **:Z** is needed if you have SELINUX enabled.
* *~/videos/output* is the directory where the analized images will be stored. A directory for each video will be created in this directory. This directory is mapped to the container directory */opt/violence-detector/output*. The **:Z** is needed if you have SELINUX enabled.

The container will automatically stop after all the videos in the directory *~/videos/input* are processed.

## Using the container image for webcam image processing

To process images for the webcam you will need to create a directory to store the processed images. For instance, *~/videos/output*.

As containers are non-persistent by default we will map the above directory. Thus the container will be able to store predictions that will not be deleted after container termination.

```bash
[jadebustos@archimedes ~]$ podman run --rm --privileged --env INPUT='webcam' --env VIDEO_INDEX=1 \
                             --env WIDTH=1280 --env HEIGHT=720 \
                             -v /dev/:/dev:rslave --mount type=devpts,destination=/dev/pts \
                             -v ~/videos/output:/opt/violence-detector/output:Z \
                             --name violence-detector -d docker.io/jadebustos2/violence-detector

```

where:

* **--privileged** tells podman to start the container into the privileged mode. By default podman does not start container with privileges for security reasons. This is needed to access the webcam device.
* **--env WIDTH=1280 --env HEIGHT=720** configures the webcam resolution. These environment variables are optional, if not used 800x600 will be used.
* **-v /dev/:/dev:rslave --mount type=devpts,destination=/dev/pts** tells podman to mount the */dev* filesystem in the container which will allow the container to access the webcam device.
* *~/videos/output* is the directory where the analized images will be stored. This directory is mapped to the container directory */opt/violence-detector/output*. The **:Z** is needed if you have SELINUX enabled.

The container image will be running until the container is stopped:

```bash
[jadebustos@archimedes violence-detector]$ podman ps
CONTAINER ID  IMAGE                                           COMMAND     CREATED        STATUS             PORTS       NAMES
e7e264116a37  docker.io/jadebustos2/violence-detector:latest              9 seconds ago  Up 10 seconds ago              violence-detector
[jadebustos@archimedes violence-detector]$ podman stop violence-detector
violence-detector
[jadebustos@archimedes violence-detector]$ podman ps
CONTAINER ID  IMAGE       COMMAND     CREATED     STATUS      PORTS       NAMES
[jadebustos@archimedes violence-detector]$ 
```

## Using your own model

Although the container includes a trained model you can use your own model.

You have to export the model as explained in [exporting-models.md](exporting-models.md).

Copy the model and the weights file to a directory. For instance, *~/mymodels* and start the container adding the following:

```
-v ~/mymodels:/opt/violence-detector/models:Z
```

this will map the directory where you have stored your model to the containers' directory where the violence-detector application loads the model. For instance, if your model:

```bash
[jadebustos@archimedes violence-detector]$ ls -lh ~/mymodels/
total 474M
drwxr-xr-x. 4 jadebustos jadebustos   84 Sep 11 10:20 myvgg16-weights
-rw-r--r--. 1 jadebustos jadebustos 474M Sep 14 00:40 myvgg16-weights.h5
[jadebustos@archimedes violence-detector]$
```

you will have to add:

* **--env MODEL='myvgg16-model'** to load your custom model.
* **--env WEIGHTS='myvgg16-weights.h5'** to load the weights.

For instance, to process images from the webcam using your custom model:

```bash
[jadebustos@archimedes ~]$ podman run --rm --privileged --env INPUT='webcam' --env VIDEO_INDEX=1 \
                             --env MODEL='myvgg16-model' --env WEIGHTS='myvgg16-weights.h5' \
                             --env WIDTH=1280 --env HEIGHT=720 \
                             -v /dev/:/dev:rslave --mount type=devpts,destination=/dev/pts \
                             -v ~/mymodels:/opt/violence-detector/models:Z \
                             -v ~/videos/output:/opt/violence-detector/output:Z \
                             --name violence-detector -d docker.io/jadebustos2/violence-detector
```

## Building your own image

To build the x86_64 image you need:

* Export a model within the *models* directory. 
* Go to the *models* directory and compress it.
* Copy the weights file in the *models* directory.

  ```bash
  [jadebustos@archimedes violence-detector]$ ls -lh models/
  total 474M
  drwxr-xr-x. 4 jadebustos jadebustos   84 Sep 11 09:43 xception
  -rw-r--r--. 1 jadebustos jadebustos 474M Sep 13 23:32 xception.h5
  [jadebustos@archimedes violence-detector]$
  ```

* Modify the [Dockerfile.tensorflow.x86_64](Dockerfile.tensorflow.x86_64) to fit your files:

  ```dockerfile
  ...
  ENV MODEL="xception"
  ENV WEIGHTS="xception.h5"
  ...
  ADD models/xception.tgz /opt/violence-detector/models/
  COPY models/xception.h5 /opt/violence-detector/models/
  ...
  ```

You can build the container image:

```bash
[jadebustos@archimedes violence-detector]$ buildah build -f Dockerfile.tensorflow.x86_64 -t violence-detector:v1
...
[jadebustos@archimedes violence-detector]$
```

The image is ready to be used:

```bash
[jadebustos@archimedes violence-detector]$ podman images
REPOSITORY                          TAG         IMAGE ID      CREATED            SIZE
localhost/violence-detector         v1          2bceeaf1290b  20 minutes ago     3.01 GB
<none>                              <none>      6746ee629965  About an hour ago  2.51 GB
<none>                              <none>      e8c9eb54f475  2 hours ago        2.51 GB
<none>                              <none>      c8e841089f76  3 hours ago        2.49 GB
<none>                              <none>      1a0339f218a6  3 hours ago        205 MB
quay.io/centos/centos               stream9     047d6e0a5993  4 days ago         160 MB
[jadebustos@archimedes violence-detector]$
```