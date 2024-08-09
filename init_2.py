import RPi.GPIO as gpio
import cv2
import keras
import numpy as np
import tensorflow as tf
from Pymail import *
import matplotlib.pyplot as plt
from keras.preprocessing.image import img_to_array
from picamera2 import Picamera2, Preview
import time
from Test_plant_disease import *
from test_soilsensor_blynk import *
#from RPICloud import *

# Define GPIO pins for wheel control
wheel1_pwm = 2
wheel2_pwm = 3
wheel3_pwm = 17
wheel4_pwm = 22

# Define GPIO pins for motor control
h1i1 = 19
h1i3 = 13
h2i1 = 24
h2i3 = 12
h1i2 = 27
h1i4 = 16
h2i2 = 25
h2i4 = 6

# Define PWM parameters
frequency = 50  # Hertz for servo control
min_duty_cycle = 2.5  # Duty cycle for 0 degrees
max_duty_cycle = 12.5  # Duty cycle for 180 degrees
wheel_frequency = 1000  # Frequency for wheel speed control (1 kHz)

soil_moisture = soil_moisture_sensor()


# Function to convert angle to duty cycle
def angle_to_duty_cycle(angle):
    return min_duty_cycle + (angle / 180.0) * (max_duty_cycle - min_duty_cycle)

# Initialize GPIO pins
def init():
    gpio.setmode(gpio.BCM)
    
    # Setup motor control pins
    gpio.setup(h1i1, gpio.OUT)
    gpio.setup(h1i2, gpio.OUT)
    gpio.setup(h1i3, gpio.OUT)
    gpio.setup(h1i4, gpio.OUT)
    gpio.setup(h2i1, gpio.OUT)
    gpio.setup(h2i2, gpio.OUT)
    gpio.setup(h2i3, gpio.OUT)
    gpio.setup(h2i4, gpio.OUT)
    
    # Setup PWM pins for wheels
    gpio.setup(wheel1_pwm, gpio.OUT)
    gpio.setup(wheel2_pwm, gpio.OUT)
    gpio.setup(wheel3_pwm, gpio.OUT)
    gpio.setup(wheel4_pwm, gpio.OUT)
    
    # Initialize motor control pins to False
    gpio.output(h1i1, False)
    gpio.output(h1i3, False)
    gpio.output(h2i1, False)
    gpio.output(h2i3, False)
    gpio.output(h1i2, False)
    gpio.output(h1i4, False)
    gpio.output(h2i2, False)
    gpio.output(h2i4, False)

# Function to set wheel speed using PWM
def set_wheel_speed(pwm_instances, duty_cycle):
    for pwm in pwm_instances:
        pwm.ChangeDutyCycle(duty_cycle)

# Function to move forward
def reverse(sec, duty_cycle):
    init()
    gpio.output(h1i2, False)
    gpio.output(h1i4, False)
    gpio.output(h2i2, True)
    gpio.output(h2i4, True)
    gpio.output(h1i1, True)
    gpio.output(h1i3, True)
    gpio.output(h2i1, False)
    gpio.output(h2i3, False)
    
    # Set wheel speed
    set_wheel_speed([pwm_wheel1, pwm_wheel2, pwm_wheel3, pwm_wheel4], duty_cycle)
    
    time.sleep(sec)
    gpio.cleanup()

# Function to move backward
def forward(sec, duty_cycle):
    init()
    gpio.output(h1i1, False)
    gpio.output(h1i3, False)
    gpio.output(h2i1, True)
    gpio.output(h2i3, True)
    gpio.output(h1i2, True)
    gpio.output(h1i4, True)
    gpio.output(h2i2, False)
    gpio.output(h2i4, False)
    
    # Set wheel speed
    set_wheel_speed([pwm_wheel1, pwm_wheel2, pwm_wheel3, pwm_wheel4], duty_cycle)
    
    time.sleep(sec)
    gpio.cleanup()

# Initialize GPIO and PWM
init()

# Setup PWM for wheels
pwm_wheel1 = gpio.PWM(wheel1_pwm, wheel_frequency)
pwm_wheel2 = gpio.PWM(wheel2_pwm, wheel_frequency)
pwm_wheel3 = gpio.PWM(wheel3_pwm, wheel_frequency)
pwm_wheel4 = gpio.PWM(wheel4_pwm, wheel_frequency)

pwm_wheel1.start(0)
pwm_wheel2.start(0)
pwm_wheel3.start(0)
pwm_wheel4.start(0)

# Define duty cycle for 40 RPM
# Adjust this value based on your motor's specifications
duty_cycle_40_rpm = 50  # Example value, may need to be adjusted

# Initialize the camera
picam2 = Picamera2()
# Create the camera configuration
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
# Configure the camera
picam2.configure(camera_config)
# Start the camera preview
picam2.start_preview(Preview.QTGL)
# Start the camera
picam2.start()
# Allow the camera to warm up and adjust to light levels
time.sleep(1)


first_run = True

# Main loop
seconds = 5
while True:
    time.sleep(seconds)
    print("forward")
    forward(seconds, duty_cycle_40_rpm)
    time.sleep(1)
    
    gpio.setmode(gpio.BCM)

    # Set the GPIO pins for the servos
    servo360_1 = 20
    servo360_2 = 21
    servo180 = 26

    # Setup GPIO pins for output
    gpio.setup(servo360_1, gpio.OUT)
    gpio.setup(servo360_2, gpio.OUT)
    gpio.setup(servo180, gpio.OUT)

    # Create PWM instances for servos
    pwm360_1 = gpio.PWM(servo360_1, frequency)
    pwm360_2 = gpio.PWM(servo360_2, frequency)
    pwm180 = gpio.PWM(servo180, frequency)
    pwm360_1.start(0)
    pwm360_2.start(0)
    pwm180.start(0)
    
    time.sleep(3)
    pwm360_1.ChangeDutyCycle(angle_to_duty_cycle(90 % 181))
    time.sleep(1)
    pwm360_1.ChangeDutyCycle(angle_to_duty_cycle(0 % 181))
    time.sleep(1)
    pwm360_2.ChangeDutyCycle(angle_to_duty_cycle(90 % 181))
    time.sleep(1)
    pwm360_2.ChangeDutyCycle(angle_to_duty_cycle(0 % 181))
    time.sleep(1)
    pwm180.ChangeDutyCycle(angle_to_duty_cycle(180))
    time.sleep(1)
    pwm180.ChangeDutyCycle(angle_to_duty_cycle(0))
    time.sleep(seconds - 0.2)
    
    
    
    picam2.capture_file("test.jpg")
    img = cv2.imread("test.jpg")
    
    # result_index = predict_disease(img)
    # model_prediction = class_names[result_index]
    # print("Predicted Disease:", model_prediction)
    # prep_and_send_email(model_prediction, soil_moisture)
    # count = 1
    # count += 1
    # print(count)
    
    if first_run == True:
        if isplant(img):
            print("Plant detected")
            # print("stuck2")
            first_run = False
            skip = True
        else:
            skip = False
            print("no plant detected")
            # print("stuck1")
            # sys.exit() #make it wait 5 seconds and try again
    
    if skip:
        result_index = predict_disease(img)
        model_prediction = class_names[result_index]
        print("Predicted Disease:", model_prediction)
        # print("stuck3")
        
        if count % 300 == 0:
            # if "healthy" in model_prediction.lower():
            #     count = 299
            # else:        
                prep_and_send_email(model_prediction, soil_moisture_sensor_Email())
                count = 0
                # print("stuck5")
        count += 1
        print(count)
        
        # myData()
    else:
        time.sleep(5)
        # print("stuck7")
        
    # print("stuck8")


    time.sleep(2)
    if cv2.waitKey(1) == ord('q'):
        picam2.stop()
        cv2.destroyAllWindows()
        break

# Cleanup PWM instances
pwm_wheel1.stop()
pwm_wheel2.stop()
pwm_wheel3.stop()
pwm_wheel4.stop()
gpio.cleanup()
