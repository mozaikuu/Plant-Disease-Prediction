import RPi.GPIO as GPIO
import time

# GPIO setup
sensor_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

# wouldnt this stop everything and run???? Changed By moussa (for blame 😋)

def soil_moisture_sensor():
        # Read soil moisture data
        if GPIO.input(sensor_pin):
            soil_moisture = 0 # dry
            return soil_moisture
        else:
            soil_moisture = 1 # wet
            return soil_moisture
        
def soil_moisture_sensor_Email():
        # Read soil moisture data
        if GPIO.input(sensor_pin):
            return "Soil is Dry"
        else:
            return "Soil is Wet"
            
        
GPIO.cleanup()

