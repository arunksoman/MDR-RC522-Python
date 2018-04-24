import RPi.GPIO as GPIO
import sys
import values
import time

GPIO.setmode(GPIO.BOARD) #GPIO Nummern statt Board Nummern

RELAIS_1_GPIO = 31 #GPIO 06
RELAIS_2_GPIO = 32 #GPIO 12

GPIO.setwarnings(False)
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) #GPIO Modus zuweisen
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT) #GPIO Modus zuweisen

#GPIO.output(RELAIS_1_GPIO, GPIO.LOW) #an
#GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) #aus
#GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) #aus
#GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) #aus
    
def ralleaus():
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) #aus
    GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) #aus


def relais1an():
	GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
	time.sleep(values.dooropen)
	GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)

def relais2an():
	GPIO.output(RELAIS_2_GPIO, GPIO.LOW) 
	time.sleep(values.dooropen)
	GPIO.output(RELAIS_2_GPIO, GPIO.HIGH)

def relais1anoderaus():
    
    if GPIO.input(31) is 1:
    		GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
    else:
                GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
                
		
def relais2an():
    if GPIO.input(32) is 1:
    		GPIO.output(RELAIS_2_GPIO, GPIO.LOW) 
    else:
                GPIO.output(RELAIS_2_GPIO, GPIO.HIGH)                
	
	
def getrel1state():
    
    if GPIO.input(31) is 1:
        return True
    else:
        return False
	
	#sys.stderr.write("\x1b[2J\x1b[H") #clear screen 

		
def getrel2state():
    
    if GPIO.input(32) is 1:
        return True
    else:
        return False
	
	#sys.stderr.write("\x1b[2J\x1b[H") #clear screen 