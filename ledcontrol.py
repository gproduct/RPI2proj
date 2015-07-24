import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
try:
        while True:
                GPIO.output(21,1)
                time.sleep(0.1)
                GPIO.output(21,0)
                GPIO.output(16,1)
                time.sleep(0.1)
                GPIO.output(16,0)
                GPIO.output(13,1)
                time.sleep(0.1)
                GPIO.output(13,0)
except KeyboardInterrupt:
        pass


GPIO.cleanup()
