import platform

# Windows users use the pyttsx3 module
if platform.system()=="Windows":
    import pyttsx3
    
    engine = pyttsx3.init()
    engine.say('Hello, how are you?')
    engine.runAndWait()

# Non-Windows users use the gtts module
elif  platform.system()=="Darwin" or platform.system()=="Linux":
    import os

    os.system('gtts-cli --nocheck "Hello, how are you?" | mpg123 -q -')