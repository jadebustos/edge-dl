# Copyright (c) 2022 Jose Angel de Bustos Perez
# May be copied or modified under the terms of 
# the GNU General Public License v3.0. 
# See https://www.gnu.org/licenses/gpl-3.0.html

from openvino.inference_engine import IECore, IENetwork

from myvars import *

# model xml is read from directory nn_name under MODELS_DIR directory
# model bin is read from directory nn_weights under MODELS_DIR directory
# device is MYRIAD or CPU
def create_cnn(nn_xml, nn_bin, device):
    try:
        ie = IECore()
        net = IENetwork(model=nn_xml, weights=nn_bin)
        mymodel = ie.load_network(network=net, device_name=device)
    except Exception as e:        
        print("*************************************************")
        print("Error creating model.")
        print("*************************************************")
        print(e)
        exit(254)
    return mymodel, net
