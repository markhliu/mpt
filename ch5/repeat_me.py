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
    from io import BytesIO
    
    from pydub import AudioSegment
    from pydub.playback import play
    from gtts import gTTS
    
    def print_say(text):
    
        print(text)
        voice=BytesIO()
        mytts=gTTS(text = text, lang = 'en', slow=False)
        mytts.write_to_fp(voice)
        voice.seek(0)
        play(AudioSegment.from_mp3(voice))
    
    # Make sure you put mysr.py in the same folder as this script
    from mysr import voice_to_text

    while True:
        print('Python is listening...')
        inp=voice_to_text()
        if inp=="stop listening":
            inp=f"You just said {inp}, Goodbye!"
            print(inp)
            voice=BytesIO()
            mytts=gTTS(text = inp, lang = 'en', slow=False)
            mytts.write_to_fp(voice)
            voice.seek(0)
            play(AudioSegment.from_mp3(voice))
            break
        else:
            inp=f"You just said {inp}."
            print(inp)
            voice=BytesIO()
            mytts=gTTS(text = inp, lang = 'en', slow=False)
            mytts.write_to_fp(voice)
            voice.seek(0)
            play(AudioSegment.from_mp3(voice))
            continue
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

