import pyttsx3
engine = pyttsx3.init()
voice_id = 0
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[voice_id].id)
engine.setProperty('rate', 160)
engine.setProperty('volume', 0.8)
engine.say("This is a test of my speech id, speed, and volume.")
engine.runAndWait()        
