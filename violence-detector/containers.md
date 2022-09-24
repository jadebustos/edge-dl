# Container

```bash
[jadebustos@archimedes violence-detector]$ buildah build -f Dockerfile.tensorflow.x86_64 -t violence-detector:v1
```

```bash
[jadebustos@archimedes ~]$ podman run --rm --privileged --env INPUT='directory' --env MODEL='xception' \
                             -v /dev/:/dev:rslave --mount type=devpts,destination=/dev/pts \
                             -v /opt/violence-detector/input:/opt/violence-detector/input:Z \
                             -v /opt/violence-detector/output:/opt/violence-detector/output:Z \
                             --name violence-detector -d localhost/violence-detector:v1
```

```bash
[jadebustos@archimedes ~]$ podman run --rm --privileged --env INPUT='webcam' --env VIDEO_INDEX=1 --env MODEL='xception' \
                             --env WIDTH=1280 --env HEIGHT=720 \
                             -v /dev/:/dev:rslave --mount type=devpts,destination=/dev/pts \
                             -v /opt/violence-detector/output:/opt/violence-detector/output:Z \
                             --name violence-detector -d localhost/violence-detector:v1

```