import platform

# Windows users use the pyttsx3 module
if platform.system()=="Windows":
    import pyttsx3
    
    engine = pyttsx3.init()
    engine.say('Hello, how are you?')
    engine.runAndWait()

# Non-Windows users use the gtts module
elif  platform.system()=="Darwin" or platform.system()=="Linux":
    from io import BytesIO
    
    from pydub import AudioSegment
    from pydub.playback import play
    from gtts import gTTS

    voice=BytesIO()
    mytts=gTTS(text = "Hello, how are you?", lang = 'en', slow=False)
    mytts.write_to_fp(voice)
    voice.seek(0)
    play(AudioSegment.from_mp3(voice))
