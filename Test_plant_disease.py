import cv2
import keras
import numpy as np
import tensorflow as tf
from Pymail import *
import matplotlib.pyplot as plt
from keras.preprocessing.image import img_to_array
# from picamera2 import Picamera2, Preview
import time
from test_soilsensor import *
from PIL import Image

# Define the directory path
directory_path = './valid'

# Create the dataset
validation_set = tf.keras.utils.image_dataset_from_directory(
    directory_path,
    labels="inferred",
    label_mode="categorical",
    class_names=None,
    color_mode="rgb",
    batch_size=32,
    image_size=(128, 128),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation="bilinear",
    follow_links=False,
    crop_to_aspect_ratio=False
)

# Get the class names
class_names = validation_set.class_names
print(class_names)

cnn = tf.keras.models.load_model('./trained_plant_disease_model.h5')

# Function to preprocess and make predictions on the image
def predict_disease(image):
    # Preprocess the image
    image = cv2.resize(image, (128, 128))
    input_arr = img_to_array(image)
    input_arr = np.array([input_arr])

    # Make predictions
    predictions = cnn.predict(input_arr)
    result_index = np.argmax(predictions)

    return result_index

# Email Counter Variable
count = 1

def isplant(plant_pic):
    # Convert the image to RGB if it's in BGR format
    img = Image.fromarray(cv2.cvtColor(plant_pic, cv2.COLOR_BGR2RGB))

    # Convert the image to HSV
    hsv_img = img.convert('HSV')

    # Extract the Hue channel
    Hue = np.array(hsv_img.getchannel('H'))

    # Create a mask for green pixels
    mask = np.zeros_like(Hue, dtype=np.uint8)

    # Set the green pixel range (35 to 85 in hue for green)
    mask[(Hue >= 35) & (Hue <= 85)] = 1

    # Calculate the percentage of green pixels
    green_percentage = mask.mean() * 100
    print(green_percentage)
    
    # Check if the image contains more than 50% green pixels
    if green_percentage > 20:
        return predict_disease(plant_pic)
        # return True
    elif green_percentage <= 20:
        not_a_plant = True
        # return False

