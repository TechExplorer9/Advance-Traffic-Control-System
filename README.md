Advanced Traffic Control System with Computer Vision
Author: Atharva Vitekar

Overview
This repository contains the source code and documentation for an Advanced Traffic Control System using computer vision. The system utilizes OpenCV, YOLO (You Only Look Once), Darknet, and runs on a Linux OS, specifically designed and tested on a Raspberry Pi with a camera module.

The key feature of this project is its ability to dynamically adjust traffic signal timings based on the detection of priority vehicles, such as ambulances. The system employs YOLO for real-time object detection, allowing it to recognize emergency vehicles and adjust traffic signal timings accordingly.

Features
Real-time object detection using YOLO and Darknet
Priority vehicle recognition (e.g., ambulances)
Dynamic adjustment of traffic signal timings
LED output to showcase the updated signal state

Hardware Requirements
Raspberry Pi
Camera Module for Raspberry Pi
LEDs for signal output

Software Requirements
Linux OS (Tested on Raspberry Pi OS)
OpenCV
YOLO (Darknet)

To achieve this project, you'll need to follow several steps. First, you'll need to set up Darknet with YOLO (You Only Look Once) for object detection. Then, you'll integrate this with a Python script to control a Raspberry Pi GPIO pin for the green LED.

Here are the high-level steps:

Install Darknet with YOLO on your system.
Set up the YOLO weights file and configuration file.
Write a Python script for YOLO object detection.
Integrate Raspberry Pi GPIO control for the green LED.
Assuming you have Darknet and YOLO set up, here's a simple Python script using the subprocess module to run Darknet for object detection. This script also includes the integration with Raspberry Pi GPIO using the RPi.GPIO library:

Make sure to replace <image_path> with the actual path to the image you want to process.

Note: The actual paths and configuration details might vary based on your setup. Adjust the paths and pins according to your requirements. Additionally, you need to install the necessary dependencies and libraries on your Raspberry Pi, such as RPi.GPIO.

Keep in mind that this is a basic example, and you may need to fine-tune it based on your specific requirements and the structure of your Darknet setup.