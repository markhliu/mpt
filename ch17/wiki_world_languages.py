from io import BytesIO

import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import wikipedia

# Create a dictionary of languages and the corresponding codes
lang_abbre={"english":"en",
            "chinese":"zh-cn",
            "spanish":"es-es",
            "french":"fr-fr",
            "japanese":"ja",
            "portuguesE":"pt",
            "russian":"ru",
            "korean":"ko",
            "german":"de",
            "italian":"it"}
lang=input("What language you want to use?\n")

# Initiate speech recognition
speech = sr.Recognizer()      
# Ask what you want to know
print(f"Say what you want to know in {lang}...")
# Capture your voice query in the language of your choice
with sr.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    try:
        audio = speech.listen(source)
        my_input = speech.recognize_google(audio, language=lang_abbre[lang][0:2])   
    except sr.UnknownValueError:
        pass
# Print out what you said
print(f"you said: {my_input}")
# Obtain answer from Wikipedia and print out
wikipedia.set_lang(lang_abbre[lang][0:2])
ans=wikipedia.summary(my_input)[0:200]
print(ans)
# Convert text to speech in the language of your choice
tts=gTTS(text=ans,lang=lang_abbre[lang])
# Create a temporary file 
voice=BytesIO()
# Save the voice output as an audio file
tts.write_to_fp(voice)
# Play the audio file
voice.seek(0)
play(AudioSegment.from_mp3(voice))

