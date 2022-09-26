# Copyright (c) 2022 Jose Angel de Bustos Perez
# May be copied or modified under the terms of 
# the GNU General Public License v3.0. 
# See https://www.gnu.org/licenses/gpl-3.0.html

import numpy as np
import cv2
import os

from openvino.runtime import Core

from datetime import datetime
from myvars import *

def predict_webcam(model, args):
    width = int(args['width'])
    height = int(args['height'])

    input_layer_ir = model.input(0)
    out_layer_ir = model.output(0)

    webcam_index = int(args['device'])
    # one of FRAMES_STEP will be read to predict
    frame_index = 1

    try:
        #video_capture = cv2.VideoCapture(webcam_index, cv2.CAP_ANY)
        video_capture = cv2.VideoCapture(webcam_index, cv2.CAP_V4L)
    except Exception as e:
            print("*************************************************")
            print("Error opening video device.")
            print("*************************************************")
            print(e)
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            exit(249)

    # setting camera resolution
    #video_capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m','j','p','g'))
    #video_capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M','J','P','G'))
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, width);
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height);
    if video_capture.isOpened():
        cam_width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        cam_height = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print("Camera resolution: %d x %d" % (cam_width, cam_height))

        # store video predictions in csv file
        csv_data = ["File;Prediction;Probability"]
        datetime_data = datetime.now()
        csv_filename = 'predictions-' + str(datetime_data.year) + str(datetime_data.month) + str(datetime_data.day) + '-' + str(datetime_data.hour) + ':' + str(datetime_data.minute) + ':' + str(datetime_data.second) + '.csv'
        try:
            csv_file = open(os.path.join(OUTPUT_DIR, csv_filename), "w")
        except Exception as e:
            print("*************************************************")
            print("Error writing to filesystem.")
            print("*************************************************")
            print(e)
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            exit(249)

        while True:
            # one of FRAMES_STEP frames is used to predict
            if frame_index != FRAMES_STEP:
                frame_index += 1
                continue
            
            # reset frame_index
            frame_index = 1

            # capture frames from webcam
            sucess, image = video_capture.read()
            if not sucess:
                continue

            # resize image
            resized = cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT))
            # reorder channels
            resized = np.moveaxis(resized, -1, 0)

            # predict using model
            webcam_frame = []
            webcam_frame.append(resized)
            frame = (np.array(webcam_frame).astype('float32'))/255
            prediction = model(frame, out_layer_ir)
            print(prediction)
            prediction = prediction[out_blob]
            pred_value = prediction[0][0]

            datetime_frame = datetime.now()
            frame_filename = 'frame-' + str(datetime_frame.year) + str(datetime_frame.month) + str(datetime_frame.day) + '-' + str(datetime_frame.hour) + ':' + str(datetime_frame.minute) + ':' + str(datetime_frame.second) + ':' + str(datetime_frame.microsecond) + '.png'            
            
            # label frames
            if pred_value > 0.5:
                prob = round(100 * pred_value, 2)
                label = "Non-Violence: " + str(prob) + ' %'
                # text color
                red = 0
                green = 255
                data_row = frame_filename + ';' + label.split(':')[0] + ';' + str(pred_value) + '\n'
            else:
                prob = round(100 * (1. - pred_value), 2)
                label = "Violence: " + str(prob) + ' %'
                # text color
                red = 255
                green = 0
                data_row = frame_filename + ';' + label.split(':')[0] + ';' + str(1. - pred_value) + '\n'

            # fontsize
            fontSize = 3
            # coordinates to print label
            x = 20
            y = 80
            if ( image.shape[1] <= 800):
                fontSize = 1                    
                y = 30

            cv2.putText(img=image, text=label, org=(x, y), 
                fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=fontSize, 
                color=(0, green, red), thickness=3)

            csv_file.write(data_row)

            # write labeled image
            cv2.imwrite(os.path.join(OUTPUT_DIR, frame_filename), image)   

            # display the resulting frame when X11 is used
            if args['graphical'] == True:
                cv2.imshow('Video', image)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    csv_data.close()
                    break

        # when everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()
    else:
        print("Error opening video device")
        
    return