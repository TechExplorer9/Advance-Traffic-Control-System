"""
Author @Atharva Vitekar
"""
import subprocess
import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
GREEN_LED_PIN = 18  # Change this to your GPIO pin
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)

def detect_ambulance():
    # Run Darknet YOLO detection
    darknet_cmd = "./darknet detector test src/cfg/coco.data cfg/ambulance_yolov3-tiny.cfg src/weights/ambulance_yolov3-tiny_400.weights </test/ambulance.jpg>"
    result = subprocess.run(darknet_cmd, shell=True, capture_output=True, text=True)

    # Check if "ambulance" is in the detection result
    if "ambulance" in result.stdout:
        return True
    else:
        return False

def control_led():
    # Set the LED on for a specific duration
    GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
    time.sleep(10)  # Adjust this time duration as needed
    GPIO.output(GREEN_LED_PIN, GPIO.LOW)

if __name__ == "__main__":
    try:
        while True:
            if detect_ambulance():
                control_led()
            time.sleep(1)  # Adjust the frequency of detection
    except KeyboardInterrupt:
        GPIO.cleanup()
