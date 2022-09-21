# Converting the model

To convert a tensorflow 2.0 model to the OpenVINO format you will need:

```python

import tensorflow as tf

model_filename = 'trained-vgg16-b16-e128-16frames-acc-dropout-0.5-alt3.h5'
model_export_name = 'vgg16'

model = tf.keras.models.load_model(model_filename)

tf.saved_model.save(model, model_export_name)
```

The above will create a directory named **vgg16** where the model is exported.