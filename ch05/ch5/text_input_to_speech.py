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
    from io import BytesIO
    
    from pydub import AudioSegment
    from pydub.playback import play
    from gtts import gTTS
    
    while True:
        inp=input("What do you want to covert to speech?\n")
        if inp=="done":
            inp=f"You just typed in {inp}, Goodbye!"
            print(inp)
            voice=BytesIO()
            mytts=gTTS(text = inp, lang = 'en', slow=False)
            mytts.write_to_fp(voice)
            voice.seek(0)
            play(AudioSegment.from_mp3(voice))
            break
        else:
            inp=f"You just typed in {inp}."
            print(inp)
            voice=BytesIO()
            mytts=gTTS(text = inp, lang = 'en', slow=False)
            mytts.write_to_fp(voice)
            voice.seek(0)
            play(AudioSegment.from_mp3(voice))
            continue
        
        
        
