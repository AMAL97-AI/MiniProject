import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.IN)
GPIO.setup(15, GPIO.IN)

import os

os.system("cd /home/pi/Desktop/New/darknet")
while True:
	print ("checking for input")
	if GPIO.input(15) == GPIO.HIGH:
		os.system("raspistill -o /home/pi/Desktop/New/darknet/images/img.jpg")
		os.system("./darknet detector test  /home/pi/Desktop/New/darknet/cfg/voc.data /home/pi/Desktop/New/darknet/cfg/yolov2-tiny-voc.cfg /home/pi/Desktop/New/darknet/cfg/yolov2-tiny-voc.weights /home/pi/Desktop/New/darknet/images/img.jpg -dont_show < data/train.txt > /home/pi/Desktop/New/darknet/result.txt")
		os.system("python /home/pi/Desktop/New/darknet/cleaning.py")
		os.system("python3 /home/pi/Desktop/New/darknet/sound.py")
	if GPIO.input(16) == GPIO.HIGH:
		break
