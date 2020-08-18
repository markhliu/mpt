
import speech_recognition as sr

speech = sr.Recognizer()


def VTT():
    voice_input="" 
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
    return voice_input
