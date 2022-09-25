#!/usr/bin/python3

# Copyright (c) 2022 Jose Angel de Bustos Perez
# May be copied or modified under the terms of 
# the GNU General Public License v3.0. 
# See https://www.gnu.org/licenses/gpl-3.0.html

# this script is based on:
#    https://ksingh7.medium.com/part-iii-convert-keras-model-to-tensorflow-frozen-graph-model-a6aa6b1aaeee

import tensorflow as tf
import numpy as np
import argparse
import sys
import os

from tensorflow import keras
from tensorflow.python.framework.convert_to_constants import convert_variables_to_constants_v2

def main():
    # parser initialization
    description_msg = "Export tensorflow 2.x models."
    parser = argparse.ArgumentParser(description = description_msg)

    # defining arguments
    parser.add_argument("-m", "--model", type=str, required=True, 
                            help = "Tensorflow model.")

    parser.add_argument("-n", "--name", type=str, required=True, 
                            help = "Exported model name.")

    # parsing arguments
    parser.parse_args()

    # read arguments from command line
    args = vars(parser.parse_args())

    # load model
    model = keras.models.load_model(args['model'])

    # convert model to concrete_function
    full_model = tf.function(lambda x: model(x))
    concrete_func = full_model.get_concrete_function(
        x = tf.TensorSpec(model.inputs[0].shape, model.inputs[0].dtype))

    # get frozen concrete_function
    frozen_func = convert_variables_to_constants_v2(concrete_func)
    frozen_func.graph.as_graph_def()

    # serialize the frozen graph
    model_export_name = args['name'] + "_frozen_graph" 
    tf.io.write_graph(graph_or_graph_def=frozen_func.graph,
        logdir=args['name'],
        name=model_export_name + ".pb",
        as_text=False)

    # frozen graph text representation
    tf.io.write_graph(graph_or_graph_def=frozen_func.graph,
        logdir=args['name'],
        name=model_export_name + ".pbtxt",
        as_text=True)

if __name__ == "__main__":
    main()