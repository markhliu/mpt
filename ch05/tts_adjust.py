# Mac and Linux users: skip this scipt
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.2)
engine.say("This is a test of my speech id, speed, and volume.")
engine.runAndWait ()
