# Executing AI models using OpenVINO toolkit

To execute models with OpenVINO toolkit you will need to follow some steps:

1. Create a model using a framework supported by OpenVINO, for instance [Tensorflow 2.x](../notebooks/README.md).
2. The model will have to be converted to [OpenVINO IR format](dev/README.md).
3. Create an application to perform inference using that model. The [violence-detector application](../violence-detector/openvino/README.md) is an application example using OpenVINO toolkit. There is a [Tensorflow 2.x version](../violence-detector/tensorflow/README.md) as well.