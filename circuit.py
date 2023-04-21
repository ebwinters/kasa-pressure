import RPi.GPIO as GPIO
import asyncio
from control_lights import *
import redis
import sys

loop = None
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
def button_callback(up_down):
    print('changing voltage event detected')
    bulb_ips = str(r.get('bulb_ips')).split(',')
    asyncio.run(up_down(bulb_ips))
    

if __name__ == '__main__':
    try:
        # setup the GPIO
        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
        GPIO.add_event_detect(10, GPIO.RISING, callback=lambda x: button_callback(up_down), bouncetime=500)
        print ("Running smart light circuit...")
        # run the event loop
        loop = asyncio.get_event_loop()
        loop.run_forever()
        loop.close()
    except :
        print("Error:", sys.exc_info()[0])

    GPIO.cleanup()
