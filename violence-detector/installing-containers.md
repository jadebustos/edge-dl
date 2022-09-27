# Containers

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

