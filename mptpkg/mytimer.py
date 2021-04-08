import time

import arrow

from mptpkg import print_say

# Define the timer() function
def timer(v_inp):
    # Find the positions of "timer for" and "hour" and "minute"
    pos1 = v_inp.find("timer for")
    pos2 = v_inp.find("hour")
    pos3 = v_inp.find("minute")
    # Handle the case "set a timer for 2 hours"
    if pos3 == -1:
        addhour = v_inp[pos1+len("timer for"):pos3]
        addminute = 0
    # Handle the case "set a timer for 24 minutes"
    elif pos2 == -1:
        addhour = 0
        addminute = v_inp[pos1+len("timer for"):pos3]
    # Handle the case for "set a timer for 1 hour 30 minutes
    else:
        addhour = v_inp[pos1+len("timer for"):pos2]
        addminute = v_inp[pos2+len("hour"):pos3]      
    # Current hour, minute, and second
    startHH = arrow.now().format('H')
    startmm = arrow.now().format('m')
    startss = arrow.now().format('s')
    # Obtain the time for the timer to go off
    newHH = int(startHH)+int(addhour)
    newmm = int(startmm)+int(addminute)
    if newmm > 59:
        newmm -= 60
        newHH += 1
    newHH = newHH%24  
    end_time = str(newHH)+":"+str(newmm)+":"+startss
    print_say("Your timer will go off at "+end_time)
    while True:
       timenow = arrow.now().format('H:m:s')
       if timenow == end_time:
           print_say("Your timer has gone off!")
           break
       time.sleep(0.5)
