#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522


continue_reading = True
reading_count = 0

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

    
def read_card():
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        (status,uid) = MIFAREReader.MFRC522_Anticoll() # Get the UID of the card
        uid_concatenated = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])+str(uid[4]) #Baut UID zusammen
        return uid_concatenated
    
    
  
		


