#!/bin/bash

podman run --rm --privileged --env INPUT='webcam' --env VIDEO_INDEX=1 \
                             --env WIDTH=1280 --env HEIGHT=720 \
                             -v /dev/:/dev:rslave --mount type=devpts,destination=/dev/pts \
                             -v /opt/violence-detector/output:/opt/violence-detector/output:Z \
                             --name violence-detector-openvino -it localhost/violence-detector-openvino-2022.2.0:v1 /bin/bash
