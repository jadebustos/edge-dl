# README

These are the notebooks used in my Master Thesis to detect violence situations.

H5 models are not included due to they exceed GitHub storage limits.

## CNN models

Several models have been tested:

* ResNet50
* InceptionV3
* InceptionResnetV2
* VGG16
* VGG19
* Xception

### Creating the dataset

The notebook [dataset-preparation.ipynb](dataset-preparation.ipynb) is used to extract images from videos for the train and validations dataset. All the images are resized to 200x200 by default.

You will have to download the video dataset, uncompress it and set the directory.

If you prefer to use a different image size do not forget to modify the notebooks for the training.

### Training the models

The notebooks you can use to train the models are named as **model_name-trained-...**.

## Testing the models

Several playbooks are provided. You will have to set the directory to read the videos and the h5 filename lo load the trained model.

* **model_name-testing.ipynb** tests the model against the test dataset. The video is labeled as violence or non-violence.
* **model_name-testing_frames.ipynb** tests the model against the test dataset. Frames will be labeled as violence or non-violence.
* **model_name-testing-airtlab.ipynb** tests the model against the Airtlab dataset.
* **model_name-testing-fight-detection-surv-dataset.ipynb** tests the model against the Fight Detection Surveillance dataset.

## CNN + LSTM model

Althouh LSTM models were out of the scope for my Master Thesis I though that will be interesting to test some LSTM models.

### Creating the dataset

The notebook [lstm-dataset-preparation.ipynb](lstm-dataset-preparation.ipynb) is used to extract images from videos for the train and validation dataset. All the images are resized to 200x200 by default.

You will have to download the video dataset, uncompress it and set the directory.

If you prefer to use a different image size do not forget to modify the notebooks for the training.

### Training the model

Unfortunately I did not have enough time to train a good LSTM model. As you can see in the performance graphs there is room for improvement.

Although, this model is useless it is interesting understand how data is loaded to be used for the LSTM model, and the input shape as well.

For the CNNs the input shape is [200,200,3]. So, if the dataset image has 9600 images the data shape will be [9600,200,200,3].

LSTM processes sequences. That means that instead of loading an image a sequence will be loaded. If the dataset has 300 videos and we sample 16 frames for each video the data shape will be [300,16,200,200,3].

### Testing the model

As the model is not a good one I did not test the test dataset. I will add an example of how testing is done with LSTM.