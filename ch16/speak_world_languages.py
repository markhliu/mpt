from io import BytesIO

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Create a dictionary of languages and the corresponding codes
lang_abbre = {"english":"en",
            "chinese":"zh",
            "spanish":"es",
            "french":"fr",
            "japanese":"ja",
            "portuguese":"pt",
            "russian":"ru",
            "korean":"ko",
            "german":"de",
            "italian":"it"}
lang = input("What language you want to use?\n")
phrase = input("What phrase you want to convert to voice?\n")
# Convert text to speech
tts = gTTS(text=phrase,lang=lang_abbre[lang])
# Create a temporary file 
voice = BytesIO()
# Save the voice output as an audio file
tts.write_to_fp(voice)
# Play the audio file
voice.seek(0)
play(AudioSegment.from_mp3(voice))
