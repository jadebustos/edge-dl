# Container

Using containers allows you to use the application without having to struggle with installation.

The container engine used will be [Podman](https://podman.io/). [Buildah](https://buildah.io/) will be used to build the container images.

Docker can be used as well.

## Building the image

To build the x86_64 image you need:

* Export a model within the *models* directory. 
* Go to the *models* directory and compress it.
* Copy the weights file in the *models* directory.
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

To run the application some arguments are needed. These arguments can be passed to the container image as environment variables. The environment variables that can be used are:

* **VIDEO_INDEX** to tell the application the video device. By default this variable is set to **0**, so the default video device is */dev/video0*. This variable is mapped to the **--device** argument.
* **INPUT** to tell the application from where video will be read. By default is set to *directory*. This variable can take two values, **directory** and **webcam**. This variable is mapped to the **--input** argument.
* **MODEL** to tell the application what model to load. By default is set to *xception*. This variable is mapped to the **--model** argument.
* **WEIGHTS** to tell the application what weights to load for the model. By defalt is set to *xception.h5*. This variable is mapped to the **--weights** argument.
* **WIDTH** to tell the application the webcam's width. By default is set to *800*. This variable is mapped to the **--width** argument.
* **HEIGHT** to tell the application the webcam's height. By default is set to *600*. This variable is mapped to the **--height** argument.

## Using the container image for video file processing

To process videos you need to copy them within a directory, for instance *~/videos/input*. You also need to create a directory to store the predictions, for instance *~/videos/output*.

As containers are non-persistent by default we will map the above directories. Thus the container will be able to access the videos to read them and the stored predictions will not be deleted after container termination.

```bash
[jadebustos@archimedes ~]$ podman run --rm --privileged --env INPUT='directory' \
                                -v /dev/:/dev:rslave --mount type=devpts,destination=/dev/pts \
                                -v ~/videos/input:/opt/violence-detector/input:Z \
                                -v ~/videos/output:/opt/violence-detector/output:Z \
                                --name violence-detector -d localhost/violence-detector:v1
```

## Using the container image for webcam image processing

```bash
[jadebustos@archimedes ~]$ podman run --rm --privileged --env INPUT='webcam' --env VIDEO_INDEX=1 \
                            --env MODEL='xception' --weights='xception.h5' \
                             --env WIDTH=1280 --env HEIGHT=720 \
                             -v /dev/:/dev:rslave --mount type=devpts,destination=/dev/pts \
                             -v ~/videos/output:/opt/violence-detector/output:Z \
                             --name violence-detector -d localhost/violence-detector:v1

```