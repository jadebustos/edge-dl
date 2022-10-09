#!/usr/bin/python3

# Copyright (c) 2022 Jose Angel de Bustos Perez
# May be copied or modified under the terms of 
# the GNU General Public License v3.0. 
# See https://www.gnu.org/licenses/gpl-3.0.html

# check inference devices

import openvino.inference_engine as ie

engine = ie.IECore()
print(engine.available_devices)