import time
import arrow

# Tell you the format to set the timer
print('''set your timer; you can set it to the number of hours,
      number of minutes, 
      or a combination of both ''')
# Set the timer
inp = input("How long do you want to set your timer for?\n")
# Find the positions of "timer for" and "hour" and "minute"
pos1 = inp.find("timer for")
pos2 = inp.find("hour")
pos3 = inp.find("minute")
# Handle the case "set a timer for hours only"
if pos3 == -1:
    addhour = inp[pos1 + len("timer for"):pos2]
    addminute = 0
# Handle the case "set a timer for minutes only"
elif pos2 == -1:
    addhour = 0
    addminute = inp[pos1 + len("timer for"):pos3]
# Handle the case for "set a timer for hours and minutes
else:
    addhour = inp[pos1 + len("timer for"):pos2]
    addminute = inp[pos2 + len("hour"):pos3]
# Current hour, minute, and second
startHH = arrow.now().format('H')
startmm = arrow.now().format('m')
startss = arrow.now().format('s')
# Obtain the time for the timer to go off
newHH = int(startHH) + int(addhour)
newmm = int(startmm) + int(addminute)
if newmm > 59:
    newmm -= 60
    newHH += 1
newHH = newHH % 24
end_time = str(newHH) + ":" + str(newmm) + ":" + startss
print("Your timer will go off at " + end_time)
while True:
    timenow = arrow.now().format('H:m:s')
    if timenow == end_time:
        print("Your timer has gone off!")
        break
    time.sleep(0.5)
