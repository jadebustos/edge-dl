# Video devices

To gather information about the video devices that are present on your computer and the resolutions they are able to work with you will need to install the Video4Linux packages.

## Installing Video4Linux

To install Video4Linux in Debian family:

```bash
jadebustos@reypastor:~# apt-get install v4l-utils -y
jadebustos@reypastor:~#
```

To install Video4Linux in Red Hat family:

```bash
[jadebustos@archimedes ~]# dnf install v4l-utils -y
[jadebustos@archimedes ~]#
```

## Getting information for the video devices

To get the video devices available in the system:

```console
[jadebustos@archimedes ~]$ v4l2-ctl --list-devices
OBS Virtual Camera (platform:v4l2loopback-000):
        /dev/video0

HD Pro Webcam C920 (usb-0000:00:14.0-2.1.3):
        /dev/video5
        /dev/video6
        /dev/media2

Integrated Camera: Integrated C (usb-0000:00:14.0-8):
        /dev/video1
        /dev/video2
        /dev/video3
        /dev/video4
        /dev/media0
        /dev/media1

[jadebustos@archimedes ~]$
```

You can get information about the webcam:

```console
[jadebustos@archimedes ~]$ v4l2-ctl -d /dev/video5 --list-formats
ioctl: VIDIOC_ENUM_FMT
        Type: Video Capture

        [0]: 'YUYV' (YUYV 4:2:2)
        [1]: 'MJPG' (Motion-JPEG, compressed)
[jadebustos@archimedes ~]$
```
Or the extended one:

```console
[jadebustos@archimedes ~]$ v4l2-ctl -d /dev/video5 --list-formats-ext
ioctl: VIDIOC_ENUM_FMT
        Type: Video Capture

        [0]: 'YUYV' (YUYV 4:2:2)
                Size: Discrete 640x480
                        Interval: Discrete 0.033s (30.000 fps)
                        Interval: Discrete 0.042s (24.000 fps)
                        Interval: Discrete 0.050s (20.000 fps)
                        Interval: Discrete 0.067s (15.000 fps)
                        Interval: Discrete 0.100s (10.000 fps)
                        Interval: Discrete 0.133s (7.500 fps)
                        Interval: Discrete 0.200s (5.000 fps)
...
[jadebustos@archimedes ~]$
```