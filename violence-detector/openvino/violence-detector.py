#!/usr/bin/python

# Copyright (c) 2022 Jose Angel de Bustos Perez
# May be copied or modified under the terms of 
# the GNU General Public License v3.0. 
# See https://www.gnu.org/licenses/gpl-3.0.html

import argparse
from fcntl import DN_DELETE
import sys

from mywebcamfeed import *
from myvideofeed import *
from myutils import *
from myvars import *
from mycnn import *

def main():
    # parser initialization
    description_msg = "Violence detection application (OpenVINO)."
    parser = argparse.ArgumentParser(description = description_msg)

    # defining arguments
    parser.add_argument("-i", "--input", type=str, required=True, 
                            help = "Image input source: webcam or directory.")

    parser.add_argument("-x", "--model-xml", type=str, required=True, 
                            help = "Model XML bin.")

    parser.add_argument("-b", "--model-bin", type=str, required=True, 
                            help = "Model bin file.")

    parser.add_argument("-d", "--device", type=int, help="Video device index.")

    parser.add_argument("-a", "--accelerator", type=str, default="CPU", required=True,
        help="Acceleration device (CPU, MYRIAD).")

    parser.add_argument("-t", "--height", type=int, default=800, 
        help="Webcam height resolution (default 720).")

    parser.add_argument("-l", "--width", type=int, default=600, 
        help="Webcam width resolution (default 1280).")

    parser.add_argument("-g", "--graphical", action="store_true", 
        help="Graphical mode when a webcam is being used.")

    # parsing arguments
    parser.parse_args()

    # read arguments from command line
    args = vars(parser.parse_args())

    # arguments validation
    if ( args['input'] not in ['webcam', 'directory'] ):
        print("Only webcam or directory are valid values for input argument.")
        sys.exit(255)

    if ( args['accelerator'] not in ['CPU', 'MYRIAD'] ):
        print("Only CPU or MYRIAD are valid values for accelerator argument.")
        sys.exit(255)

    # video arguments validation
    if ( args['input'] == 'webcam' ):
        if args['device'] is None:
            print("When using webcam as input device the --device parameter is mandatory.")
            sys.exit(251)

    # model creation
    xml = os.path.join('/opt/violence-detector/models', args['model_xml'])
    bin = os.path.join('/opt/violence-detector/models', args['model_bin'])
    mymodel, mynet = create_cnn(xml, bin, args['accelerator'])

    if args['input'] == 'directory':
        videos = get_files_dir(INPUT_DIR)
        videos_path = INPUT_DIR
        try:
            predict_videos(mymodel, mynet, videos, videos_path, args)
        except Exception as e:
            print("*************************************************")
            print("Error predicting videos.")
            print("*************************************************")
            print(e)
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            exit(253)
    else:
        try:
            predict_webcam(mymodel, mynet, args)
        except Exception as e:
            print("*************************************************")
            print("Error predicting from webcam.")
            print("*************************************************")
            print(e)
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            exit(250)

    sys.exit(0)

if __name__ == "__main__":
    main()