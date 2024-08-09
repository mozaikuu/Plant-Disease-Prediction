# %pip install numpy matplotlib tensorflow keras opencv-python
# %pip install --upgrade tensorflow keras


import cv2
import keras
import numpy as np
import tensorflow as tf
from Pymail import *
# from time import sleep
import matplotlib.pyplot as plt
# from multiprocessing import Process
from keras.preprocessing.image import img_to_array

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

image_path = r'./valid/Apple___Apple_scab/00075aa8-d81a-4184-8541-b692b78d398a___FREC_Scab 3335_270deg.jpg'

# # Reading an image in default mode
# img = cv2.imread(image_path)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converting BGR to RGB

# # Displaying the image 
# plt.imshow(img)
# plt.title('Test Image')
# plt.xticks([])
# plt.yticks([])
# plt.show()

image = tf.keras.preprocessing.image.load_img(image_path,target_size=(128,128))
input_arr = tf.keras.preprocessing.image.img_to_array(image)
input_arr = np.array([input_arr])  # Convert single image to a batch.
predictions = cnn.predict(input_arr)

# print(predictions)

result_index = np.argmax(predictions) #Return index of max element
# print(result_index)

# # Displaying the disease prediction
class_name = validation_set.class_names
# model_prediction = class_name[result_index]
# plt.imshow(img)
# plt.title(f"Disease Name: {model_prediction}")
# plt.xticks([])
# plt.yticks([])
# plt.show()

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

# Open the default camera
cap = cv2.VideoCapture(1)

count = 1
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the captured frame
    cv2.imshow('Frame', frame)

    # Preprocess and make predictions
    result_index = predict_disease(frame)
    model_prediction = class_name[result_index]

    # Display the prediction
    print("Predicted Disease:", model_prediction)
    
    if count % 300 == 0:
        auto_email(model_prediction)
        count = 1
    count += 1
    print(count)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break