# README

A x86_64 laptop will be used to convert tensorflow models to the OpenVINO format.

## Installation

The version we will install is the OpenVINO 2021.2 under Ubuntu 18.04 LTS.

The installation procedure is described in [OpenVINO official documentation](https://docs.openvino.ai/2021.2/openvino_docs_install_guides_installing_openvino_linux.html)

Before configuring the Model Optimizer you should install:

```bash
jadebustos@movidius:~$ pip install setuptools
```

Only the tensorflow2 framework is required:

```bash
jadebustos@movidius:intall_prerequisites$ sudo ./install_prerequisites_tf2.sh
```

## Converting the model

To convert the model you need to export it:

```python

import tensorflow as tf

model_filename = 'trained-vgg16-b16-e128-16frames-acc-dropout-0.5-alt3.h5'
model_export_name = 'vgg16'

model = tf.keras.models.load_model(model_filename)

tf.saved_model.save(model, model_export_name)
```

The above will create a directory named **vgg16** where the model is exported.