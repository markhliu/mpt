# make sure you put all local modules in the program folder
from myWakeUp import VTT, WakeUp
from mySAY import printAndSAY
from TimerMode import Timer
from AlarmMode import Alarm
from JokeMode import Joke
from EmailMode import Email
from KnowAllMode import KnowAll

# put the program in standby
while True:
    # capture your voice command quietly in standby
    ToWakeUp = WakeUp()
    # you can wake up the program by saying "Hello Python"
    while ToWakeUp == "Activated":   
        printAndSAY("how may I help you?")
        inp=VTT().lower()
        printAndSAY(f'you just said {inp}')
        if "back" in inp and "stand" in inp:
            printAndSAY('OK, back to standby, let me know if you need help!')
            break
        # activate the timer mode
        elif "timer for" in inp and ("hour" in inp or "minute" in inp):
            Timer(inp)
            continue        
        # activate the alarm clock mode
        elif "alarm for" in inp and ("a.m." in inp or "p.m." in inp):
            Alarm(inp)
            continue
        # activate the joke-telling mode
        elif "joke" in inp and "tell" in inp:
            Joke()
            continue
        # activate the email-sending mode
        elif "send" in inp and "email" in inp:
            Email()
            continue
        # activate the know-it-all mode
        else:
            KnowAll(inp)
            continue
    # you can end the program by saying "stop the program"
    if ToWakeUp == "ToQuit":
        printAndSAY("OK, exit the program, goodbye!")
        break