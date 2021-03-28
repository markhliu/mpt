from mptpkg import print_say

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

# Import the platform module to identify your OS
import platform

# If you are using Windows, use gtts
if platform.system() == "Windows": 
    import random
    
    from translate import Translator
    from gtts import gTTS
    from pydub import AudioSegment
    from pydub.playback import play
    
    def voice_translate(inp):
        # Extract the phrase and the language name
        ps1 = inp.find('how to say')
        ps2 = inp.rfind(' in ')
        try:
            eng_phrase = inp[ps1+10:ps2]
            tolang = inp[ps2+4:]
            translator = Translator(from_lang="english",to_lang=tolang)
            translation = translator.translate(eng_phrase)
            tts = gTTS(text=translation, lang=lang_abbre[tolang])
            print_say(f"The {tolang} for {eng_phrase} is")
            print(translation)
            x = random.choice(range(1000000))
            tts.save(f'file{x}.mp3')
            play(AudioSegment.from_mp3(f"file{x}.mp3"))
        except:
            print_say("sorry, cannot find what you are looking for!")

# If you are not using Windows, use gtts-cli
if  platform.system() == "Darwin" or platform.system() == "Linux":
    import os
    from translate import Translator
    from gtts import gTTS

    def voice_translate(inp):
        # Extract the phrase and the language name
        ps1 = inp.find('how to say')
        ps2 = inp.rfind(' in ')
        try:
            eng_phrase = inp[ps1+10:ps2]
            tolang = inp[ps2+4:]
            translator = Translator(from_lang="english",to_lang=tolang)
            translation = translator.translate(eng_phrase)
            print_say(f"The {tolang} for {eng_phrase} is")
            print(translation)
            tr = translation.replace('"','')
            ab = lang_abbre[tolang]
            os.system(f'gtts-cli --nocheck "{tr}" --lang {ab} | mpg123 -q -')               
        except:
            print_say("sorry, cannot find what you are looking for!")
