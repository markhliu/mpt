import pyttsx3
engine = pyttsx3.init()
voice_id = 1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[voice_id].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.2)
engine.say("This is a test of my speech id, speed, and volume.")
engine.runAndWait()        
