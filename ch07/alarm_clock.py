import time

import arrow

# Tell you the format to set the timer
print('''set your alarm clock\nyou can use the format of:\n
      \tset an alarm for 7 a.m., or
      \tset an alarm for 2:15 p.m.''')
# Set the timer
inp = input("How do you want to set your alarm clock?\n")
# Find the positions of "timer for" and "hour" and "minute"
p1 = inp.find("alarm for")
p2 = inp.find("a.m.")
p3 = inp.find("p.m.")
p4 = inp.find(":")
# Handle the four different cases
if p2 != -1 and p4 != -1:
    inp = inp[p1 + len("alarm for") + 1:p2] + "AM"
elif p3 != -1 and p4 != -1:
    inp = inp[p1 + len("alarm for") + 1:p3] + "PM"
elif p2 != -1 and p4 == -1:
    inp = inp[p1 + len("alarm for") + 1:p2 - 1] + ":00 AM"
elif p3 != -1 and p4 == -1:
    inp = inp[p1 + len("alarm for") + 1:p3 - 1] + ":00 PM"

print(f"OK, your alarm will go off at {inp}!")
while True:
    # Obtain time and change it to "7:25 AM" format
    tm = arrow.now().format('h:mm A')
    time.sleep(5)
    # If the clock reaches alarm time, the alarm clock goes off
    if inp == tm:
        print("Your alarm has gone off!")
        break
