import platform

# Windows users use the pyttsx3 module
if platform.system()=="Windows":
    import pyttsx3
    
    engine = pyttsx3.init()
    while True:
        inp=input("What do you want to covert to speech?\n")
        if inp=="done":
            print(f"You just typed in {inp}, Goodbye!")
            engine.say(f"You just typed in {inp}, Goodbye!")
            engine.runAndWait()        
            break
        else:
            print(f"You just typed in {inp}.")
            engine.say(f"You just typed in {inp}")
            engine.runAndWait()
            continue

# Non-Windows users use the gtts module
elif  platform.system()=="Darwin" or platform.system()=="Linux":
    import os

    while True:
        inp=input("What do you want to covert to speech?\n")
        if inp=="done":
            inp=f"You just typed in {inp}, Goodbye!"
            print(inp)
            inp=inp.replace(' ','-')
            inp=inp.replace("'","")
            inp=inp.replace('"','')
            os.system(f"gtts-cli --nocheck {inp} | mpg123 -q -")
            break
        else:
            inp=f"You just typed in {inp}."
            print(inp)
            inp=inp.replace(' ','-')
            inp=inp.replace("'","")
            inp=inp.replace('"','')
            os.system(f"gtts-cli --nocheck {inp} | mpg123 -q -")
            continue
