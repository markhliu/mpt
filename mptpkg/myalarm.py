import time

import arrow

from mptpkg import print_say


# Define the Alarm() function
def alarm(v_inp):
    # Find the positions of the four indicators
    p1 = v_inp.find("alarm for")
    p2 = v_inp.find("a.m.")
    p3 = v_inp.find("p.m.")
    p4 = v_inp.find(":")
    # Handle the four different cases
    if p2 != -1 and p4 != -1:
        v_inp = v_inp[p1 + len("alarm for") + 1:p2] + "AM"
    elif p3 != -1 and p4 != -1:
        v_inp = v_inp[p1 + len("alarm for") + 1:p3] + "PM"
    elif p2 != -1 and p4 == -1:
        v_inp = v_inp[p1 + len("alarm for") + 1:p2 - 1] + ":00 AM"
    elif p3 != -1 and p4 == -1:
        v_inp = v_inp[p1 + len("alarm for") + 1:p3 - 1] + ":00 PM"
    # Tell you when the alarm will go off
    print_say(f"OK, your alarm will go off at {v_inp}!")
    while True:
        # Obtain time and change it to "7:25 AM" format
        tm = arrow.now().format('h:mm A')
        time.sleep(5)
        # If the clock reaches the preset time, the alarm clock goes off
        if v_inp == tm:
            print_say("Your alarm has gone off!")
            break
