# Make sure you put mysr.py in the same folder as this script
from mysr import voice_to_text

import platform
if platform.system() == "Windows":
    import pyttsx3
    engine = pyttsx3.init()
else:
    import os
    
while True:   
    print('Python is listening...')
    inp = voice_to_text()
    
    if inp == "stop listening":
        print(f'You just said {inp}, goodbye!')
        if platform.system() == "Windows":
            engine.say(f'You just said {inp}, goodbye!')
            engine.runAndWait()
        else:
            os.system(f'gtts-cli --nocheck "You just said {inp}, goodbye!" | mpg123 -q -')
        break

    else:
        print(f'You just said {inp}')
        if platform.system() == "Windows":
            engine.say(f'You just said {inp}')
            engine.runAndWait()
        else:
            os.system(f'gtts-cli --nocheck "You just said {inp}" | mpg123 -q -')
        continue
