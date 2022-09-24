# Container

```bash
[jadebustos@archimedes violence-detector]$ buildah build -f Dockerfile.tensorflow.x86_64 -t violence-detector:v1
```

```bash
[jadebustos@archimedes ~]$ podman run --rm --env VIDEO_INDEX=1 --privileged -v /dev/:/dev:rslave \
                            --mount type=devpts,destination=/dev/pts \
                            -v /opt/violence-detector/input:/opt/violence-detector/input:Z \
                            -v /opt/violence-detector/ouput:/opt/violence-detector/output:Z \
                            -d localhost/violence-detector:v1
```