#!/bin/bash

# Copyright (c) 2022 Jose Angel de Bustos Perez
# May be copied or modified under the terms of 
# the GNU General Public License v3.0. 
# See https://www.gnu.org/licenses/gpl-3.0.html

source ~/.pyenv/versions/3.7.5/envs/tfm-tf/bin/activate

 case $INPUT in
    "directory")  ;;
    "webcam") /usr/bin/python3 violence-detector.py --input $INPUT --model $MODEL --device $VIDEO_INDEX \
                                    --width $WIDTH --height $HEIGHT ;;
    *) echo "other" ;;
esac

#/usr/bin/python3 violence-detector.py --device $VIDEO_INDEX
