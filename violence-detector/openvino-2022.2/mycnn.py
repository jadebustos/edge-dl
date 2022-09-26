# Copyright (c) 2022 Jose Angel de Bustos Perez
# May be copied or modified under the terms of 
# the GNU General Public License v3.0. 
# See https://www.gnu.org/licenses/gpl-3.0.html

from openvino.runtime import Core

from myvars import *

# model xml is read from directory nn_name under MODELS_DIR directory
# device is MYRIAD or CPU
def create_cnn(nn_xml, device):
    try:
        ie = Core()
        mymodel = ie.read_model(model=nn_xml)
        compiled_model = ie.compile_model(model=mymodel, device_name=device)
    except Exception as e:        
        print("*************************************************")
        print("Error creating model.")
        print("*************************************************")
        print(e)
        exit(254)
    return compiled_model
