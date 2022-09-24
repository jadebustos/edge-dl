#!/bin/bash

#podman run --rm --privileged --env INPUT='directory' --env MODEL='xception' --env WEIGHTS='xception.h5' \
podman run --rm --privileged --env INPUT='directory' \
                             -v /dev/:/dev:rslave --mount type=devpts,destination=/dev/pts \
                             -v /opt/violence-detector/input:/opt/violence-detector/input:Z \
                             -v /opt/violence-detector/output:/opt/violence-detector/output:Z \
                             --name violence-detector -d localhost/violence-detector:v1
#                             --entrypoint /bin/bash -it localhost/violence-detector:v1
#                             -v /opt/violence-detector/input:/opt/violence-detector/input:Z \
