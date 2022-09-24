# Copyright (c) 2022 Jose Angel de Bustos Perez
# May be copied or modified under the terms of 
# the GNU General Public License v3.0. 
# See https://www.gnu.org/licenses/gpl-3.0.html

import tensorflow as tf
import tensorflow.keras as K
import os

from myvars import *

# model is read from directory nn_name under MODELS_DIR directory
def create_cnn(nn_name):
    try:
        mymodel = tf.keras.models.load_model(os.path.join(MODELS_DIR, nn_name))
    except Exception as e:        
        print("*************************************************")
        print("Error creating model.")
        print("*************************************************")
        print(e)
        exit(254)
    return mymodel
