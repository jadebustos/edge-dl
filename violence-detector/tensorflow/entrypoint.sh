#!/bin/bash

# Copyright (c) 2022 Jose Angel de Bustos Perez
# May be copied or modified under the terms of 
# the GNU General Public License v3.0. 
# See https://www.gnu.org/licenses/gpl-3.0.html

case $INPUT in
    "directory") /usr/bin/python3 violence-detector.py --input $INPUT --model $MODEL --weights $WEIGHTS ;;
    "webcam") /usr/bin/python3 violence-detector.py --input $INPUT --model $MODEL --weights $WEIGHTS \
                                    --device $VIDEO_INDEX --width $WIDTH --height $HEIGHT ;;
    *) echo "Only webcam and directory are allowed as input source." 
       exit 1;;
esac