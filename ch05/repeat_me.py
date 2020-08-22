import platform

# Windows users use the pyttsx3 module
if platform.system()=="Windows":
    import pyttsx3
    
    # Make sure you put mysr.py in the same folder as this script
    from mysr import voice_to_text

    engine = pyttsx3.init()
    while True:
        print('Python is listening...')
        inp=voice_to_text()
        if inp=="stop listening":
            print(f"You just said {inp}, Goodbye!")
            engine.say(f"You just typed {inp}, Goodbye!")
            engine.runAndWait()        
            break
        else:
            print(f"You just said {inp}.")
            engine.say(f"You just said {inp}.")
            engine.runAndWait()
            continue

# Non-Windows users use the gtts module
elif  platform.system()=="Darwin" or platform.system()=="Linux":
    import os

    # Make sure you put mysr.py in the same folder as this script
    from mysr import voice_to_text

    while True:
        print('Python is listening...')
        inp=voice_to_text()
        if inp=="stop listening":
            inp=f"You just said {inp}, Goodbye!"
            print(inp)
            inp=inp.replace(' ','-')
            os.system(f"gtts-cli --nocheck {inp} | mpg123 -q -")
            break
        else:
            inp=f"You just said {inp}."
            print(inp)
            inp=inp.replace(' ','-')
            inp=inp.replace("'","")
            inp=inp.replace('"','')
            os.system(f"gtts-cli --nocheck {inp} | mpg123 -q -")
            continue
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

