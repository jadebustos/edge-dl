# Converting a Tensorflow 2.x model to OpenVINO

Tensorflow models needs to be converted to IR format to be used by the Intel® Neural Compute Stick 2 (Intel® NCS2). 

## Exporting the Tensorflow 2.x model

The tensorflow model has to be converte to a tensorflow frozen graph:

```bash
jadebustos@movidius:~/edge-dl/movidius$ python3 export_tf_model.py --model trained-xception-b16-e128-16frames-acc-dropout-0.5-alt3.h5 --name xception
...
jadebustos@movidius:~/edge-dl/movidius$ ls -lh xception/
total 1.1G
-rw-rw-r-- 1 jadebustos jadebustos 277M sep 10 15:49 xception_frozen_graph.pb
-rw-rw-r-- 1 jadebustos jadebustos 788M sep 10 15:50 xception_frozen_graph.pbtxt
jadebustos@movidius:~/edge-dl/movidius$
```

## Converting the exported model to the IR format

The tensorflow frozen graph will be converted to IR format:

```bash
jadebustos@movidius:~/edge-dl/movidius$ python3 /opt/intel/openvino_2021/deployment_tools/model_optimizer/mo_tf.py --input_model xception/xception_frozen_graph.pb --input_shape=\[1,200,200,3\] --output_dir xception_ir --data_type FP16
...
[ SUCCESS ] Generated IR version 10 model.
[ SUCCESS ] XML file: /home/jadebustos/tfm/tfm-software/openvino/xception_ir/xception_frozen_graph.xml
[ SUCCESS ] BIN file: /home/jadebustos/tfm/tfm-software/openvino/xception_ir/xception_frozen_graph.bin
[ SUCCESS ] Total execution time: 23.02 seconds. 
[ SUCCESS ] Memory consumed: 1862 MB. 
jadebustos@movidius:~/edge-dl/movidius$ ls -lh xception_ir/
total 139M
-rw-rw-r-- 1 jadebustos jadebustos 139M sep 10 15:51 xception_frozen_graph.bin
-rw-rw-r-- 1 jadebustos jadebustos  53K sep 10 15:51 xception_frozen_graph.mapping
-rw-rw-r-- 1 jadebustos jadebustos 161K sep 10 15:51 xception_frozen_graph.xml
jadebustos@movidius:~/edge-dl/movidius$
```