# import needed modules
import time

import arrow

# make sure you put mySAY.py in the same folder as this program
from mySAY import printAndSAY

#define the Alarm() function
def Alarm(v_inp):
    # find the positions of the four indicators
    p1=v_inp.find("alarm for") 
    p2=v_inp.find("a.m.") 
    p3=v_inp.find("p.m.") 
    p4=v_inp.find(":")  
    # handle the four different cases
    if p2 != -1 and p4 != -1: v_inp=v_inp[p1+len("alarm for")+1:p2]+"AM"
    elif p3 != -1 and p4 != -1: v_inp=v_inp[p1+len("alarm for")+1:p3]+"PM" 
    elif p2 != -1 and p4 == -1: v_inp=v_inp[p1+len("alarm for")+1:p2-1]+":00 AM"        
    elif p3 != -1 and p4 == -1: v_inp=v_inp[p1+len("alarm for")+1:p3-1]+":00 PM"       
    # tell you when the alarm will go off
    printAndSAY(f"OK, your alarm will go off at {v_inp}!")
    while True:
        #obtain time and change it to "7:25 AM" format
        tm=arrow.utcnow().format('h:mm A')
        time.sleep(5)
        #if the clock reaches the preset time, the alarm clock goes off
        if v_inp==tm:
            printAndSAY("Your alarm has gone off!")
            break 
