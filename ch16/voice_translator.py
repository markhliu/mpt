from io import BytesIO

from translate import Translator
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Initiate speech recognition
speech = sr.Recognizer()
# Prompt you to say something in English
print('say something in English')    
# Capture spoken English 
with sr.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    try:
        audio = speech.listen(source)
        my_input = speech.recognize_google(audio, language="en")
        print(f"you said: {my_input}")    
    except sr.UnknownValueError:
        pass
# Specify the input and output languages
translator = Translator(from_lang="en",to_lang="es")
# Do the actual translation
translation = translator.translate(my_input)
print(translation)
# Convert text to speech in Spanish
tts = gTTS(text=translation,lang='es')
# Create a temporary file 
voice = BytesIO()
# Save the voice output as an audio file
tts.write_to_fp(voice)
# Play the audio file
voice.seek(0)
play(AudioSegment.from_mp3(voice))
# Prompt you to say something in Spanish
print('say something in Spanish')    
# Capture spoken Spanish 
with sr.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    try:
        audio = speech.listen(source)
        my_input = speech.recognize_google(audio, language="es")
        print(f"you said: {my_input}")    
    except sr.UnknownValueError:
        pass
# Specify the input and output languages
translator = Translator(from_lang="es",to_lang="en")
# Do the actual translation
translation = translator.translate(my_input)
print(translation)
# Convert text to speech in Spanish
tts = gTTS(text=translation,lang='en')
# Create a temporary file 
voice = BytesIO()
# Save the voice output as an audio file
tts.write_to_fp(voice)
# Play the audio file
voice.seek(0)
play(AudioSegment.from_mp3(voice))
