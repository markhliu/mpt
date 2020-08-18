import platform

if platform.system()=="Windows":
    
    import pyttsx3
    
    try:
        engine = pyttsx3.init()
    except ImportError:
        pass
    except RuntimeError:
        pass
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.2)
    

    
    def printAndSAY(txt):
        print(txt)
        engine.say(txt)
        engine.runAndWait()

# non Windows users should pip install pydub
elif  platform.system()=="Darwin" or platform.system()=="Linux":
    
    #import needed modules
    from pydub import AudioSegment
    from pydub.playback import play
    import random
    from gtts import gTTS
    
    def printAndSAY(mytext):
        print(mytext)
        try:
            tts = gTTS(text=mytext, lang='en')
        except:pass
        x = random.choice(range(1000000))
        tts.save(f'file{x}.mp3')
        play(AudioSegment.from_mp3(f"file{x}.mp3"))
        

'''
if you cannot install pydub, then pip install playsound

then use the following: 


elif  platform.system()=="Darwin" or platform.system()=="Linux":
    
    #import needed modules
    from playsound import playsound
    import random
    from gtts import gTTS
    
    def printAndSAY(mytext):
        print(mytext)
        try:
            tts = gTTS(text=mytext, lang='en')
        except:pass
        x = random.choice(range(1000000))
        tts.save(f'file{x}.mp3')
        playsound(f"file{x}.mp3")


'''





