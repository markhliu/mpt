import speech_recognition as sr
speech = sr.Recognizer()
print('Python is listening...')
with sr.Microphone() as source:
    audio = speech.listen(source)
    inp = speech.recognize_google(audio)
print(f'You just said {inp}.') 
