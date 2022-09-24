# Exporting tensorflow models

You need to export your model to be used by *violence-detector* application.

To export it you need to load the h5 file and export it in the following way:

```python
#!/usr/bin/python3

import tensorflow as tf

h5model = 'trained-vgg16-b16-e256-16frames-last-dropout05-alt1.h5'

model = tf.keras.models.load_model(h5model)
tf.saved_model.save(model,'vgg16')
```

This will create a directory named *vgg16*. You will need to copy this directory to */opt/violence-detector/models* and use **vgg16** as parameter for **--model**.