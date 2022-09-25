# Copyright (c) 2022 Jose Angel de Bustos Perez
# May be copied or modified under the terms of 
# the GNU General Public License v3.0. 
# See https://www.gnu.org/licenses/gpl-3.0.html

import numpy as np
import cv2
import os

from myvars import *

# predict videos
# model: model used to predict
# videos: video names
# frame_step: sampling ratio
# videos_path: directory to read videos
# args: command line args

def predict_videos(model, videos, videos_path, args):

    # test model using test dataset
    for video in videos:
        # store video predictions in csv file
        csv_data = ["File;Prediction;Probability"]
        # create directory to store images
        dir_basename = os.path.splitext(video)[0]
        predictions_dir = os.path.join(OUTPUT_DIR, dir_basename)     
        try:
            os.mkdir(predictions_dir)
            csv_file = open(os.path.join(predictions_dir, dir_basename + '.csv'), "w")
        except Exception as e:
            print("*************************************************")
            print("Error writing to filesystem %s." % predictions_dir)
            print("*************************************************")
            print(e)
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            exit(252)
        # open video
        video_path = os.path.join(videos_path, video)
        print("Procesing video: %s" % video_path)
        try:
            vidcap = cv2.VideoCapture(video_path)
            length = int(vidcap. get(cv2. CAP_PROP_FRAME_COUNT))
            video_frames = []
            frames_filenames = []
            # select frames every 5 frames
            frame_index = 1
            while frame_index <= length:
                try:
                    # position video frame
                    vidcap.set(1, frame_index)
                    sucess, image = vidcap.read()
                    if not sucess:
                        frame_index += FRAMES_STEP
                        continue
                    image_filename = os.path.join(predictions_dir, dir_basename + '-' + str(frame_index) + '.png')
                    frames_filenames.append(image_filename)
                    cv2.imwrite(image_filename, image)
                    resized = cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT))
                    video_frames.append(resized)

                    # increment index
                    frame_index += FRAMES_STEP
                except Exception as e:
                    frame_index += FRAMES_STEP
                    print("*************************************************")
                    print(e) 
                    print("Video %s." % video)
                    print("*************************************************")                               
                    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            # close video capture
            vidcap.release() 

            # predict using model
            frames = (np.array(video_frames).astype('float32'))/255
            prediction = model.predict(frames)
            
            # label frames
            for item in range(len(frames_filenames)):
                if prediction[item][0] > 0.5:
                    prob = round(100 * prediction[item][0], 2)
                    label = "Non-Violence: " + str(prob) + ' %'
                    # text color
                    red = 0
                    green = 255
                    csv_data.append(frames_filenames[item].split('/')[-1] + ';' 
                        + 'Non-Violence' + ';' + str(prediction[item][0]))
                else:
                    prob = round(100 * (1. - prediction[item][0]), 2)
                    label = "Violence: " + str(prob) + ' %'
                    # text color
                    red = 255
                    green = 0
                    csv_data.append(frames_filenames[item].split('/')[-1] + ';' + 
                        'Violence' + ';' + str(1. - prediction[item][0]))

                # open image to label
                image = cv2.imread(frames_filenames[item])
                    
                # label image
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

                # write labeled image
                cv2.imwrite(frames_filenames[item], image)   

                # display the resulting frame when X11 is used
                if args['graphical'] == True:
                    cv2.imshow('Video', image)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        csv_data.close()
                        break

            # write data to csv and close
            csv_file.write('\n'.join(csv_data))
            csv_file.close()

        except Exception as e:
            print("*************************************************")
            print("Error opening video %s." % video)
            print("*************************************************")
            print(e)            
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")       

    return