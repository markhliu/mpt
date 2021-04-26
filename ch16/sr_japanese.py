import speech_recognition as sr

# Initiate speech recognition
speech = sr.Recognizer()      
# Use it to capture spoken Japanese 
print('Python is listening in Japanese...')
with sr.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    try:
        audio = speech.listen(source)
        my_input = speech.recognize_google(audio, language="ja")
        print(f"you said: {my_input}")    
    except sr.UnknownValueError:
        pass
